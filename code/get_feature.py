import pandas as pd
import numpy as np
import os
from sklearn.metrics import roc_auc_score,log_loss
from sklearn.cross_validation import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import BernoulliNB,GaussianNB,MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import ExtraTreeClassifier,DecisionTreeClassifier

def get_oof_feat(thres=0.5):
    from config import useless_col

    use_col = pd.read_csv('feat_importance.csv')
    use_col = use_col[use_col['importance1']>20]
    use_col = use_col.iloc[:400]
    use_col = use_col['name'].tolist()+['SK_ID_CURR']+useless_col

    tr = pd.read_csv('./data/tr.csv')
    te = pd.read_csv('./data/te.csv')
    y = tr['TARGET'].astype(int)
    tr.drop(['TARGET'], axis=1,inplace=True)

    data = tr.append(te).reset_index(drop=True)
    drop_col = ['SK_ID_CURR']
    for col in tr.columns:
        if tr[col].dtype == 'object':
            drop_col.append(col)
            continue
        if col not in use_col:
            drop_col.append(col)
            continue

        num_na = tr[col].isnull().sum()
        if (num_na/tr.shape[0]) > thres:
            drop_col.append(col)
            continue


        num_na = te[col].isnull().sum()
        if (num_na / te.shape[0]) > thres:
            drop_col.append(col)
            continue

        mean = data[col].mean()
        std = data[col].std()

        tr[col] = (tr[col] - mean) / std
        te[col] = (te[col] - mean) / std

        tr[col] = tr[col].fillna(0)
        te[col] = te[col].fillna(0)

    tr.drop(drop_col + useless_col, axis=1, inplace=True)
    te.drop(drop_col + useless_col, axis=1, inplace=True)
    print(tr.shape)
    print(te.shape)
    return tr,te,y



def get_oof(tr,te,y,num_folds,model_name):
    if model_name == 'MultinomialNB':
        data = tr.append(te).reset_index(drop=True)
        for col in tr.columns:
            min_v = data[col].min()
            tr[col] = tr[col] - min_v
            te[col] = te[col] - min_v
        seed = 2017
    elif model_name == 'BernoulliNB':
        seed = 2019
    elif model_name == 'GaussianNB':
        seed = 2021
    elif model_name == 'lr':
        seed = 2018
    elif model_name == 'extra_tree_gini':
        seed = 2016
    elif model_name == 'extra_tree_entropy':
        seed = 20120
    elif model_name == 'dc_tree_entropy':
        seed = 2020
    elif model_name == 'dc_tree_gini':
        seed = 2015
    else:
        raise RuntimeError('model error')
    def get_model(model_name):
        if model_name == 'svm_rbf':
            return SVC(C=5.0,kernel='rbf',tol=1e-4,class_weight='balanced',verbose=1)
        elif model_name == 'lr':
            return LogisticRegression(n_jobs=-1, verbose=1, tol=1e-6, max_iter=200, C=5,
                                      solver='saga', class_weight='balanced')
        elif model_name == 'GaussianNB':
            prob_pos = np.sum(y)/len(y)
            priors = np.array([1-prob_pos,prob_pos])
            return GaussianNB(priors=priors)
        elif model_name == 'BernoulliNB':
            prob_pos = np.sum(y)/len(y)
            priors = np.array([1-prob_pos,prob_pos])
            return BernoulliNB(alpha=1.0,fit_prior=True,class_prior=priors)
        elif model_name == 'MultinomialNB':
            prob_pos = np.sum(y)/len(y)
            priors = np.array([1-prob_pos,prob_pos])
            return MultinomialNB(alpha=1000,fit_prior=True,class_prior=priors)
        elif model_name == 'extra_tree_gini':
            return ExtraTreeClassifier(criterion='gini',min_samples_leaf=70)
        elif model_name == 'extra_tree_entropy':
            return ExtraTreeClassifier(min_samples_leaf=70,criterion='entropy')
        elif model_name == 'dc_tree_entropy':
            return DecisionTreeClassifier('entropy',min_samples_leaf=70)
        elif model_name == 'dc_tree_entropy':
            return DecisionTreeClassifier('gini',min_samples_leaf=70)
        else:
            raise RuntimeError('model error')
    print(model_name)

    folds = StratifiedKFold(y,n_folds=num_folds,shuffle=True,random_state=seed)


    oof_preds = np.zeros(tr.shape[0])
    sub_preds = np.zeros(te.shape[0])
    for n_fold, (tr_idx, val_idx) in enumerate(folds):
        print('fold :',n_fold)

        tr_data = tr.iloc[tr_idx].values
        tr_y = y[tr_idx]

        val_data = tr.iloc[val_idx].values
        val_y = y[val_idx]

        model = get_model(model_name)
        model.fit(tr_data,tr_y)


        # val_pred = model.predict_proba(val_data)[:,1]
        # sub_preds += model.predict_proba(te.values)[:,1]
        val_pred = model.predict(val_data)
        sub_preds += model.predict(te.values)

        oof_preds[val_idx] = val_pred
        print(roc_auc_score(val_y,val_pred))
        print(log_loss(val_y,val_pred))


    sub_preds/=num_folds

    print('Full AUC score %.6f' % roc_auc_score(y, oof_preds))

    print("Output Model")

    Submission = pd.read_csv("./data/sample_submission.csv")
    Submission['TARGET'] = sub_preds.copy()
    Submission.to_csv("sample_submission.csv", index=False)

    print('save oof ')


    if os.path.exists("./data/oof_te.csv") and os.path.exists("./data/oof_tr.csv"):
        tr_oof = pd.read_csv("./data/oof_tr.csv")
        te_oof = pd.read_csv("./data/oof_te.csv")
    else:
        tr_oof = pd.read_csv("./data/tr.csv", usecols=['SK_ID_CURR'])
        te_oof = pd.read_csv("./data/te.csv", usecols=['SK_ID_CURR'])

    tr_oof[model_name+'_oof'] = oof_preds.copy()
    tr_oof.to_csv("./data/oof_tr.csv", index=False)

    te_oof[model_name+'_oof'] = sub_preds.copy()
    te_oof.to_csv("./data/oof_te.csv", index=False)


def get_data():
    from config import useless_col

    use_col = pd.read_csv('feat_importance.csv')
    use_col = use_col[use_col['importance1'] > 20]
    use_col = use_col.iloc[:50]
    use_col = use_col['name'].tolist() + useless_col

    tr = pd.read_csv('./data/tr.csv')
    te = pd.read_csv('./data/te.csv')
    y = tr['TARGET'].astype(int)
    tr.drop(['TARGET'], axis=1,inplace=True)

    data = tr.append(te).reset_index(drop=True)
    drop_col = ['SK_ID_CURR']
    for col in tr.columns:
        if col not in use_col:
            drop_col.append(col)
            continue

        if tr[col].dtype == 'object':
            drop_col.append(col)
            continue

        num_na = tr[col].isnull().sum()
        if num_na/len(tr) > 0.3:
            drop_col.append(col)
            continue

        num_na = te[col].isnull().sum()
        if num_na/len(te) > 0.3:
            drop_col.append(col)
            continue

        mean = data[col].mean()
        std = data[col].std()

        if (std>0)==False:
            drop_col.append(col)
            continue
        assert std>0

        tr[col] = (tr[col] - mean) / std
        te[col] = (te[col] - mean) / std
        tr[col] = tr[col].fillna(0)
        te[col] = te[col].fillna(0)


    tr.drop(drop_col + useless_col, axis=1, inplace=True)
    te.drop(drop_col + useless_col, axis=1, inplace=True)
    print(tr.shape)
    print(te.shape)
    return tr,te,y

def pca_feat(tr,te,kernel = 'linear',n_comp=16):
    from sklearn.decomposition import KernelPCA,PCA,TruncatedSVD

    data = tr.append(te).values

    print('begin fit')
    # model = KernelPCA(n_components=n_comp,kernel=kernel,n_jobs=-1)
    model = TruncatedSVD(16,algorithm='arpack',n_iter=10)

    data = model.fit_transform(data)
    tr_feat = data[:len(tr)]
    te_feat = data[len(tr):]

    if os.path.exists("./data/pca_te.csv") and os.path.exists("./data/pca_tr.csv"):
        tr_pca = pd.read_csv("./data/pca_tr.csv")
        te_pca = pd.read_csv("./data/pca_te.csv")
    else:
        tr_pca = pd.DataFrame()
        te_pca = pd.DataFrame()

    for i in range(n_comp):
        tr_pca[kernel + '_' + str(i)] = tr_feat[:, i]
        te_pca[kernel + '_' + str(i)] = te_feat[:, i]
    print('save')
    tr_pca.to_csv("./data/pca_tr.csv",index=False)
    te_pca.to_csv("./data/pca_te.csv",index=False)




def get_target_encode():
    tr = pd.read_csv('./data/tr.csv')
    te = pd.read_csv('./data/te.csv')

def target_encode():
    from category_encoders.target_encoder import TargetEncoder
    tr = pd.read_csv('./data/tr.csv')
    te = pd.read_csv('./data/te.csv')
    y = tr['TARGET'].astype(int)
    tr.drop(['TARGET'], axis=1, inplace=True)

    encode_model = TargetEncoder(verbose=1,min_samples_leaf=100)

    cate_col = []
    for col in tr.columns:
        if tr[col].dtype=='object':
            cate_col.append(col)

    encode_model.fit(tr,y)
    tr = encode_model.transform(tr)
    te = encode_model.transform(te)

    tr = tr[cate_col]
    te = te[cate_col]
    tr.columns = ['TE_'+col for col in cate_col]
    te.columns = ['TE_'+col for col in cate_col]
    print(tr.info())
    print(te.info())
    tr.to_csv("./data/target_tr.csv", index=False)
    te.to_csv("./data/target_te.csv", index=False)

if __name__=='__main__':
    # tr,te,y = get_oof_feat()
    # get_oof(tr,te,y,5,'MultinomialNB')
    # get_oof(tr,te,y, 5, 'BernoulliNB')
    # get_oof(tr, te, y, 5, 'lr')
    # get_oof(tr, te, y, 5, 'dc_tree_gini')
    # get_oof(tr, te, y, 5, 'GaussianNB')
    # tr,te,y = get_data()

    # pca_feat(tr,te,kernel='linear')
    target_encode()
