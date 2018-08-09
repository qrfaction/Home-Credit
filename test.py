
import pandas as pd
import numpy as np
from config import useless_col

# train = pd.read_csv('./data/application_train.csv')
# test = pd.read_csv('./data/application_test.csv')
prev = pd.read_csv('./data/tr.csv')
# pos_cash = pd.read_csv('./data/POS_CASH_balance.csv')
# buro = pd.read_csv('./data/bureau.csv')
# burobl = pd.read_csv('./data/bureau_balance.csv')
# credit = pd.read_csv('./data/credit_card_balance.csv')
# installment = pd.read_csv('./data/installments_payments.csv')

# files = [train,test,prev,pos_cash,buro,burobl,credit,installment]

# print(buro.nunique())
# print(buro.info)
# print(buro.shape)

cols_importance = pd.read_csv("feat_importance.csv").sort_values(by=['importance2'],ascending=False)
cols_importance = cols_importance['name'].tolist()[:400]
for col in prev.columns:
    if col not in cols_importance and col not in useless_col:
        print(col)

# for table in files:
#     cols = table.columns
#     num_unique = table.nunique()
#     types = table.dtypes
#     print(table.describe())
#     for i,j,k in zip(cols,num_unique,types):
#         if k==np.object:
#
#             print(i,j,k)

"""
SK_ID_PREV                       int64
SK_ID_CURR                       int64
AMT_ANNUITY                    float64
AMT_APPLICATION                float64
AMT_CREDIT                     float64
AMT_DOWN_PAYMENT               float64
AMT_GOODS_PRICE                float64
HOUR_APPR_PROCESS_START          int64
RATE_DOWN_PAYMENT              float64
DAYS_DECISION                    int64
CNT_PAYMENT                    float64

NFLAG_LAST_APPL_IN_DAY           int64
RATE_INTEREST_PRIMARY          float64
RATE_INTEREST_PRIVILEGED       float64
SELLERPLACE_AREA                 int64
DAYS_FIRST_DRAWING             float64
DAYS_FIRST_DUE                 float64
DAYS_LAST_DUE_1ST_VERSION      float64
DAYS_LAST_DUE                  float64
DAYS_TERMINATION               float64
NFLAG_INSURED_ON_APPROVAL      float64




NAME_CONTRACT_TYPE              object
NAME_SELLER_INDUSTRY            object
NAME_YIELD_GROUP                object
PRODUCT_COMBINATION             object
NAME_PAYMENT_TYPE               object
CODE_REJECT_REASON              object
NAME_TYPE_SUITE                 object
NAME_CLIENT_TYPE                object
NAME_GOODS_CATEGORY             object
NAME_PORTFOLIO                  object
NAME_PRODUCT_TYPE               object
CHANNEL_TYPE                    object
NAME_CASH_LOAN_PURPOSE          object
FLAG_LAST_APPL_PER_CONTRACT     object
NAME_CONTRACT_STATUS            object
WEEKDAY_APPR_PROCESS_START      object



"""






