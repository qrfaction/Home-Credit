






useless_col = [

    "NONLIVINGAPARTMENTS_MODE",
    "LIVE_REGION_NOT_WORK_REGION",
    'FLAG_EMAIL',
    "AMT_REQ_CREDIT_BUREAU_WEEK",
    "AMT_REQ_CREDIT_BUREAU_QRT",
    "AMT_REQ_CREDIT_BUREAU_MON",
    "AMT_REQ_CREDIT_BUREAU_YEAR",
    "AMT_REQ_CREDIT_BUREAU_DAY",
    "AMT_REQ_CREDIT_BUREAU_HOUR",
    "FLAG_EMP_PHONE",
    "REG_REGION_NOT_WORK_REGION",
    "REG_REGION_NOT_LIVE_REGION",
    "REG_CITY_NOT_WORK_CITY",
    "EMERGENCYSTATE_MODE",
    "HOUSETYPE_MODE",
    "CNT_FAM_MEMBERS",
    "FLAG_PHONE",
    "FLAG_OWN_REALTY",
    "FLAG_MOBIL",
    "FLAG_CONT_MOBILE",
    "LIVE_CITY_NOT_WORK_CITY",
    "NONLIVINGAPARTMENTS_MEDI",
    "NAME_TYPE_SUITE",
    "NONLIVINGAPARTMENTS_AVG",
    "CNT_CHILDREN",
    "FLOORSMIN_MODE",
    "FLOORSMIN_MEDI",
    "ELEVATORS_MEDI",
    "COMMONAREA_MODE",
    "FONDKAPREMONT_MODE",
    "FLOORSMIN_AVG",


    'NAME_EDUCATION_TYPE',
    'ORGANIZATION_TYPE',
    'OCCUPATION_TYPE',



    "ACTIVE_AMT_CREDIT_SUM_DEBT_LAST",
    "ACTIVE_AMT_CREDIT_SUM_DEBT_SUM",
    "ACTIVE_AMT_CREDIT_SUM_DEBT_MIN",
    "ACTIVE_AMT_CREDIT_SUM_DEBT_MEAN",

    # "BURO_DAYS_CREDIT_ENDDATE_DIFF_MAX",
    # "BURO_DAYS_CREDIT_UPDATE_DIFF_LAST",
    # "BURO_DAYS_ENDDATE_FACT_DIFF_MEAN",
    #
    # "BURO_AMT_CREDIT_SUM_DIFF_SUM",
    # "BURO_AMT_CREDIT_SUM_DIFF_VAR",
    #
    # "BURO_DAYS_ENDDATE_FACT_bin_nan_MEAN",


    "CLOSED_DAYS_ENDDATE_FACT_LAST",
    "CLOSED_DAYS_ENDDATE_FACT_SUM",
    "CLOSED_DAYS_ENDDATE_FACT_MIN",
    "CLOSED_DAYS_ENDDATE_FACT_VAR",
    "CLOSED_DAYS_ENDDATE_FACT_MAX",

    # "CLOSED_AMT_CREDIT_SUM_MEAN",
    # "CLOSED_AMT_CREDIT_SUM_SUM",
    # "CLOSED_AMT_CREDIT_SUM_FIRST",
    # "CLOSED_AMT_CREDIT_SUM_MAX",

    # "ACTIVE_AMT_CREDIT_SUM_FIRST",
    # "ACTIVE_AMT_CREDIT_SUM_SUM",
    # "ACTIVE_AMT_CREDIT_SUM_MIN",
    # "ACTIVE_AMT_CREDIT_SUM_MAX",
    # "ACTIVE_AMT_CREDIT_SUM_MEDIAN",

]


prev_drop_col = [
    "AMT_CREDIT"
]

bureau_drop_col = [
    "AMT_ANNUITY"
]


"""
[50]	train's auc: 0.770644	valid's auc: 0.759071
[100]	train's auc: 0.77906	valid's auc: 0.766885
[150]	train's auc: 0.78569	valid's auc: 0.77315
[200]	train's auc: 0.79059	valid's auc: 0.776564
[250]	train's auc: 0.794684	valid's auc: 0.77949
[300]	train's auc: 0.798187	valid's auc: 0.781887
[350]	train's auc: 0.801341	valid's auc: 0.784006
[400]	train's auc: 0.804102	valid's auc: 0.785445
[450]	train's auc: 0.806767	valid's auc: 0.786882
[500]	train's auc: 0.809181	valid's auc: 0.788122
[550]	train's auc: 0.811497	valid's auc: 0.789178
[600]	train's auc: 0.813619	valid's auc: 0.790203
[650]	train's auc: 0.815641	valid's auc: 0.791066
[700]	train's auc: 0.817578	valid's auc: 0.791712
[750]	train's auc: 0.819543	valid's auc: 0.792457
[800]	train's auc: 0.821397	valid's auc: 0.79307
[850]	train's auc: 0.823165	valid's auc: 0.79372
[900]	train's auc: 0.824854	valid's auc: 0.794251
[950]	train's auc: 0.826506	valid's auc: 0.794675
[1000]	train's auc: 0.828131	valid's auc: 0.795106
[1050]	train's auc: 0.829745	valid's auc: 0.795528
[1100]	train's auc: 0.831207	valid's auc: 0.795883
[1150]	train's auc: 0.832722	valid's auc: 0.796225
[1200]	train's auc: 0.834202	valid's auc: 0.796587
[1250]	train's auc: 0.835683	valid's auc: 0.796892
[1300]	train's auc: 0.837079	valid's auc: 0.797157
[1350]	train's auc: 0.838468	valid's auc: 0.79741
[1400]	train's auc: 0.839798	valid's auc: 0.797515
[1450]	train's auc: 0.841155	valid's auc: 0.797762
[1500]	train's auc: 0.84245	valid's auc: 0.797936
[1550]	train's auc: 0.843763	valid's auc: 0.798167
[1600]	train's auc: 0.845087	valid's auc: 0.798372
[1650]	train's auc: 0.846428	valid's auc: 0.798539
[1700]	train's auc: 0.847623	valid's auc: 0.798708
[1750]	train's auc: 0.848899	valid's auc: 0.79885
[1800]	train's auc: 0.850107	valid's auc: 0.798969
[1850]	train's auc: 0.851263	valid's auc: 0.799073
[1900]	train's auc: 0.85247	valid's auc: 0.799154
[1950]	train's auc: 0.853596	valid's auc: 0.799301
[2000]	train's auc: 0.854772	valid's auc: 0.799439
[2050]	train's auc: 0.855915	valid's auc: 0.799507
[2100]	train's auc: 0.856988	valid's auc: 0.799656
[2150]	train's auc: 0.858113	valid's auc: 0.799774
[2200]	train's auc: 0.859213	valid's auc: 0.799913
[2250]	train's auc: 0.860302	valid's auc: 0.800033
[2300]	train's auc: 0.861375	valid's auc: 0.800115
[2350]	train's auc: 0.862397	valid's auc: 0.800168
[2400]	train's auc: 0.863399	valid's auc: 0.800191
[2450]	train's auc: 0.864401	valid's auc: 0.800282
[2500]	train's auc: 0.865434	valid's auc: 0.80035
[2550]	train's auc: 0.866473	valid's auc: 0.800437
[2600]	train's auc: 0.867435	valid's auc: 0.80054
[2650]	train's auc: 0.868482	valid's auc: 0.800635
[2700]	train's auc: 0.869443	valid's auc: 0.800663
[2750]	train's auc: 0.8704	valid's auc: 0.800727
[2800]	train's auc: 0.871366	valid's auc: 0.800807
[2850]	train's auc: 0.872309	valid's auc: 0.800887
[2900]	train's auc: 0.873226	valid's auc: 0.800927
[2950]	train's auc: 0.874142	valid's auc: 0.80092
[3000]	train's auc: 0.875019	valid's auc: 0.80093
[3050]	train's auc: 0.875896	valid's auc: 0.800948
[3100]	train's auc: 0.8768	valid's auc: 0.800971
[3150]	train's auc: 0.877702	valid's auc: 0.800977
[3200]	train's auc: 0.878563	valid's auc: 0.801021
[3250]	train's auc: 0.879479	valid's auc: 0.801026
[3300]	train's auc: 0.88037	valid's auc: 0.801007
[3350]	train's auc: 0.881275	valid's auc: 0.801063
[3400]	train's auc: 0.882112	valid's auc: 0.801056
[3450]	train's auc: 0.882955	valid's auc: 0.801071
[3500]	train's auc: 0.883767	valid's auc: 0.801115
[3550]	train's auc: 0.884547	valid's auc: 0.801078
[3600]	train's auc: 0.88533	valid's auc: 0.801083
[3650]	train's auc: 0.886153	valid's auc: 0.801074
[3700]	train's auc: 0.886973	valid's auc: 0.801121
[3750]	train's auc: 0.88776	valid's auc: 0.80114
[3800]	train's auc: 0.888529	valid's auc: 0.80111
[3850]	train's auc: 0.889351	valid's auc: 0.80112
[3900]	train's auc: 0.890131	valid's auc: 0.801151
[3950]	train's auc: 0.890868	valid's auc: 0.801133
[4000]	train's auc: 0.891627	valid's auc: 0.801153
[4050]	train's auc: 0.892356	valid's auc: 0.801096
[4100]	train's auc: 0.893114	valid's auc: 0.801079
[4150]	train's auc: 0.893877	valid's auc: 0.801067
[4200]	train's auc: 0.894596	valid's auc: 0.801027
Early stopping, best iteration is:
[3922]	train's auc: 0.890443	valid's auc: 0.801173


fold : 1
[50]	train's auc: 0.771184	valid's auc: 0.75835
[100]	train's auc: 0.779146	valid's auc: 0.765512
[150]	train's auc: 0.785715	valid's auc: 0.77099
[200]	train's auc: 0.790494	valid's auc: 0.774481
[250]	train's auc: 0.794546	valid's auc: 0.777738
[300]	train's auc: 0.798075	valid's auc: 0.780266
[350]	train's auc: 0.801264	valid's auc: 0.782605
[400]	train's auc: 0.803951	valid's auc: 0.784308
[450]	train's auc: 0.806555	valid's auc: 0.785925
[500]	train's auc: 0.808956	valid's auc: 0.787137
[550]	train's auc: 0.811218	valid's auc: 0.788209
[600]	train's auc: 0.813401	valid's auc: 0.789272
[650]	train's auc: 0.815437	valid's auc: 0.790187
[700]	train's auc: 0.817383	valid's auc: 0.79104
[750]	train's auc: 0.819337	valid's auc: 0.791799
[800]	train's auc: 0.82118	valid's auc: 0.792473
[850]	train's auc: 0.822946	valid's auc: 0.793163
[900]	train's auc: 0.824643	valid's auc: 0.793745
[950]	train's auc: 0.826285	valid's auc: 0.794242
[1000]	train's auc: 0.827862	valid's auc: 0.794682
[1050]	train's auc: 0.82951	valid's auc: 0.795116
[1100]	train's auc: 0.830999	valid's auc: 0.795533
[1150]	train's auc: 0.832528	valid's auc: 0.795895
[1200]	train's auc: 0.834006	valid's auc: 0.796291
[1250]	train's auc: 0.835477	valid's auc: 0.79658
[1300]	train's auc: 0.836879	valid's auc: 0.796821
[1350]	train's auc: 0.838229	valid's auc: 0.79705
[1400]	train's auc: 0.83959	valid's auc: 0.797267
[1450]	train's auc: 0.840913	valid's auc: 0.797459
[1500]	train's auc: 0.842211	valid's auc: 0.797711
[1550]	train's auc: 0.843531	valid's auc: 0.797972
[1600]	train's auc: 0.844895	valid's auc: 0.798155
[1650]	train's auc: 0.846216	valid's auc: 0.798365
[1700]	train's auc: 0.847427	valid's auc: 0.798487
[1750]	train's auc: 0.848677	valid's auc: 0.798673
[1800]	train's auc: 0.849895	valid's auc: 0.798877
[1850]	train's auc: 0.851069	valid's auc: 0.799087
[1900]	train's auc: 0.85225	valid's auc: 0.799099
[1950]	train's auc: 0.853424	valid's auc: 0.799252
[2000]	train's auc: 0.854572	valid's auc: 0.79936
[2050]	train's auc: 0.855737	valid's auc: 0.799456
[2100]	train's auc: 0.856829	valid's auc: 0.799508
[2150]	train's auc: 0.857997	valid's auc: 0.799582
[2200]	train's auc: 0.859106	valid's auc: 0.799751
[2250]	train's auc: 0.860124	valid's auc: 0.799879
[2300]	train's auc: 0.86121	valid's auc: 0.800026
[2350]	train's auc: 0.862319	valid's auc: 0.800131
[2400]	train's auc: 0.86331	valid's auc: 0.8002
[2450]	train's auc: 0.864287	valid's auc: 0.800249
[2500]	train's auc: 0.865292	valid's auc: 0.800305
[2550]	train's auc: 0.86632	valid's auc: 0.800426
[2600]	train's auc: 0.867318	valid's auc: 0.800459
[2650]	train's auc: 0.868261	valid's auc: 0.800537
[2700]	train's auc: 0.869161	valid's auc: 0.800587
[2750]	train's auc: 0.870071	valid's auc: 0.800631
[2800]	train's auc: 0.871045	valid's auc: 0.800694
[2850]	train's auc: 0.871987	valid's auc: 0.80071
[2900]	train's auc: 0.872949	valid's auc: 0.80074
[2950]	train's auc: 0.873908	valid's auc: 0.800797
[3000]	train's auc: 0.874826	valid's auc: 0.800827
[3050]	train's auc: 0.875689	valid's auc: 0.800816
[3100]	train's auc: 0.876595	valid's auc: 0.80087
[3150]	train's auc: 0.877495	valid's auc: 0.800899
[3200]	train's auc: 0.878383	valid's auc: 0.800934
[3250]	train's auc: 0.87926	valid's auc: 0.80096
[3300]	train's auc: 0.880161	valid's auc: 0.801005
[3350]	train's auc: 0.881005	valid's auc: 0.801017
[3400]	train's auc: 0.881833	valid's auc: 0.801029
[3450]	train's auc: 0.882708	valid's auc: 0.80105
[3500]	train's auc: 0.883524	valid's auc: 0.801048
[3550]	train's auc: 0.884322	valid's auc: 0.80106
[3600]	train's auc: 0.885111	valid's auc: 0.801056
[3650]	train's auc: 0.885945	valid's auc: 0.801059
[3700]	train's auc: 0.886745	valid's auc: 0.801066
[3750]	train's auc: 0.887576	valid's auc: 0.801139
[3800]	train's auc: 0.888354	valid's auc: 0.801105
[3850]	train's auc: 0.889169	valid's auc: 0.801123
[3900]	train's auc: 0.889949	valid's auc: 0.801124
[3950]	train's auc: 0.890701	valid's auc: 0.801109
[4000]	train's auc: 0.891471	valid's auc: 0.801106
[4050]	train's auc: 0.892222	valid's auc: 0.801096
Early stopping, best iteration is:
[3751]	train's auc: 0.887591	valid's auc: 0.801147


fold : 2
[50]	train's auc: 0.771066	valid's auc: 0.756301
[100]	train's auc: 0.779051	valid's auc: 0.764159
[150]	train's auc: 0.785583	valid's auc: 0.770443
[200]	train's auc: 0.790286	valid's auc: 0.774204
[250]	train's auc: 0.794384	valid's auc: 0.777576
[300]	train's auc: 0.797932	valid's auc: 0.780194
[350]	train's auc: 0.80102	valid's auc: 0.782511
[400]	train's auc: 0.803736	valid's auc: 0.784217
[450]	train's auc: 0.80633	valid's auc: 0.786049
[500]	train's auc: 0.808727	valid's auc: 0.787456
[550]	train's auc: 0.810964	valid's auc: 0.788709
[600]	train's auc: 0.813144	valid's auc: 0.789927
[650]	train's auc: 0.81518	valid's auc: 0.790862
[700]	train's auc: 0.817128	valid's auc: 0.791659
[750]	train's auc: 0.81908	valid's auc: 0.79246
[800]	train's auc: 0.820909	valid's auc: 0.793245
[850]	train's auc: 0.82268	valid's auc: 0.793802
[900]	train's auc: 0.824395	valid's auc: 0.794418
[950]	train's auc: 0.826034	valid's auc: 0.794854
[1000]	train's auc: 0.827638	valid's auc: 0.79537
[1050]	train's auc: 0.829271	valid's auc: 0.79585
[1100]	train's auc: 0.83078	valid's auc: 0.796263
[1150]	train's auc: 0.832293	valid's auc: 0.796658
[1200]	train's auc: 0.833797	valid's auc: 0.797086
[1250]	train's auc: 0.835293	valid's auc: 0.797394
[1300]	train's auc: 0.836668	valid's auc: 0.797681
[1350]	train's auc: 0.838061	valid's auc: 0.79795
[1400]	train's auc: 0.839389	valid's auc: 0.798103
[1450]	train's auc: 0.840685	valid's auc: 0.798354
[1500]	train's auc: 0.841975	valid's auc: 0.798595
[1550]	train's auc: 0.843228	valid's auc: 0.798754
[1600]	train's auc: 0.844499	valid's auc: 0.798915
[1650]	train's auc: 0.845814	valid's auc: 0.799098
[1700]	train's auc: 0.847015	valid's auc: 0.799225
[1750]	train's auc: 0.848213	valid's auc: 0.799378
[1800]	train's auc: 0.849375	valid's auc: 0.799553
[1850]	train's auc: 0.850547	valid's auc: 0.799722
[1900]	train's auc: 0.851697	valid's auc: 0.799903
[1950]	train's auc: 0.852797	valid's auc: 0.799961
[2000]	train's auc: 0.853949	valid's auc: 0.800051
[2050]	train's auc: 0.855059	valid's auc: 0.800176
[2100]	train's auc: 0.856135	valid's auc: 0.80025
[2150]	train's auc: 0.85722	valid's auc: 0.800413
[2200]	train's auc: 0.858267	valid's auc: 0.800544
[2250]	train's auc: 0.859355	valid's auc: 0.800647
[2300]	train's auc: 0.860435	valid's auc: 0.800768
[2350]	train's auc: 0.861464	valid's auc: 0.800919
[2400]	train's auc: 0.86244	valid's auc: 0.801023
[2450]	train's auc: 0.863436	valid's auc: 0.801053
[2500]	train's auc: 0.864381	valid's auc: 0.801114
[2550]	train's auc: 0.865366	valid's auc: 0.801165
[2600]	train's auc: 0.866378	valid's auc: 0.801201
[2650]	train's auc: 0.867334	valid's auc: 0.801239
[2700]	train's auc: 0.868278	valid's auc: 0.80131
[2750]	train's auc: 0.869202	valid's auc: 0.801357
[2800]	train's auc: 0.870143	valid's auc: 0.801423
[2850]	train's auc: 0.871072	valid's auc: 0.801488
[2900]	train's auc: 0.871985	valid's auc: 0.801543
[2950]	train's auc: 0.872892	valid's auc: 0.801594
[3000]	train's auc: 0.873753	valid's auc: 0.801643
[3050]	train's auc: 0.874662	valid's auc: 0.801661
[3100]	train's auc: 0.875568	valid's auc: 0.801693
[3150]	train's auc: 0.876478	valid's auc: 0.801709
[3200]	train's auc: 0.87734	valid's auc: 0.801732
[3250]	train's auc: 0.878188	valid's auc: 0.801746
[3300]	train's auc: 0.879045	valid's auc: 0.801773
[3350]	train's auc: 0.879923	valid's auc: 0.801793
[3400]	train's auc: 0.880792	valid's auc: 0.80184
[3450]	train's auc: 0.881631	valid's auc: 0.801828
[3500]	train's auc: 0.882496	valid's auc: 0.801802
[3550]	train's auc: 0.883283	valid's auc: 0.801806
[3600]	train's auc: 0.884083	valid's auc: 0.801823
[3650]	train's auc: 0.8849	valid's auc: 0.801812
[3700]	train's auc: 0.885666	valid's auc: 0.80184
[3750]	train's auc: 0.886491	valid's auc: 0.801886
[3800]	train's auc: 0.887248	valid's auc: 0.8019
[3850]	train's auc: 0.888035	valid's auc: 0.801904
[3900]	train's auc: 0.888794	valid's auc: 0.80192
[3950]	train's auc: 0.889562	valid's auc: 0.801907
[4000]	train's auc: 0.890357	valid's auc: 0.801893
[4050]	train's auc: 0.891146	valid's auc: 0.801885
[4100]	train's auc: 0.891894	valid's auc: 0.801859
Early stopping, best iteration is:
[3824]	train's auc: 0.887644	valid's auc: 0.801936


fold : 3
[50]	train's auc: 0.770308	valid's auc: 0.766655
[100]	train's auc: 0.778713	valid's auc: 0.77294
[150]	train's auc: 0.785358	valid's auc: 0.777841
[200]	train's auc: 0.790009	valid's auc: 0.780858
[250]	train's auc: 0.794193	valid's auc: 0.783408
[300]	train's auc: 0.797757	valid's auc: 0.78543
[350]	train's auc: 0.800928	valid's auc: 0.787402
[400]	train's auc: 0.803609	valid's auc: 0.788823
[450]	train's auc: 0.806251	valid's auc: 0.790075
[500]	train's auc: 0.808625	valid's auc: 0.791198
[550]	train's auc: 0.810877	valid's auc: 0.792033
[600]	train's auc: 0.813081	valid's auc: 0.792946
[650]	train's auc: 0.815154	valid's auc: 0.793625
[700]	train's auc: 0.817174	valid's auc: 0.794292
[750]	train's auc: 0.819158	valid's auc: 0.794812
[800]	train's auc: 0.821011	valid's auc: 0.795343
[850]	train's auc: 0.822796	valid's auc: 0.795867
[900]	train's auc: 0.824526	valid's auc: 0.796312
[950]	train's auc: 0.826169	valid's auc: 0.796587
[1000]	train's auc: 0.827748	valid's auc: 0.796963
[1050]	train's auc: 0.829383	valid's auc: 0.797335
[1100]	train's auc: 0.830899	valid's auc: 0.797681
[1150]	train's auc: 0.832473	valid's auc: 0.797924
[1200]	train's auc: 0.833976	valid's auc: 0.798124
[1250]	train's auc: 0.835429	valid's auc: 0.798302
[1300]	train's auc: 0.836895	valid's auc: 0.798495
[1350]	train's auc: 0.83829	valid's auc: 0.798657
[1400]	train's auc: 0.839637	valid's auc: 0.798757
[1450]	train's auc: 0.840949	valid's auc: 0.798892
[1500]	train's auc: 0.842268	valid's auc: 0.799094
[1550]	train's auc: 0.843608	valid's auc: 0.799279
[1600]	train's auc: 0.844923	valid's auc: 0.799434
[1650]	train's auc: 0.846279	valid's auc: 0.79957
[1700]	train's auc: 0.847501	valid's auc: 0.799711
[1750]	train's auc: 0.848771	valid's auc: 0.799795
[1800]	train's auc: 0.850007	valid's auc: 0.799891
[1850]	train's auc: 0.851186	valid's auc: 0.799993
[1900]	train's auc: 0.852386	valid's auc: 0.800099
[1950]	train's auc: 0.853524	valid's auc: 0.80018
[2000]	train's auc: 0.854688	valid's auc: 0.800262
[2050]	train's auc: 0.855776	valid's auc: 0.800329
[2100]	train's auc: 0.856892	valid's auc: 0.800395
[2150]	train's auc: 0.858015	valid's auc: 0.800497
[2200]	train's auc: 0.859088	valid's auc: 0.800593
[2250]	train's auc: 0.860185	valid's auc: 0.800656
[2300]	train's auc: 0.861242	valid's auc: 0.800698
[2350]	train's auc: 0.862289	valid's auc: 0.800813
[2400]	train's auc: 0.863304	valid's auc: 0.800881
[2450]	train's auc: 0.864338	valid's auc: 0.800876
[2500]	train's auc: 0.86534	valid's auc: 0.800926
[2550]	train's auc: 0.866311	valid's auc: 0.80097
[2600]	train's auc: 0.867331	valid's auc: 0.800956
[2650]	train's auc: 0.868318	valid's auc: 0.800992
[2700]	train's auc: 0.869293	valid's auc: 0.80102
[2750]	train's auc: 0.870214	valid's auc: 0.801066
[2800]	train's auc: 0.871159	valid's auc: 0.801085
[2850]	train's auc: 0.872096	valid's auc: 0.801094
[2900]	train's auc: 0.873034	valid's auc: 0.801095
[2950]	train's auc: 0.873975	valid's auc: 0.801097
[3000]	train's auc: 0.874835	valid's auc: 0.80111
[3050]	train's auc: 0.875693	valid's auc: 0.801192
[3100]	train's auc: 0.876587	valid's auc: 0.801235
[3150]	train's auc: 0.877489	valid's auc: 0.801286
[3200]	train's auc: 0.878327	valid's auc: 0.801277
[3250]	train's auc: 0.879162	valid's auc: 0.801265
[3300]	train's auc: 0.880043	valid's auc: 0.80127
[3350]	train's auc: 0.880912	valid's auc: 0.801297
[3400]	train's auc: 0.881779	valid's auc: 0.801374
[3450]	train's auc: 0.882618	valid's auc: 0.801339
[3500]	train's auc: 0.883428	valid's auc: 0.801327
[3550]	train's auc: 0.884232	valid's auc: 0.801296
[3600]	train's auc: 0.885059	valid's auc: 0.801342
[3650]	train's auc: 0.88583	valid's auc: 0.801328
Early stopping, best iteration is:
[3395]	train's auc: 0.881688	valid's auc: 0.801377


fold : 4
[50]	train's auc: 0.771891	valid's auc: 0.758179
[100]	train's auc: 0.780248	valid's auc: 0.764389
[150]	train's auc: 0.786702	valid's auc: 0.769239
[200]	train's auc: 0.791281	valid's auc: 0.772818
[250]	train's auc: 0.795453	valid's auc: 0.775792
[300]	train's auc: 0.798838	valid's auc: 0.77795
[350]	train's auc: 0.801937	valid's auc: 0.77999
[400]	train's auc: 0.804572	valid's auc: 0.781428
[450]	train's auc: 0.807223	valid's auc: 0.783039
[500]	train's auc: 0.809653	valid's auc: 0.78429
[550]	train's auc: 0.81191	valid's auc: 0.785244
[600]	train's auc: 0.814039	valid's auc: 0.786233
[650]	train's auc: 0.816008	valid's auc: 0.787009
[700]	train's auc: 0.817926	valid's auc: 0.787676
[750]	train's auc: 0.819847	valid's auc: 0.788293
[800]	train's auc: 0.821736	valid's auc: 0.788956
[850]	train's auc: 0.823534	valid's auc: 0.789533
[900]	train's auc: 0.82526	valid's auc: 0.790062
[950]	train's auc: 0.826872	valid's auc: 0.790453
[1000]	train's auc: 0.828467	valid's auc: 0.79089
[1050]	train's auc: 0.830101	valid's auc: 0.79122
[1100]	train's auc: 0.831537	valid's auc: 0.791465
[1150]	train's auc: 0.833087	valid's auc: 0.791775
[1200]	train's auc: 0.834589	valid's auc: 0.792125
[1250]	train's auc: 0.83607	valid's auc: 0.792341
[1300]	train's auc: 0.837511	valid's auc: 0.792605
[1350]	train's auc: 0.838877	valid's auc: 0.792831
[1400]	train's auc: 0.840267	valid's auc: 0.793036
[1450]	train's auc: 0.841585	valid's auc: 0.793223
[1500]	train's auc: 0.842863	valid's auc: 0.7934
[1550]	train's auc: 0.844166	valid's auc: 0.793539
[1600]	train's auc: 0.845469	valid's auc: 0.793753
[1650]	train's auc: 0.846758	valid's auc: 0.793904
[1700]	train's auc: 0.847987	valid's auc: 0.794003
[1750]	train's auc: 0.849211	valid's auc: 0.794161
[1800]	train's auc: 0.850403	valid's auc: 0.794322
[1850]	train's auc: 0.851582	valid's auc: 0.794366
[1900]	train's auc: 0.852727	valid's auc: 0.794498
[1950]	train's auc: 0.853843	valid's auc: 0.7946
[2000]	train's auc: 0.855002	valid's auc: 0.794764
[2050]	train's auc: 0.856131	valid's auc: 0.794871
[2100]	train's auc: 0.857248	valid's auc: 0.794956
[2150]	train's auc: 0.858359	valid's auc: 0.795075
[2200]	train's auc: 0.859443	valid's auc: 0.795178
[2250]	train's auc: 0.860548	valid's auc: 0.795257
[2300]	train's auc: 0.861618	valid's auc: 0.795308
[2350]	train's auc: 0.862635	valid's auc: 0.795432
[2400]	train's auc: 0.863617	valid's auc: 0.795486
[2450]	train's auc: 0.864608	valid's auc: 0.795541
[2500]	train's auc: 0.865619	valid's auc: 0.795599
[2550]	train's auc: 0.866619	valid's auc: 0.795631
[2600]	train's auc: 0.86766	valid's auc: 0.79573
[2650]	train's auc: 0.868615	valid's auc: 0.795798
[2700]	train's auc: 0.869577	valid's auc: 0.795832
[2750]	train's auc: 0.870493	valid's auc: 0.795863
[2800]	train's auc: 0.871457	valid's auc: 0.795893
[2850]	train's auc: 0.872403	valid's auc: 0.795916
[2900]	train's auc: 0.873368	valid's auc: 0.795959
[2950]	train's auc: 0.874338	valid's auc: 0.796006
[3000]	train's auc: 0.875252	valid's auc: 0.795988
[3050]	train's auc: 0.876176	valid's auc: 0.795987
[3100]	train's auc: 0.877081	valid's auc: 0.79602
[3150]	train's auc: 0.877932	valid's auc: 0.796072
[3200]	train's auc: 0.878791	valid's auc: 0.796095
[3250]	train's auc: 0.879666	valid's auc: 0.796097
[3300]	train's auc: 0.880522	valid's auc: 0.796081
[3350]	train's auc: 0.881412	valid's auc: 0.79607
[3400]	train's auc: 0.882298	valid's auc: 0.796126
[3450]	train's auc: 0.88313	valid's auc: 0.796122
[3500]	train's auc: 0.883955	valid's auc: 0.796107
[3550]	train's auc: 0.88475	valid's auc: 0.796112
[3600]	train's auc: 0.885576	valid's auc: 0.796147
[3650]	train's auc: 0.886413	valid's auc: 0.796143
[3700]	train's auc: 0.88725	valid's auc: 0.796137
[3750]	train's auc: 0.888054	valid's auc: 0.796166
[3800]	train's auc: 0.888844	valid's auc: 0.796205
[3850]	train's auc: 0.889635	valid's auc: 0.796177
[3900]	train's auc: 0.890435	valid's auc: 0.796171
[3950]	train's auc: 0.891191	valid's auc: 0.796196
[4000]	train's auc: 0.891994	valid's auc: 0.796174
[4050]	train's auc: 0.892752	valid's auc: 0.796173
[4100]	train's auc: 0.893493	valid's auc: 0.796163
Early stopping, best iteration is:
[3809]	train's auc: 0.888998	valid's auc: 0.796208
Full AUC score 0.800331
"""
























