import pandas as pd
import numpy as np
import json
from tqdm import tqdm

def read_prepocess():

    # feat = pd.read_csv('feat.csv')
    # usecols = feat.loc[:200,'name'].tolist()
    # print(usecols)

    with open('./data/col_type.json', 'r') as f:
        col_type = json.loads(f.read())

    # tr = pd.read_csv('./data/tr.csv',dtype=col_type,usecols=usecols+['TARGET','SK_ID_CURR'])
    # te = pd.read_csv('./data/te.csv',dtype=col_type,usecols=usecols+['SK_ID_CURR'])
    tr = pd.read_csv('./data/tr.csv',dtype=col_type)
    te = pd.read_csv('./data/te.csv',dtype=col_type)

    tr.drop(['SK_ID_CURR','TARGET'],axis=1,inplace=True)
    te.drop(['SK_ID_CURR'],axis=1,inplace=True)




    y = np.ones(len(tr)+len(te))
    y[:len(tr)] = 0

    tr = pd.concat([tr,te]).reset_index(drop=True)

    from config import useless_col
    tr.drop(useless_col,axis=1,inplace=True)

    for col in tr.columns:
        if tr[col].dtype == 'object':
            tr[col] = tr[col].astype('category')

    print(tr.shape)
    return tr,y


def train(tr,y,num_folds):

    import lightgbm as gbm
    from sklearn.cross_validation import StratifiedKFold
    Dparam = {
        'objective': 'binary',
        'boosting_type': 'gbdt',
        'metric': 'auc',
        'nthread': 30,
        'shrinkage_rate': 0.02,
        # 'max_depth':9,
        # 'min_child_weight': 70,
        # 'feature_fraction': 0.05,
        # 'lambda_l2': 100,
        # 'num_leaves': 30,
        # 'min_split_gain':0.05,
        # 'max_depth' : 15,
        'device':'gpu',
    }

    print("Training model...\n")

    folds = StratifiedKFold(y,n_folds=num_folds,shuffle=False)


    for n_fold, (trn_idx, val_idx) in enumerate(folds):
        print('fold :',n_fold)
        dtrain = gbm.Dataset(tr.iloc[trn_idx], y[trn_idx])
        dval = gbm.Dataset(tr.iloc[val_idx], y[val_idx])
        m_gbm = gbm.train(params=Dparam, train_set=dtrain, num_boost_round=200, verbose_eval=50,
                          valid_sets=[dtrain,dval], valid_names=['train','valid'],early_stopping_rounds=100)


        feature_score = pd.DataFrame()
        feature_score['name'] = m_gbm.feature_name()
        feature_score['importance1'] = m_gbm.feature_importance()
        feature_score['importance2'] = m_gbm.feature_importance('gain')
        feature_score['importance3'] = feature_score['importance2']/(feature_score['importance1']**0.5)
        feature_score.dropna(inplace=True)
        feature_score = feature_score.sort_values(by=['importance3','importance2','importance1'],ascending=False)
        print(feature_score)
        feature_score.to_csv('./log/leak_feat'+str(n_fold)+'.csv',index=False)




def main():

    tr,y = read_prepocess()

    train(tr,y,5)

if __name__ == '__main__':
    main()





