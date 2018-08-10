import pandas as pd
import numpy as np
import json
import os
from imblearn.over_sampling import SMOTE

def read_prepocess():

    # feat = pd.read_csv('feat.csv')
    # usecols = feat.loc[:200,'name'].tolist()
    # print(usecols)

    # with open('./data/col_type.json', 'r') as f:
    #     col_type_ = json.loads(f.read())

    # tr = pd.read_csv('./data/tr.csv',dtype=col_type,usecols=usecols+['TARGET','SK_ID_CURR'])
    # te = pd.read_csv('./data/te.csv',dtype=col_type,usecols=usecols+['SK_ID_CURR'])
    # col_type = {}
    # for col in col_type_.keys():
    #     if col_type_[col] == 'category':
    #         col_type[col] = col_type_[col]
    tr = pd.read_csv('./data/tr.csv')
    te = pd.read_csv('./data/te.csv')
    for col in tr.columns:
        if tr[col].dtype == 'object':
            tr[col] = tr[col].astype('category')
            te[col] = te[col].astype('category')


    te_usecols = [
        'TE_NAME_INCOME_TYPE',
        'TE_PREV_PRODUCT_COMBINATION_LAST',
        'TE_NAME_FAMILY_STATUS',
        # 'TE_NAME_CONTRACT_TYPE',
        # 'TE_PREV_NAME_YIELD_GROUP_LAST',
        # 'TE_PREV_CODE_REJECT_REASON_LAST',
        # "TE_WEEKDAY_APPR_PROCESS_START",
        ]
    target_tr = pd.read_csv("./data/target_tr.csv",usecols=te_usecols)
    target_te = pd.read_csv("./data/target_te.csv",usecols=te_usecols)
    # oof_tr = pd.read_csv("./data/oof_tr.csv")
    # oof_te = pd.read_csv("./data/oof_te.csv")
    drop_col = [
        'SK_ID_CURR',
        # 'extra_tree_entropy_oof',
        # 'extra_tree_gini_oof',
        # 'MultinomialNB_oof',
        # 'lr_oof',
        'lgb_oof',
        # 'GaussianNB_oof',
        # 'BernoulliNB_oof',
    ]
    # oof_tr.drop(drop_col,axis=1,inplace=True)
    # oof_te.drop(drop_col, axis=1, inplace=True)
    tr = pd.concat([tr,target_tr],axis=1)
    te = pd.concat([te,target_te],axis=1)



    y = tr['TARGET'].astype(int)
    from config import useless_col
    tr.drop(['SK_ID_CURR','TARGET']+useless_col,axis=1,inplace=True)
    te.drop(['SK_ID_CURR',]+useless_col,axis=1,inplace=True)

    score_feat = pd.read_csv("feat_score.csv")
    score_feat = score_feat.sort_values(by=['importance2'],ascending=False)
    usecols = score_feat['name'].tolist()[:550]
    tr.columns = [col.replace(' ','_') for col in tr.columns]
    te.columns = [col.replace(' ','_') for col in te.columns]
    usecols += te_usecols
    usecols = list(set(usecols))
    tr = tr[usecols]
    te = te[usecols]
    print(tr.info())
    print(te.info())
    return tr,te,y


def train(tr,te,y,num_folds,over_sample=False):

    import lightgbm as gbm
    from sklearn.metrics import roc_auc_score
    from sklearn.cross_validation import StratifiedKFold,KFold

    Dparam = {
        'objective': 'binary',
        'boosting_type': 'gbdt',
        'metric': 'auc',
        'nthread': 32,
        'shrinkage_rate': 0.015,
        'min_child_samples': 70,
        'feature_fraction': 0.05,
        'lambda_l2': 50,
        'min_child_weight':40,
        'num_leaves': 24,
        'min_split_gain':1,

        # 'bagging_fraction':0.8,
        # 'bagging_freq':2,
        'max_depth' : -1,
        'device':'gpu',
        'scale_pos_weight':2,
    }

    print("Training model...\n")

    # folds = StratifiedKFold(y,n_folds=num_folds,shuffle=False)
    folds = KFold(len(y),5,shuffle=True,random_state=47)
    # y = (y-0.5)*2
    def lr_decay(current_round,base_lr=Dparam['shrinkage_rate']):
        return base_lr-(current_round%500/500)*base_lr*2/3

    def col_sample(current_round,base_fs=Dparam['feature_fraction']):
        print(base_fs*(1+current_round/750))
        return base_fs*(1+current_round/750)

    oof_preds = np.zeros(tr.shape[0])
    sub_preds = np.zeros(te.shape[0])


    for n_fold, (trn_idx, val_idx) in enumerate(folds):

        tr_x,tr_y = tr.iloc[trn_idx], y.iloc[trn_idx]
        print('fold :',n_fold)

        if over_sample:
            print(tr_x.shape, tr_y.shape)
            sm = SMOTE(ratio={0 : len(y)-np.sum(y), 1 : 2*np.sum(y)},n_jobs=-1)

            tr_x,tr_y= sm.fit_sample(tr_x,tr_y)
            tr_x = pd.DataFrame(tr_x,columns=tr.columns)
            print(tr_x.shape,tr_y.shape)

        dtrain = gbm.Dataset(tr_x, tr_y)
        dval = gbm.Dataset(tr.iloc[val_idx], y.iloc[val_idx])
        m_gbm = gbm.train(params=Dparam, train_set=dtrain, num_boost_round=20000, verbose_eval=50,
                          valid_sets=[dtrain,dval], valid_names=['train','valid'],
                          early_stopping_rounds=300,
                          # callbacks=[gbm.reset_parameter(shrinkage_rate=lr_decay)]
                          )

        if n_fold==0:
            feature_score = pd.DataFrame()
            feature_score['name'] = m_gbm.feature_name()
            feature_score['importance1'] = m_gbm.feature_importance()
            feature_score['importance2'] = m_gbm.feature_importance('gain')
            # feature_score['importance3'] = feature_score['importance2']/(feature_score['importance1']**0.5)
            feature_score.dropna(inplace=True)
            feature_score = feature_score.sort_values(by=['importance2','importance1'],ascending=False)
            print(feature_score)
            feature_score.to_csv('feat_importance.csv',index=False)


        oof_preds[val_idx] = m_gbm.predict(tr.iloc[val_idx])

        test_pred = m_gbm.predict(te, num_iteration=m_gbm.best_iteration)
        test_pred /= 5
        sub_preds += test_pred

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

    # tr_oof['lgb_oof'] = oof_preds.copy()
    # tr_oof.to_csv("./data/oof_tr.csv", index=False)
    #
    # te_oof['lgb_oof'] = sub_preds.copy()
    # te_oof.to_csv("./data/oof_te.csv", index=False)

def main():

    tr,te,y = read_prepocess()

    train(tr,te,y,5)

if __name__ == '__main__':
    main()









