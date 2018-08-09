import pandas as pd
import numpy as np
import json
import gc
from util import *
from tqdm import tqdm
import time
from contextlib import contextmanager
import multiprocessing as mp
import warnings
warnings.filterwarnings('ignore')

@contextmanager
def timer(title):
    t0 = time.time()
    yield
    print("{} - done in {:.0f}s".format(title, time.time() - t0))

stat = ['mean', 'min', 'max', 'sum', 'median', 'last', 'first','var']

def set_dtype(df):
    with open('./data/col_type.json', 'r') as f:
        col_type = json.loads(f.read())
    for col in df.columns:
        df[col] = df[col].astype(col_type[col])
    return df

def co_prob(dataset,cols,feature_name,normilize=False,return_col=False):
    """
    create  feature  :  P(x1,x2,x3,...)
    :param cols:          list  cols   or str
    :param dataset:    pandas Dataframe
    """
    if isinstance(cols,str) :
        cols = [cols]
    X = dataset[cols]
    X[feature_name] = range(len(dataset))
    X = X.groupby(by=cols, as_index=False).count()
    if normilize:
        X[feature_name] = X[feature_name]/len(dataset)
    dataset = dataset.merge(right=X,how='left',on=cols)
    if return_col:
        return dataset[feature_name]
    return dataset

def condition_prob(dataset,Y,X,feature_name,return_col=False):
    """
    create  feature  :  P(y1,y2,y3...|x1,x2,x3...)
    :param Y:           list cols  or  str col
    :param X:           list cols  or  str col
    :param dataset:     pandas Dataframe
    """
    if isinstance(Y,str):
        Y = [Y]
    if isinstance(Y,str):
        X = [X]
    XY = X + Y
    prob_x = co_prob(dataset,X,'prob_x',return_col=True)
    prob_xy = co_prob(dataset,XY,'prob_xy', return_col=True)
    dataset[feature_name] = prob_xy/prob_x

    if return_col:
        return dataset[feature_name]
    return dataset

def condition_stat(dataset,target_col,cols,feature_name,stat_f,return_col=False):

    if isinstance(cols,str) :
        cols = [cols]
    cols = list(cols)
    X = dataset[[target_col]+cols]


    X = X.groupby(by=cols, as_index=False).aggregate({target_col:stat_f})
    # X = pd.DataFrame()
    X = X.rename(columns={target_col:feature_name})

    dataset = dataset.merge(right=X,how='left',on=cols)
    if return_col:
        return dataset[feature_name]
    return dataset

def set_dtypes():
    train = pd.read_csv('./data/application_train.csv')
    test = pd.read_csv('./data/application_test.csv')
    prev = pd.read_csv('./data/previous_application.csv')
    pos_cash = pd.read_csv('./data/POS_CASH_balance.csv')
    buro = pd.read_csv('./data/bureau.csv')
    burobl = pd.read_csv('./data/bureau_balance.csv')
    credit = pd.read_csv('./data/credit_card_balance.csv')
    installment = pd.read_csv('./data/installments_payments.csv')

    files = [train, test, prev, pos_cash, buro, burobl, credit, installment]

    col_type = {}
    category_col = [
        "SK_ID_PREV",
        "SK_ID_CURR",
        "SELLERPLACE_AREA",    # 2097个
        "SK_ID_BUREAU",
        "HOUR_APPR_PROCESS_START",# 用户在哪个小时申请的贷款
    ]
    for table in files:
        cols = table.columns
        num_unique = table.nunique()
        types = table.dtypes
        for i, j, k in zip(cols, num_unique, types):

            if k == np.object  or i in category_col:
                col_type[i] = 'category'
            else:
                col_type[i] = 'float'

    col_type['TARGET'] = 'int'
    with open('./data/col_type.json','w') as f:
        f.write(json.dumps(col_type))



# One-hot encoding for categorical columns with get_dummies

# Preprocess application_train.csv and application_test.csv
def application_train_test(num_rows=None):
    # Read data and merge
    df = pd.read_csv('./data/application_train.csv', nrows=num_rows)
    test_df = pd.read_csv('./data/application_test.csv', nrows=num_rows)
    print("Train samples: {}, test samples: {}".format(len(df), len(test_df)))
    df = df.append(test_df).reset_index(drop=True)
    # Optional: Remove 4 applications with XNA CODE_GENDER (train set)
    df = df[df['CODE_GENDER'] != 'XNA']

    docs = [_f for _f in df.columns if 'FLAG_DOC' in _f]
    live = [_f for _f in df.columns if ('FLAG_' in _f) & ('FLAG_DOC' not in _f) & ('_FLAG_' not in _f)]

    df['DAYS_EMPLOYED'].replace(365243, np.nan, inplace=True)


    df['nan_count'] = df.isna().sum(axis = 1)

    df['NEW_DOC_IND_KURT'] = df[docs].kurtosis(axis=1)
    df['NEW_DOC_IND_SUM'] = df[docs].kurtosis(axis=1)


    df['NEW_SOURCES_PROD'] = df['EXT_SOURCE_1'] * df['EXT_SOURCE_2'] * df['EXT_SOURCE_3']
    df['NEW_EXT_SOURCES_MEAN'] = df[['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3']].mean(axis=1)
    df['NEW_SCORES_STD'] = df[['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3']].std(axis=1)
    df['NEW_SCORES_STD'] = df['NEW_SCORES_STD'].fillna(df['NEW_SCORES_STD'].mean())

    df['annuity_income_percentage'] = df['AMT_ANNUITY'] / df['AMT_INCOME_TOTAL']
    df['car_to_birth_ratio'] = df['OWN_CAR_AGE'] / df['DAYS_BIRTH']
    df['car_to_employ_ratio'] = df['OWN_CAR_AGE'] / df['DAYS_EMPLOYED']

    df['credit_to_annuity_ratio'] = df['AMT_CREDIT'] / df['AMT_ANNUITY']
    df['payment_rate'] = df['AMT_ANNUITY'] / df['AMT_CREDIT']
    df['credit_to_income_ratio'] = df['AMT_CREDIT'] / df['AMT_INCOME_TOTAL']
    df['income_credit_percentage'] = df['AMT_INCOME_TOTAL'] / df['AMT_CREDIT']

    df['credit_to_goods_ratio'] = df['AMT_CREDIT'] / df['AMT_GOODS_PRICE']
    df['days_employed_percentage'] = df['DAYS_EMPLOYED'] / df['DAYS_BIRTH']
    df['phone_to_birth_ratio'] = df['DAYS_LAST_PHONE_CHANGE'] / df['DAYS_BIRTH']
    df['phone_to_employ_ratio'] = df['DAYS_LAST_PHONE_CHANGE'] / df['DAYS_EMPLOYED']
    df['cnt_non_child'] = df['CNT_FAM_MEMBERS'] - df['CNT_CHILDREN']
    df['credit_per_person'] = df['AMT_CREDIT'] / df['CNT_FAM_MEMBERS']
    df['credit_per_child'] = df['AMT_CREDIT'] / (1 + df['CNT_CHILDREN'])
    df['credit_per_non_child'] = df['AMT_CREDIT'] / df['cnt_non_child']

    # Categorical features with Binary encode (0 or 1; two categories)
    for bin_feature in ['CODE_GENDER', 'FLAG_OWN_CAR', 'FLAG_OWN_REALTY']:
        df[bin_feature], uniques = pd.factorize(df[bin_feature])
    # Categorical features with One-Hot encode

    dropcolum = ['FLAG_DOCUMENT_2', 'FLAG_DOCUMENT_4',
                 'FLAG_DOCUMENT_5', 'FLAG_DOCUMENT_6', 'FLAG_DOCUMENT_7',
                 'FLAG_DOCUMENT_8', 'FLAG_DOCUMENT_9', 'FLAG_DOCUMENT_10',
                 'FLAG_DOCUMENT_11', 'FLAG_DOCUMENT_12', 'FLAG_DOCUMENT_13',
                 'FLAG_DOCUMENT_14', 'FLAG_DOCUMENT_15', 'FLAG_DOCUMENT_16',
                 'FLAG_DOCUMENT_17', 'FLAG_DOCUMENT_18', 'FLAG_DOCUMENT_19',
                 'FLAG_DOCUMENT_20', 'FLAG_DOCUMENT_21']
    df = df.drop(dropcolum, axis=1)
    # for col in df.columns:
    #     if df[col].dtype == 'object':
    #         df[col] = df[col].astype('category')


    condi_stat_feat = [
        (["CODE_GENDER",
          "ORGANIZATION_TYPE",
          "NAME_EDUCATION_TYPE"], [("AMT_ANNUITY", "median"),
                                 ("DAYS_REGISTRATION", "median"),
                                 ("credit_to_annuity_ratio", "median"),
                                 ("credit_to_goods_ratio", "median"),
                                 ("car_to_employ_ratio", "median"),
                                 ("phone_to_birth_ratio", "median"),
                                 ("days_employed_percentage", "median"),
                                 ("phone_to_employ_ratio", "median")]),

        (["NAME_EDUCATION_TYPE",
          "OCCUPATION_TYPE",
          "REG_CITY_NOT_WORK_CITY"], [
                                      ("credit_to_goods_ratio", "median"),
                                      ("car_to_employ_ratio", "median"),
                                      ("phone_to_birth_ratio", "median"),
                                      ("annuity_income_percentage", "median"),
                                      ("days_employed_percentage", "median"),
                                      ("phone_to_employ_ratio", "median")]),
    ]

    for groupby_cols, specs in condi_stat_feat:
        group_object = df.groupby(groupby_cols)
        for select, agg in specs:
            groupby_aggregate_name = "{}_{}_{}_{}".format("NEW", "_".join(groupby_cols), agg, select)
            df = df.merge(
                group_object[select]
                    .agg(agg)
                    .reset_index()
                    .rename(index=str, columns={select: groupby_aggregate_name}),
                left_on=groupby_cols,
                right_on=groupby_cols,
                how="left"
            )

    # df = pd.get_dummies(df, columns=['NAME_EDUCATION_TYPE'], dummy_na=True)
    # df = pd.get_dummies(df, columns=['ORGANIZATION_TYPE'], dummy_na=True)
    # df = pd.get_dummies(df, columns=['OCCUPATION_TYPE'], dummy_na=True)
    print(df.shape)
    return df


# Preprocess bureau.csv and bureau_balance.csv
def bureau_and_balance(num_rows=None):

    bureau = pd.read_csv('./data/bureau.csv', nrows=num_rows)

    bureau.drop(['CREDIT_CURRENCY'],axis=1,inplace=True)


    bureau['DAYS_CREDIT_ENDDATE'][bureau['DAYS_CREDIT_ENDDATE'] < -40000] = np.nan
    bureau['DAYS_CREDIT_UPDATE'][bureau['DAYS_CREDIT_UPDATE'] < -40000] = np.nan
    bureau['DAYS_ENDDATE_FACT'][bureau['DAYS_ENDDATE_FACT'] < -40000] = np.nan


    usecol = ['Microloan','Mortgage','Consumer_credit','Credit_card','Car_loan']
    bureau['CREDIT_TYPE'] = bureau['CREDIT_TYPE'].apply(lambda x:'other' if x not in usecol else x)
    bureau, bureau_cat = one_hot_encoder(bureau)

    bureau['nan_count'] = bureau.isna().sum(axis=1)

    bureau["AMT_CREDIT_SUM_DEBT_divide_AMT_CREDIT_SUM"] = bureau["AMT_CREDIT_SUM_DEBT"] / bureau["AMT_CREDIT_SUM"]
    bureau["AMT_CREDIT_MAX_OVERDUE_divide_AMT_CREDIT_SUM_LIMIT"] = bureau["AMT_CREDIT_MAX_OVERDUE"] / bureau["AMT_CREDIT_SUM_LIMIT"]
    bureau["CNT_CREDIT_PROLONG_divide_AMT_CREDIT_MAX_OVERDUE"] = bureau["CNT_CREDIT_PROLONG"] / bureau[ "AMT_CREDIT_MAX_OVERDUE"]
    bureau["AMT_CREDIT_SUM_DEBT_divide_AMT_CREDIT_MAX_OVERDUE"] = bureau["AMT_CREDIT_SUM_DEBT"] / bureau["AMT_CREDIT_MAX_OVERDUE"]
    bureau["AMT_CREDIT_MAX_OVERDUE_divide_AMT_CREDIT_SUM_LIMIT"] = bureau["AMT_CREDIT_MAX_OVERDUE"] / bureau["AMT_CREDIT_SUM_LIMIT"]
    bureau["AMT_CREDIT_SUM_divide_AMT_CREDIT_MAX_OVERDUE"] = bureau["AMT_CREDIT_SUM"] / bureau["AMT_CREDIT_MAX_OVERDUE"]
    bureau["AMT_CREDIT_MAX_OVERDUE_divide_AMT_CREDIT_SUM"] = bureau["AMT_CREDIT_MAX_OVERDUE"] / bureau["AMT_CREDIT_SUM"]

    bureau["DAYS_CREDIT_subtr_CREDIT_DAY_OVERDUE"] = bureau["DAYS_CREDIT"] - bureau["CREDIT_DAY_OVERDUE"]
    bureau["DAYS_CREDIT_ENDDATE_subtr_DAYS_CREDIT_UPDATE"] = bureau["DAYS_CREDIT_ENDDATE"] - bureau["DAYS_CREDIT_UPDATE"]
    bureau["CREDIT_DAY_OVERDUE_subtr_DAYS_CREDIT_ENDDATE"] = bureau["CREDIT_DAY_OVERDUE"] - bureau["DAYS_CREDIT_ENDDATE"]
    bureau["CREDIT_DAY_OVERDUE_subtr_DAYS_CREDIT_UPDATE"] = bureau["CREDIT_DAY_OVERDUE"] - bureau["DAYS_CREDIT_UPDATE"]
    bureau["DAYS_CREDIT_subtr_DAYS_CREDIT_ENDDATE"] = bureau["DAYS_CREDIT"] - bureau["DAYS_CREDIT_ENDDATE"]
    bureau["DAYS_CREDIT_subtr_DAYS_CREDIT_UPDATE"] = bureau["DAYS_CREDIT"] - bureau["DAYS_CREDIT_UPDATE"]

    bureau["AMT_CREDIT_MAX_OVERDUE_add_AMT_CREDIT_SUM_DEBT"] = bureau["AMT_CREDIT_MAX_OVERDUE"] + bureau["AMT_CREDIT_SUM_DEBT"]


    # Bureau balance: Perform aggregations and merge with bureau.csv
    stat = ['min','max','sum','median','mean','first','last','var','size']
    bb = pd.read_csv('./data/bureau_balance.csv')
    bb, bb_cat = one_hot_encoder(bb)
    bb.sort_values(['SK_ID_BUREAU','MONTHS_BALANCE'],ascending=True,inplace=True)
    bb_aggregations = {'MONTHS_BALANCE': stat}
    for col in bb_cat:
        bb_aggregations[col] = ['mean']
    bb_agg = bb.groupby('SK_ID_BUREAU').agg(bb_aggregations)
    bb_agg.columns = pd.Index([e[0] + "_" + e[1].upper() for e in bb_agg.columns.tolist()])
    bureau = bureau.join(bb_agg, how='left', on='SK_ID_BUREAU')


    bureau.sort_values(['SK_ID_CURR','DAYS_CREDIT'], ascending=True, inplace=True)
    gr = bureau.groupby(by=['SK_ID_CURR'])

    cols = [
        'DAYS_CREDIT',
        'DAYS_CREDIT_ENDDATE',
        'DAYS_CREDIT_UPDATE',
        'DAYS_ENDDATE_FACT',
        'AMT_CREDIT_MAX_OVERDUE',
        'AMT_CREDIT_SUM',
        'AMT_CREDIT_SUM_DEBT',
        'AMT_CREDIT_SUM_LIMIT',
    ]
    bureau = parallel_diff(bureau, gr, cols)

    bin_cols = [
        'DAYS_CREDIT',
        'DAYS_ENDDATE_FACT',
    ]
    bureau,bin_cols = get_bin_feature(bureau,bin_cols)


    bureau.drop(['SK_ID_BUREAU'], axis=1, inplace=True)
    aggregations = {
        'DAYS_CREDIT': ['var','median','max','min'],   # last ,first <=> min max
        'DAYS_CREDIT_UPDATE': ['mean', 'median'],
        'DAYS_ENDDATE_FACT':['max','last','median'],
        'DAYS_CREDIT_ENDDATE': ['sum','median',trend_feature,'last'],
        'AMT_CREDIT_MAX_OVERDUE':['sum','max','median','mean'],
        'AMT_CREDIT_SUM':['max','sum','first','last','mean'],
        'AMT_CREDIT_SUM_DEBT':['max','sum','last'],
        'AMT_CREDIT_SUM_OVERDUE':['sum'],
        'AMT_CREDIT_SUM_LIMIT':['var'],

        'AMT_ANNUITY': ['max', 'mean'],


        'DAYS_CREDIT_DIFF':['var','max','mean'],
        "DAYS_CREDIT_ENDDATE_DIFF": ['max'],
        'DAYS_CREDIT_UPDATE_DIFF':['skew','last'],
        "DAYS_ENDDATE_FACT_DIFF":['mean'],
        "AMT_CREDIT_SUM_DIFF":['sum','var','max'],
        "AMT_CREDIT_SUM_DEBT_DIFF":['var','last'],


        'AMT_CREDIT_SUM_DEBT_divide_AMT_CREDIT_SUM':['max','mean','sum','last'],   # median
        'AMT_CREDIT_MAX_OVERDUE_divide_AMT_CREDIT_SUM_LIMIT':['max'],
        'AMT_CREDIT_MAX_OVERDUE_divide_AMT_CREDIT_SUM':['mean'],


        "DAYS_CREDIT_subtr_CREDIT_DAY_OVERDUE":['median','last','max',trend_feature,'min'],
        "DAYS_CREDIT_ENDDATE_subtr_DAYS_CREDIT_UPDATE":['median','last',trend_feature_v2],
        "CREDIT_DAY_OVERDUE_subtr_DAYS_CREDIT_ENDDATE":['median','min'],
        "CREDIT_DAY_OVERDUE_subtr_DAYS_CREDIT_UPDATE":['median'],
        "DAYS_CREDIT_subtr_DAYS_CREDIT_ENDDATE":['last'],

        "AMT_CREDIT_MAX_OVERDUE_add_AMT_CREDIT_SUM_DEBT":['max','sum','mean'],

        "DAYS_CREDIT_bin_7.0":['sum'],
        "DAYS_ENDDATE_FACT_bin_nan":['mean'],

        "STATUS_0_MEAN":['var','mean'],
        "STATUS_C_MEAN":['max','var'],
        "STATUS_X_MEAN":['var'],

        'MONTHS_BALANCE_LAST':['var'],
        'MONTHS_BALANCE_MEDIAN': ['skew'],
        'MONTHS_BALANCE_VAR': ['mean'],
        'MONTHS_BALANCE_SIZE': ['sum'],

    }
    for cat in bureau_cat: aggregations[cat] = ['mean']

    bureau_agg = agg_parallel(bureau,aggregations,mp.cpu_count())
    bureau_agg.columns = pd.Index(['BURO_' + e for e in bureau_agg.columns])


    ###  ----------------------------------active ---------------------------------------------------

    aggregations = {
        'DAYS_CREDIT': ['mean','max'],   # last ,first <=> min max
        'AMT_CREDIT_SUM':['min','sum','first'],
        "AMT_CREDIT_SUM_DIFF":['max'],

        'AMT_CREDIT_SUM_DEBT_divide_AMT_CREDIT_SUM':['max','last','median'],
        'AMT_CREDIT_MAX_OVERDUE_divide_AMT_CREDIT_SUM_LIMIT':['median'],

        "DAYS_CREDIT_subtr_CREDIT_DAY_OVERDUE":['last'],
        # "CREDIT_DAY_OVERDUE_subtr_DAYS_CREDIT_ENDDATE":['last'],
        "DAYS_CREDIT_subtr_DAYS_CREDIT_ENDDATE":['max'],

        "AMT_CREDIT_MAX_OVERDUE_add_AMT_CREDIT_SUM_DEBT":['max'],

        "DAYS_CREDIT_bin_7.0":['sum'],

        "MONTHS_BALANCE_VAR":['skew'],

        'AMT_ANNUITY': ['max', 'mean'],

    }

    active = bureau[bureau['CREDIT_ACTIVE_Active'] == 1]
    active_agg = agg_parallel(active, aggregations, mp.cpu_count())
    active_agg.columns = pd.Index(['ACTIVE_' + e for e in active_agg.columns])
    bureau_agg = bureau_agg.join(active_agg, how='left', on='SK_ID_CURR')

    ###  ----------------------------------closed ---------------------------------------------------

    aggregations = {
        'DAYS_CREDIT': ['min'],   # last ,first <=> min max
        'AMT_CREDIT_SUM':['median','sum','first'],
        'DAYS_CREDIT_DIFF':['sum','mean','last'],
        "DAYS_CREDIT_subtr_CREDIT_DAY_OVERDUE":['first'],
        # "DAYS_CREDIT_subtr_DAYS_CREDIT_ENDDATE":['max'],

        "MONTHS_BALANCE_LAST":['sum'],
        "MONTHS_BALANCE_MEAN": ['sum'],

        'AMT_ANNUITY': ['max', 'mean'],
    }

    closed = bureau[bureau['CREDIT_ACTIVE_Closed'] == 1]
    closed_agg = agg_parallel(closed, aggregations, mp.cpu_count())
    closed_agg.columns = pd.Index(['CLOSED_' + e for e in closed_agg.columns])
    bureau_agg = bureau_agg.join(closed_agg, how='left', on='SK_ID_CURR')


    ###  period  feature
    aggregations = {
        'DAYS_CREDIT_ENDDATE': ['max',trend_feature_v2],
        'DAYS_CREDIT_DIFF': ['mean'],
        'AMT_CREDIT_MAX_OVERDUE': ['sum', 'max', 'mean'],
        'AMT_CREDIT_SUM_DEBT_divide_AMT_CREDIT_SUM':['max','sum','median',trend_feature_v2], # 'mean
        'nan_count': ['sum','max','var','mean'],
        "AMT_CREDIT_MAX_OVERDUE_add_AMT_CREDIT_SUM_DEBT":['last'],
    }
    bure_period_1 = bureau[bureau['DAYS_CREDIT']>=-760]
    bureau_agg_period1 = agg_parallel(bure_period_1,aggregations, mp.cpu_count())
    bureau_agg_period1.columns = pd.Index(['BURO_PERIOD_' + e for e in bureau_agg_period1.columns])

    bureau_agg = bureau_agg.join(bureau_agg_period1,how='left', on='SK_ID_CURR')

    for prefix in ['BURO_']:

        bureau_agg[prefix+'debt_credit_ratio'] = \
            bureau_agg[prefix+'AMT_CREDIT_SUM_DEBT_SUM'] / bureau_agg[prefix+'AMT_CREDIT_SUM_SUM']

        bureau_agg[prefix + 'credit_active_ratio'] = \
            bureau_agg[prefix + 'CREDIT_ACTIVE_Active_MEAN'] / bureau_agg[prefix + 'CREDIT_ACTIVE_Closed_MEAN']


    useless_col = [
        'BURO_CREDIT_ACTIVE_Bad debt_MEAN',
        'BURO_CREDIT_ACTIVE_nan_MEAN',
        'BURO_CREDIT_TYPE_nan_MEAN',
        'BURO_CREDIT_ACTIVE_Sold_MEAN',
    ]
    bureau_agg.drop(useless_col,axis=1,inplace=True)

    return bureau_agg


def previous_applications(num_rows=None):
    prev = pd.read_csv('./data/previous_application.csv', nrows=num_rows)


    # Days 365.243 values -> nan
    prev['DAYS_FIRST_DRAWING'].replace(365243, np.nan, inplace=True)
    prev['DAYS_FIRST_DUE'].replace(365243, np.nan, inplace=True)
    prev['DAYS_LAST_DUE_1ST_VERSION'].replace(365243, np.nan, inplace=True)
    prev['DAYS_LAST_DUE'].replace(365243, np.nan, inplace=True)
    prev['DAYS_TERMINATION'].replace(365243, np.nan, inplace=True)


    prev['nan_count'] = prev.isna().sum(axis=1)
    prev["AMT_CREDIT_divide_AMT_GOODS_PRICE"] = prev["AMT_CREDIT"] / prev["AMT_GOODS_PRICE"]
    prev["AMT_GOODS_PRICE_divide_AMT_CREDIT"] = prev["AMT_GOODS_PRICE"] / prev["AMT_CREDIT"]
    prev["AMT_DOWN_PAYMENT_divide_AMT_CREDIT"] = prev["AMT_DOWN_PAYMENT"] / prev["AMT_CREDIT"]
    prev["AMT_DOWN_PAYMENT_divide_CNT_PAYMENT"] = prev["AMT_DOWN_PAYMENT"] / prev["CNT_PAYMENT"]
    prev["CNT_PAYMENT_divide_AMT_ANNUITY"] = prev["CNT_PAYMENT"] / prev["AMT_ANNUITY"]
    prev["AMT_ANNUITY_divide_CNT_PAYMENT"] = prev["AMT_ANNUITY"] / prev["CNT_PAYMENT"]
    prev["CNT_PAYMENT_divide_AMT_GOODS_PRICE"] = prev["CNT_PAYMENT"] / prev["AMT_GOODS_PRICE"]
    prev["AMT_CREDIT_divide_AMT_ANNUITY"] = prev["AMT_CREDIT"] / prev["AMT_ANNUITY"]
    prev["AMT_CREDIT_divide_CNT_PAYMENT"] = prev["AMT_CREDIT"] / prev["CNT_PAYMENT"]
    prev['AMT_CREDIT_divide_AMT_APPLICATION'] = prev['AMT_CREDIT'] / prev['AMT_APPLICATION']
    prev['AMT_APPLICATION_divide_AMT_CREDIT'] = prev['AMT_APPLICATION'] / prev['AMT_CREDIT']
    prev['AMT_APPLICATION_divide_CNT_PAYMENT'] = prev['AMT_APPLICATION'] / prev['CNT_PAYMENT']
    prev['CNT_PAYMENT_divide_AMT_APPLICATION'] = prev['CNT_PAYMENT'] / prev['AMT_APPLICATION']
    prev["AMT_GOODS_PRICE_divide_CNT_PAYMENT"] = prev["AMT_GOODS_PRICE"] / prev["CNT_PAYMENT"]

    prev["DAYS_LAST_DUE_1ST_VERSION_subtr_DAYS_TERMINATION"] = prev["DAYS_LAST_DUE_1ST_VERSION"] - prev["DAYS_TERMINATION"]
    prev["DAYS_DECISION_subtr_DAYS_LAST_DUE_1ST_VERSION"] = prev["DAYS_DECISION"] - prev["DAYS_LAST_DUE_1ST_VERSION"]
    prev["DAYS_FIRST_DUE_subtr_DAYS_TERMINATION"] = prev["DAYS_FIRST_DUE"] - prev["DAYS_TERMINATION"]
    prev["DAYS_LAST_DUE_1ST_VERSION_subtr_DAYS_LAST_DUE"] = prev["DAYS_LAST_DUE_1ST_VERSION"] - prev["DAYS_LAST_DUE"]
    prev["DAYS_DECISION_subtr_DAYS_LAST_DUE"] = prev["DAYS_DECISION"] - prev[ "DAYS_LAST_DUE"]
    prev["DAYS_DECISION_subtr_DAYS_FIRST_DRAWING"] = prev["DAYS_DECISION"] - prev["DAYS_FIRST_DRAWING"]

    prev.sort_values(['SK_ID_CURR', 'DAYS_DECISION'],ascending=True, inplace=True)

    gr = prev.groupby(by=['SK_ID_CURR'])
    cols = [
        'DAYS_DECISION',
        "NFLAG_INSURED_ON_APPROVAL",
        "CNT_PAYMENT",
        "DAYS_FIRST_DRAWING",
        "AMT_ANNUITY",
        "DAYS_LAST_DUE_1ST_VERSION",
        "RATE_DOWN_PAYMENT",
        "AMT_GOODS_PRICE",
        "DAYS_LAST_DUE",
        "DAYS_FIRST_DUE",
        "HOUR_APPR_PROCESS_START",
        "AMT_CREDIT",
        "AMT_APPLICATION",
    ]
    prev = parallel_diff(prev, gr, cols)


    # Previous applications numeric features
    aggregations = {

        'AMT_ANNUITY': ['min'],
        'AMT_APPLICATION': ['skew'],
        'AMT_CREDIT': ['first'],
        'AMT_DOWN_PAYMENT': ['sum','mean','median'],
        'AMT_GOODS_PRICE': ['first'],
        'HOUR_APPR_PROCESS_START': ['max', 'mean','var'],
        'DAYS_DECISION': ['mean','last'],
        "SELLERPLACE_AREA":['mean'],
        'CNT_PAYMENT': ['max','var'],
        # 'DAYS_FIRST_DRAWING': ['max'],
        'DAYS_FIRST_DUE': ['last'],
        'DAYS_LAST_DUE_1ST_VERSION': ['max','median','last','sum'],
        'DAYS_LAST_DUE': ['last','max'],
        'DAYS_TERMINATION': ['last','max'],


        "AMT_APPLICATION_divide_AMT_CREDIT":['mean'],
        "AMT_GOODS_PRICE_divide_AMT_CREDIT":['min','mean','last'],
        "AMT_DOWN_PAYMENT_divide_CNT_PAYMENT":['sum'],
        "CNT_PAYMENT_divide_AMT_ANNUITY":['median'],
        'AMT_CREDIT_divide_AMT_APPLICATION':['mean','median'],
        "AMT_GOODS_PRICE_divide_CNT_PAYMENT":['min'],
        # "AMT_CREDIT_divide_CNT_PAYMENT":['last'],


        'DAYS_LAST_DUE_1ST_VERSION_subtr_DAYS_TERMINATION':['last'],
        'DAYS_LAST_DUE_1ST_VERSION_subtr_DAYS_LAST_DUE':['mean'],

        # category feature
        'WEEKDAY_APPR_PROCESS_START': ['last'],
        'NAME_GOODS_CATEGORY': ['last'],
        'PRODUCT_COMBINATION': ['last'],

        'nan_count': ['skew','var','median','sum'],
    }
    for k in aggregations.keys():
        aggregations[k] += [trend_feature_v2,trend_feature]

    useless_col =[
        'FLAG_LAST_APPL_PER_CONTRACT',
        'NAME_CASH_LOAN_PURPOSE',

        'NAME_CONTRACT_TYPE',
        "WEEKDAY_APPR_PROCESS_START",
        "NAME_PAYMENT_TYPE",
        # "NAME_GOODS_CATEGORY",
        "NAME_PORTFOLIO",
        # "NAME_PRODUCT_TYPE",
        "CHANNEL_TYPE",
        "NAME_GOODS_CATEGORY",
        "NAME_TYPE_SUITE",
        'NAME_SELLER_INDUSTRY',
        "PRODUCT_COMBINATION",
    ]
    col = ['Refused','Approved','Canceled']
    prev['NAME_CONTRACT_STATUS'] = prev['NAME_CONTRACT_STATUS'].apply(lambda x: 'other' if x not in col else x)

    prev, cat_cols = one_hot_encoder(prev,useless_col)
    for cat in cat_cols:
        aggregations[cat] = ['mean']

    prev_agg = agg_parallel(prev,aggregations, mp.cpu_count())
    prev_agg.columns = pd.Index(['PREV_' + e for e in prev_agg.columns])

    # -----------------------------      approved -----------------------------
    aggregations = {

        'DAYS_LAST_DUE_1ST_VERSION': ['max','sum','last'],
        'AMT_DOWN_PAYMENT': ['max','sum'],
        'AMT_ANNUITY': [ 'sum','last'],
        'AMT_APPLICATION': [ 'sum'],
        'AMT_GOODS_PRICE': ['max','first','sum','min'],
        'HOUR_APPR_PROCESS_START': ['mean','max'],
        'DAYS_LAST_DUE': ['max','last'],
        'DAYS_TERMINATION': ['last'],
        'SELLERPLACE_AREA': ['sum'],

        'DAYS_DECISION_DIFF': ['sum'],
        "DAYS_LAST_DUE_DIFF":['var'],
        "DAYS_FIRST_DUE_DIFF":['max'],

        "AMT_APPLICATION_divide_CNT_PAYMENT": ['sum','median','max','last'],
        "CNT_PAYMENT_divide_AMT_APPLICATION":['min'],
        "AMT_DOWN_PAYMENT_divide_CNT_PAYMENT":['sum','max'],
        "CNT_PAYMENT_divide_AMT_GOODS_PRICE":['median','mean','first','min','last'],
        "AMT_CREDIT_divide_AMT_GOODS_PRICE":['mean','min','last'],
        "AMT_GOODS_PRICE_divide_AMT_CREDIT":['min'],
        "CNT_PAYMENT_divide_AMT_ANNUITY":['min','median'],
        "AMT_ANNUITY_divide_CNT_PAYMENT":['last'],

        'DAYS_LAST_DUE_1ST_VERSION_subtr_DAYS_TERMINATION':['last','median'],
        # 'DAYS_DECISION_subtr_DAYS_LAST_DUE_1ST_VERSION':['min'],
        'DAYS_FIRST_DUE_subtr_DAYS_TERMINATION':['sum'],
        'DAYS_LAST_DUE_1ST_VERSION_subtr_DAYS_LAST_DUE':['mean'],
        'nan_count': stat,
    }

    approved = prev[prev['NAME_CONTRACT_STATUS_Approved'] == 1]
    approved_agg = agg_parallel(approved, aggregations, mp.cpu_count())
    approved_agg.columns = pd.Index(['APPROVED_' + e for e in approved_agg.columns])
    prev_agg = prev_agg.join(approved_agg, how='left', on='SK_ID_CURR')



    # -----------------------------      refused -----------------------------
    aggregations = {
        'DAYS_DECISION': ['last','var','mean','median','max'],
        'SELLERPLACE_AREA': ['first'],
        'DAYS_DECISION_DIFF': ['max','sum'],
        "AMT_CREDIT_DIFF":['max'],
        "AMT_CREDIT_divide_AMT_GOODS_PRICE":['max'],
        "CNT_PAYMENT_divide_AMT_GOODS_PRICE":['sum'],
        'nan_count':stat,
    }

    refused = prev[prev['NAME_CONTRACT_STATUS_Refused'] == 1]
    refused_agg = agg_parallel(refused,aggregations,mp.cpu_count())
    refused_agg.columns = pd.Index(['REFUSED_' + e for e in refused_agg.columns])
    prev_agg = prev_agg.join(refused_agg, how='left', on='SK_ID_CURR')


    gr = prev.groupby(by=['SK_ID_CURR'])
    agg_history ={
        'CNT_PAYMENT': ['mean'],
        'DAYS_DECISION': ['mean'],
        'DAYS_FIRST_DRAWING': ['mean'],
        'DAYS_LAST_DUE_1ST_VERSION': ['mean'],
    }
    for number in [3,8,14]:
        prev_applications_tail = gr.tail(number)
        tail_groupby = prev_applications_tail.groupby(by=['SK_ID_CURR'])
        g = tail_groupby.agg(agg_history)
        g.columns = pd.Index(['PREV_' + e[0] + "_" + e[1].upper()+"_"+str(number) for e in g.columns.tolist()])
        prev_agg = prev_agg.join(g, how='left', on='SK_ID_CURR')


    useless_col = [
        'PREV_NAME_CONTRACT_STATUS_nan_MEAN',
        'PREV_CODE_REJECT_REASON_SYSTEM_MEAN',
        'PREV_CODE_REJECT_REASON_XNA_MEAN',
        'PREV_CODE_REJECT_REASON_nan_MEAN',
        'PREV_NAME_CLIENT_TYPE_XNA_MEAN',
        'PREV_NAME_CLIENT_TYPE_nan_MEAN',
        'PREV_NAME_PRODUCT_TYPE_nan_MEAN',
        'PREV_NAME_YIELD_GROUP_nan_MEAN',
        'PREV_CODE_REJECT_REASON_SCOFR_MEAN',
        'PREV_CODE_REJECT_REASON_CLIENT_MEAN',
        'PREV_NAME_CONTRACT_STATUS_other_MEAN',
    ]
    prev_agg.drop(useless_col,axis=1,inplace=True)
    return prev_agg

# Preprocess POS_CASH_balance.csv
def pos_cash(num_rows=None):

    pos = pd.read_csv('./data/POS_CASH_balance.csv', nrows=num_rows)
    # pos, cat_cols = one_hot_encoder(pos, nan_as_category=True)

    pos.sort_values(['SK_ID_CURR', 'MONTHS_BALANCE'], ascending=True, inplace=True)
    pos['pos_cash_paid_late'] = (pos['SK_DPD'] > 0).astype(int)
    pos['pos_cash_paid_late_with_tolerance'] = (pos['SK_DPD_DEF'] > 0).astype(int)

    pos['MONTHS_BALANCE_subtr_CNT_INSTALMENT_FUTURE'] = pos['MONTHS_BALANCE'] - pos['CNT_INSTALMENT_FUTURE']
    pos['MONTHS_BALANCE_subtr_CNT_INSTALMENT'] = pos['MONTHS_BALANCE'] - pos['CNT_INSTALMENT']
    pos['CNT_INSTALMENT_subtr_CNT_INSTALMENT_FUTURE'] = pos['MONTHS_BALANCE'] - pos['CNT_INSTALMENT']

    gr = pos.groupby(by=['SK_ID_CURR'])
    cols = [
        'MONTHS_BALANCE',
        'CNT_INSTALMENT_FUTURE',
        # 'SK_DPD',
        'CNT_INSTALMENT',
    ]
    pos = parallel_diff(pos, gr, cols)


    # Features
    aggregations = {
        'MONTHS_BALANCE': ['min','var'],
        # 'SK_DPD': [trend_feature],
        # 'SK_DPD_DEF': ['sum'],
        'CNT_INSTALMENT_FUTURE': [ trend_feature, 'mean', 'max', 'var','last','sum'],
        # 'CNT_INSTALMENT': ['last','skew'],

        "MONTHS_BALANCE_DIFF":['sum','skew'],
        'CNT_INSTALMENT_FUTURE_DIFF':['mean','skew','var'],
        'CNT_INSTALMENT_DIFF':['var','mean'],

        'MONTHS_BALANCE_subtr_CNT_INSTALMENT_FUTURE':['mean','sum','min','median'],
        'MONTHS_BALANCE_subtr_CNT_INSTALMENT': ['mean'],
        'CNT_INSTALMENT_subtr_CNT_INSTALMENT_FUTURE': ['mean'],
    }

    trend_periods = [6,None]
    agg_periods = [6,None]
    aggre = {}
    for k, features in aggregations.items():
        aggre[k] = []
        for v in features:
            if 'DIFF' in k:
                aggre[k].append((v,[None]))
            elif v in [trend_feature_v2, trend_feature]:
                aggre[k].append((v, trend_periods))
            elif v in ['last', 'first','size']:
                aggre[k].append((v, [None]))
            else:
                aggre[k].append((v, agg_periods))

    # pre_cols = [
    #     'MONTHS_BALANCE',
    #     'CNT_INSTALMENT',
    #     'CNT_INSTALMENT_FUTURE',
    #     'SK_DPD',
    #     'SK_DPD_DEF',
    # ]
    # pos, pre_cols = get_bin_feature(pos, pre_cols)
    # aggre.update(pre_cols)

    usecol = ['Active','Completed']
    pos['NAME_CONTRACT_STATUS'] = pos['NAME_CONTRACT_STATUS'].apply(lambda x: 'other' if x not in usecol else x)
    pos, pos_cat = one_hot_encoder(pos)
    for c in pos_cat:
        aggre[c] = ['mean']

    # pos_agg = pos.groupby('SK_ID_CURR').agg(aggregations)
    pos_agg = agg_parallel(pos,aggre,mp.cpu_count())
    pos_agg.columns = pd.Index(['POS_' + e for e in pos_agg.columns])

    pos_agg['POS_COUNT'] = pos.groupby('SK_ID_CURR').size()

    return pos_agg



def installments_payments(num_rows=None):
    ins = pd.read_csv('./data/installments_payments.csv', nrows=num_rows)
    ins, cat_cols = one_hot_encoder(ins)


    ins['PAYMENT_PERC'] = ins['AMT_PAYMENT'] / ins['AMT_INSTALMENT']
    ins['PAYMENT_DIFF'] = ins['AMT_PAYMENT'] - ins['AMT_INSTALMENT']
    # Days past due and days before due (no negative values)
    ins['DPD'] = ins['DAYS_ENTRY_PAYMENT'] - ins['DAYS_INSTALMENT']
    ins['DBD'] = ins['DAYS_INSTALMENT'] - ins['DAYS_ENTRY_PAYMENT']
    ins['DPD'] = ins['DPD'].apply(lambda x: x if x > 0 else 0)
    ins['DBD'] = ins['DBD'].apply(lambda x: x if x > 0 else 0)

    ins.sort_values(['SK_ID_CURR', 'DAYS_INSTALMENT'], ascending=True, inplace=True)
    gr = ins.groupby('SK_ID_CURR')

    cols = [
        'DAYS_INSTALMENT',
        'DAYS_ENTRY_PAYMENT',
        # 'NUM_INSTALMENT_NUMBER',
        # 'NUM_INSTALMENT_VERSION',
        'AMT_INSTALMENT',
        # 'AMT_PAYMENT'
    ]
    ins = parallel_diff(ins,gr,cols)

    # Features: Perform aggregations
    aggregations = {
        # 'NUM_INSTALMENT_VERSION': ['nunique','last'],
        'DPD': ['sum','mean','var',trend_feature_v2,'skew','max'],
        'DBD': ['min','sum',trend_feature,'last','max'],
        'PAYMENT_PERC': ['sum','mean','min'],
        'PAYMENT_DIFF': ['mean'],

        'AMT_INSTALMENT': ['sum', 'min'],
        'AMT_PAYMENT': ['min','mean','median','sum'],
        'DAYS_ENTRY_PAYMENT': ['min','var',trend_feature,'skew'],
        'DAYS_INSTALMENT':['min','var','first'],
        'NUM_INSTALMENT_VERSION':['sum','var'],
        "NUM_INSTALMENT_NUMBER":['skew','sum'],

        'DAYS_INSTALMENT_DIFF':['sum'],                     # 'max','skew','mean','var'
        'DAYS_ENTRY_PAYMENT_DIFF':['sum','last'],           #'max', 'mean', 'var'
        # 'NUM_INSTALMENT_NUMBER_DIFF':['mean'],              # 'skew', ,'max'
        # 'NUM_INSTALMENT_VERSION_DIFF':['sum','mean','skew'],
        'AMT_INSTALMENT_DIFF':['mean'],
        # 'AMT_PAYMENT_DIFF':['skew'],
    }



    trend_periods = [10,50,None]
    agg_periods = [5,20,50,None]
    aggre = {}
    for k,features in aggregations.items():
        aggre[k] = []
        for v in features:
            if 'DIFF' in k:
                aggre[k].append((v,[None]))
            elif v in [trend_feature_v2,trend_feature]:
                aggre[k].append((v,trend_periods))
            elif v  in ['last','first']:
                aggre[k].append((v,[None]))
            else:
                aggre[k].append((v,agg_periods))

    for cat in cat_cols:
        aggre[cat] = ['mean']

    ins_agg = agg_parallel(ins,aggre,mp.cpu_count())
    ins_agg.columns = pd.Index(['INSTAL_' + e for e in ins_agg.columns])

    return ins_agg

# Preprocess credit_card_balance.csv
def credit_card_balance(num_rows=None):
    credit_card = pd.read_csv('./data/credit_card_balance.csv', nrows=num_rows)
    # General aggregations


    credit_card["AMT_RECIVABLE_divide_AMT_CREDIT_LIMIT_ACTUAL"] = \
        credit_card["AMT_RECIVABLE"]/credit_card["AMT_CREDIT_LIMIT_ACTUAL"]

    credit_card["AMT_RECEIVABLE_PRINCIPAL_divide_AMT_CREDIT_LIMIT_ACTUAL"] = \
        credit_card["AMT_RECEIVABLE_PRINCIPAL"] /credit_card["AMT_CREDIT_LIMIT_ACTUAL"]

    credit_card['AMT_BALANCE_divide_AMT_CREDIT_LIMIT_ACTUAL'] = \
        credit_card["AMT_BALANCE"] / credit_card["AMT_CREDIT_LIMIT_ACTUAL"]

    credit_card['AMT_TOTAL_RECEIVABLE_divide_AMT_CREDIT_LIMIT_ACTUAL'] = \
        credit_card["AMT_TOTAL_RECEIVABLE"] / credit_card["AMT_CREDIT_LIMIT_ACTUAL"]

    credit_card['CNT_DRAWINGS_ATM_CURRENT_divide_CNT_INSTALMENT_MATURE_CUM'] = \
        credit_card["CNT_DRAWINGS_ATM_CURRENT"] / credit_card["CNT_INSTALMENT_MATURE_CUM"]

    credit_card['AMT_PAYMENT_TOTAL_CURRENT_divide_AMT_RECEIVABLE_PRINCIPAL'] = \
        credit_card["AMT_PAYMENT_TOTAL_CURRENT"] / credit_card["AMT_RECEIVABLE_PRINCIPAL"]

    credit_card['AMT_RECEIVABLE_PRINCIPAL_divide_AMT_PAYMENT_CURRENT'] = \
        credit_card["AMT_RECEIVABLE_PRINCIPAL"] / credit_card["AMT_PAYMENT_CURRENT"]

    credit_card['CNT_INSTALMENT_MATURE_CUM_divide_AMT_RECIVABLE'] = \
        credit_card["CNT_INSTALMENT_MATURE_CUM"] / credit_card["AMT_RECIVABLE"]

    credit_card['AMT_RECIVABLE_divide_AMT_PAYMENT_TOTAL_CURRENT'] = \
        credit_card["AMT_RECIVABLE"] / credit_card["AMT_PAYMENT_TOTAL_CURRENT"]

    credit_card['AMT_INST_MIN_REGULARITY_divide_AMT_CREDIT_LIMIT_ACTUAL'] = \
        credit_card["AMT_INST_MIN_REGULARITY"] / credit_card["AMT_CREDIT_LIMIT_ACTUAL"]

    credit_card['CNT_DRAWINGS_POS_CURRENT_divide_AMT_DRAWINGS_POS_CURRENT'] = \
        credit_card["CNT_DRAWINGS_POS_CURRENT"] / credit_card["AMT_DRAWINGS_POS_CURRENT"]

    credit_card.sort_values(['SK_ID_CURR', 'MONTHS_BALANCE'],ascending=True,inplace=True)

    groupby = credit_card.groupby(by=['SK_ID_CURR'])
    cols = [
        'CNT_DRAWINGS_CURRENT',
    ]
    credit_card = parallel_diff(credit_card, groupby, cols)

    # Features: Perform aggregations
    aggregations = {
        "AMT_DRAWINGS_ATM_CURRENT":['last'],
        "CNT_DRAWINGS_ATM_CURRENT":['mean'],
        "CNT_DRAWINGS_CURRENT":['max'],
        "MONTHS_BALANCE":['size'],

        "CNT_DRAWINGS_CURRENT_DIFF":['var'],

        "AMT_RECIVABLE_divide_AMT_CREDIT_LIMIT_ACTUAL": ['last'],
        'CNT_INSTALMENT_MATURE_CUM_divide_AMT_RECIVABLE': ['last'],
        'AMT_RECIVABLE_divide_AMT_PAYMENT_TOTAL_CURRENT': ['median'],
        "AMT_RECEIVABLE_PRINCIPAL_divide_AMT_CREDIT_LIMIT_ACTUAL":['last'],
        "AMT_PAYMENT_TOTAL_CURRENT_divide_AMT_RECEIVABLE_PRINCIPAL": ['median'],
        "AMT_RECEIVABLE_PRINCIPAL_divide_AMT_PAYMENT_CURRENT": ['median'],
        # "AMT_RECEIVABLE_PRINCIPAL_divide_CNT_INSTALMENT_MATURE_CUM": ['median','last'],
        "AMT_BALANCE_divide_AMT_CREDIT_LIMIT_ACTUAL":['last'],
        "AMT_TOTAL_RECEIVABLE_divide_AMT_CREDIT_LIMIT_ACTUAL":['last'],
        "CNT_DRAWINGS_ATM_CURRENT_divide_CNT_INSTALMENT_MATURE_CUM": ['mean'],
        'AMT_INST_MIN_REGULARITY_divide_AMT_CREDIT_LIMIT_ACTUAL': ['max','last'],
        'CNT_DRAWINGS_POS_CURRENT_divide_AMT_DRAWINGS_POS_CURRENT':['median'],
    }

    cc_agg = agg_parallel(credit_card, aggregations, mp.cpu_count())
    cc_agg.columns = pd.Index(['CC_' + e for e in cc_agg.columns])

    cols = [
        'AMT_BALANCE',
        'AMT_CREDIT_LIMIT_ACTUAL',
        'AMT_DRAWINGS_ATM_CURRENT',
        'AMT_DRAWINGS_CURRENT',
        'AMT_DRAWINGS_OTHER_CURRENT',
        'AMT_DRAWINGS_POS_CURRENT',
        'AMT_INST_MIN_REGULARITY',
        'AMT_PAYMENT_CURRENT',
        'AMT_PAYMENT_TOTAL_CURRENT',
        'AMT_RECEIVABLE_PRINCIPAL',
        'AMT_RECIVABLE',
        'AMT_TOTAL_RECEIVABLE',
    ]
    credit_card,cols = comb_feat(credit_card, cols, '+')
    # ----------          period1  --------------------------------------
    aggregations = {
        'CNT_DRAWINGS_ATM_CURRENT':['mean'],
        'AMT_DRAWINGS_ATM_CURRENT':['max'],
        'CNT_DRAWINGS_CURRENT':['mean'],
    }

    credit_card_1 = credit_card[credit_card['MONTHS_BALANCE']>-12]
    credit_card_period1 = agg_parallel(credit_card_1, aggregations, mp.cpu_count())
    credit_card_period1.columns = pd.Index(['CC_PERIOD1_' + e for e in credit_card_period1.columns])
    cc_agg = cc_agg.join(credit_card_period1, how='left', on='SK_ID_CURR')


    # ----------          period2  --------------------------------------
    aggregations = {
        'CNT_DRAWINGS_ATM_CURRENT':['mean'],
        'CNT_DRAWINGS_CURRENT': ['var'],
        'AMT_DRAWINGS_ATM_CURRENT_add_AMT_RECEIVABLE_PRINCIPAL':['median'],
        'AMT_INST_MIN_REGULARITY_add_AMT_TOTAL_RECEIVABLE':['last'],
        'AMT_BALANCE_add_AMT_DRAWINGS_ATM_CURRENT':['median'],
        'AMT_DRAWINGS_ATM_CURRENT_add_AMT_INST_MIN_REGULARITY':['last'],
        'AMT_RECEIVABLE_PRINCIPAL_add_AMT_RECIVABLE':['last'],
    }
    credit_card_2 = credit_card[credit_card['MONTHS_BALANCE']>-24]
    credit_card_period2 = agg_parallel(credit_card_2, aggregations, mp.cpu_count())
    credit_card_period2.columns = pd.Index(['CC_PERIOD2_' + e for e in credit_card_period2.columns])
    cc_agg = cc_agg.join(credit_card_period2, how='left', on='SK_ID_CURR')


    return cc_agg

def merge_data(debug=False):

    num_rows = 10000 if debug else None

    df = application_train_test(num_rows)

    feat_gen = {
        'cred':1,
        'ins':0,
        'bure':1,
        'prev':1,
        'pos':0,

    }

    with timer("Process previous_applications"):
        if feat_gen['prev'] ==1:
            prev = previous_applications(num_rows)
            prev.to_csv('./data/prev_feat.csv')
        else:
            prev = pd.read_csv('./data/prev_feat.csv',index_col='SK_ID_CURR')
        print("Previous applications df shape:", prev.shape)
        df = df.join(prev, how='left', on='SK_ID_CURR')
        del prev
        gc.collect()
    with timer("Process installments payments"):
        if feat_gen['ins'] ==1:
            ins = installments_payments(num_rows)
            ins.to_csv('./data/ins_feat.csv')
        else:
            ins = pd.read_csv('./data/ins_feat.csv',index_col='SK_ID_CURR')
        print("Installments payments df shape:", ins.shape)
        df = df.join(ins, how='left', on='SK_ID_CURR')
        del ins
        gc.collect()
    with timer("Process credit card balance"):
        if feat_gen['cred'] ==1:
            cc = credit_card_balance(num_rows)
            cc.to_csv('./data/cred_feat.csv')
        else:
            cc = pd.read_csv('./data/cred_feat.csv',index_col='SK_ID_CURR')

        print("Credit card balance df shape:", cc.shape)
        df = df.join(cc, how='left', on='SK_ID_CURR')
        del cc
        gc.collect()
    with timer("Process bureau and bureau_balance"):
        if feat_gen['bure'] ==1:
            bureau = bureau_and_balance(num_rows)
            bureau.to_csv('./data/bure_feat.csv')
        else:
            bureau = pd.read_csv('./data/bure_feat.csv',index_col='SK_ID_CURR')
        print("Bureau df shape:", bureau.shape)
        df = df.join(bureau, how='left', on='SK_ID_CURR')
        del bureau
        gc.collect()



    with timer("Process POS-CASH balance"):
        if feat_gen['pos'] ==1:
            pos = pos_cash(num_rows)
            pos.to_csv('./data/pos_feat.csv')
        else:
            pos = pd.read_csv('./data/pos_feat.csv',index_col='SK_ID_CURR')
        print("Pos-cash balance df shape:", pos.shape)
        df = df.join(pos, how='left', on='SK_ID_CURR')
        del pos
        gc.collect()


    tr = df[df['TARGET'].notnull()]
    te = df[df['TARGET'].isnull()]

    te.drop(['TARGET'],axis=1,inplace=True)

    print(tr.info())
    print(te.info())

    tr.to_csv('./data/tr.csv',index=False)
    te.to_csv('./data/te.csv',index=False)




if __name__ == "__main__":
    # set_dtypes()
    merge_data()




