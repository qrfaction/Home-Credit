
from sklearn.linear_model import LinearRegression
import numpy as np
import multiprocessing as mp
from tqdm import tqdm
import pandas as pd



def trend_feature(feature_col,return_pred):
    y = feature_col.values
    try:
        x = np.arange(0, len(y)).reshape(-1, 1)
        lr = LinearRegression(n_jobs=2)
        lr.fit(x, y)
        if return_pred:
            return lr.coef_[0],lr.predict([[len(y)]])[0]
        else:
            return lr.coef_[0]
    except:
        if return_pred:
            return np.nan,np.nan
        else:
            return np.nan

def trend_feature_v2(df,feat,time_col,period,return_pred):

    try:
        if period is None:
            y = df[feat].values
            x = df[time_col].values.reshape(-1, 1)
        else:
            y = df[feat][-period:].values
            x = df[time_col][-period:].values.reshape(-1,1)
        lr = LinearRegression(n_jobs=2)
        lr.fit(x, y)
        if return_pred:
            return lr.coef_[0], lr.predict([[0]])[0]
        else:
            return lr.coef_[0]
    except:
        if return_pred:
            return np.nan, np.nan
        else:
            return np.nan


def agg_feature(df,feat,stat,period):
    if period is None:
        return df[feat].agg(stat)
    return df[feat][-period:].agg(stat)

def agg_worker(gr,feat,stat,period):

    try:
        name = feat + '_' + stat.upper()
    except:
        name = feat + '_' + stat.__name__.upper()
    if period is not None:
        name = name + '_' + str(period)

    if stat in ['last','first']:
        result = gr.agg({feat:stat})
        result.columns = [name]
    else:
        result = pd.DataFrame()
        result[name] = gr.apply(agg_feature,feat=feat,stat=stat,period=period)
    return result

def agg_batch_worker(gr,agg_para):
    return pd.concat([agg_worker(gr, para[0], para[1], para[2]) for para in tqdm(agg_para)],axis=1)

def trend_worker(gr,feat,period,time_col,return_pred):
    result = []
    if time_col == None:
        if period is None:
            for df in gr:
                result.append(trend_feature(df[feat],return_pred))
        else:
            for df in gr:
                result.append(trend_feature(df[feat][-period:],return_pred))
    else:
        for df in gr:
            result.append(trend_feature_v2(df,feat,time_col,period,return_pred))

    return result

def trend_parallel(gr,feat,stat,period,return_pred):


    def chunk_groups(groupby_object):
        num_cpu = mp.cpu_count()
        n_groups = gr.ngroups
        chunk_size = n_groups // (num_cpu * 2)

        group_chunk, index_chunk = [], []
        for i, (index, df) in enumerate(groupby_object):
            group_chunk.append(df)
            index_chunk.append(index)

            if (i + 1) % chunk_size == 0 or i + 1 == n_groups:
                group_chunk_, index_chunk_ = group_chunk.copy(), index_chunk.copy()
                group_chunk, index_chunk = [], []
                yield index_chunk_, group_chunk_

    try:
        name = feat + '_' + stat.upper()
    except:
        name = feat + '_' + stat.__name__.upper()
    if period is not None:
        name = name + '_' + str(period)

    if 'TREND_FEATURE_V2' in name:
        cols = dir(gr)
        if 'MONTHS_BALANCE' in cols:
            time_col = 'MONTHS_BALANCE'
        elif 'DAYS_DECISION' in cols:
            time_col = 'DAYS_DECISION'
        elif 'DAYS_INSTALMENT' in cols:
            time_col = 'DAYS_INSTALMENT'
        elif 'DAYS_CREDIT' in cols:
            time_col = 'DAYS_CREDIT'
        else:
            raise RuntimeError("time col error")
    else:
        time_col = None
    pool = mp.Pool(mp.cpu_count())

    indeces, features, results = [], [], []
    for index_chunk, groups_chunk in chunk_groups(gr):
        result = pool.apply_async(trend_worker, args=(groups_chunk,feat,period,time_col,return_pred))

        results.append(result)
        indeces.extend(index_chunk)

    if return_pred:
        for result in tqdm(results):
            features.append(pd.DataFrame(result.get()))
        features = pd.concat(features,axis=0)
    else:
        for result in tqdm(results):
            features += result.get()
        features = pd.DataFrame(features)
    features.index = indeces

    if return_pred:
        features.columns = [name,name+'_pred']
    else:
        features.columns = [name]

    pool.close()
    pool.join()

    return features

def agg_parallel(df,tasks,num_worker):

    def is_trend_feat(s):
        return isinstance(s,str)==False and "trend" in s.__name__

    trend_features = []
    gr = df.groupby("SK_ID_CURR")
    for feat,stats in tasks.items():
        for stat in stats:
            if isinstance(stat, list) or isinstance(stat, tuple):
                s = stat[0]
                if is_trend_feat(s):
                    for period in stat[1]:
                        result = trend_parallel(gr,feat,s,period,True)
                        trend_features.append(result)
            else:
                if is_trend_feat(stat):
                    result = trend_parallel(gr, feat, stat, None,True)
                    trend_features.append(result)


    feat_para = []
    for feat,stats in tasks.items():
        for stat in stats:
            if isinstance(stat, list) or isinstance(stat, tuple):
                s = stat[0]
                if is_trend_feat(s)==False:
                    for period in stat[1]:
                        feat_para.append((feat, s, period))
            else:
                if is_trend_feat(stat)==False:
                    feat_para.append((feat, stat,None))

    pool = mp.Pool(num_worker)
    num_task = int(np.ceil(len(feat_para)/num_worker))
    results = []
    for i in range(num_worker):
        use_feat = list(set([para[0] for para in feat_para[i*num_task:(i+1)*num_task]]))
        if len(use_feat) == 0:
            continue
        df_sub = df[use_feat + ['SK_ID_CURR']]
        gr = df_sub.groupby("SK_ID_CURR")

        result = pool.apply_async(agg_batch_worker,args=(gr,feat_para[i*num_task:(i+1)*num_task]))
        results.append(result)

    pool.close()
    pool.join()
    return pd.concat([r.get() for r in results] + trend_features, axis=1)


def diff_work(gr):
    return gr.diff().fillna(0)

def parallel_diff(df,gr,cols):

    pool = mp.Pool(mp.cpu_count()//2)
    results = []

    for col in cols:
        result = pool.apply_async(diff_work,args=(gr[col],))
        results.append(result)
    pool.close()
    pool.join()

    for result,col in zip(results,cols):
        df[col+'_DIFF'] = result.get()

    return df


def comb_feat(df,cols,mode,double_mode=True):
    from itertools import combinations
    feat = []
    for colx,coly in combinations(cols,2):
        if mode == '-':
            df[colx+'_subtr_'+coly] = df[colx] - df[coly]
            feat.append(colx+'_subtr_'+coly)
        elif mode == '+':
            df[colx+'_add_'+coly] = df[colx] + df[coly]
            feat.append(colx+'_add_'+coly)
        elif mode == '/':
            df[colx+'_divide_'+coly] = df[colx]/df[coly]
            feat.append(colx+'_divide_'+coly)
            if double_mode:
                df[coly +'_divide_' + colx] = df[coly] / df[colx]
                feat.append(coly+'_divide_'+colx)
        else:
            raise RuntimeError("mode error")
    return df,feat

def one_hot_encoder(df,useless_col=None):
    original_columns = list(df.columns)

    if useless_col is not None:
        categorical_columns = [col for col in df.columns if df[col].dtype == 'object' and col not in useless_col]
    else:
        categorical_columns = [col for col in df.columns if df[col].dtype == 'object']

    category_df = df[categorical_columns]
    df = pd.get_dummies(df, columns=categorical_columns, dummy_na=True)
    new_columns = [c for c in df.columns if c not in original_columns]

    for col in categorical_columns:
        df[col] = category_df[col]
    return df, new_columns

def agg_comb_feat(df,cols,mode,double_mode=True):
    stat = ['mean', 'min', 'max', 'sum','median',  'last', 'first']
    df,comb_cols = comb_feat(df,cols,mode,double_mode)
    agg_feat = {}
    for select in comb_cols:
        agg_feat[select] = stat
    return df,agg_feat

def get_bin_feature(df,cols,bins=8):
    agg_feat = {}
    for col in cols:
        original_columns = list(df.columns)
        df[col+'_bin'] = pd.qcut(df[col],bins,labels=False,duplicates='drop')
        df = pd.get_dummies(df, columns=[col+'_bin'], dummy_na=True)
        agg_feat.update({c:['mean','sum'] for c in df.columns if c not in original_columns})
    return df,agg_feat












