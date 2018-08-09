






useless_col = [

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
    # "NAME_EDUCATION_TYPE_Incomplete higher",
    # "OCCUPATION_TYPE_nan",
    # "OCCUPATION_TYPE_Laborers",
    # "OCCUPATION_TYPE_High skill tech staff",
    # "OCCUPATION_TYPE_Accountants",
    # "OCCUPATION_TYPE_Sales staff",
    "CNT_FAM_MEMBERS",
    # "OCCUPATION_TYPE_Low-skill Laborers",
    "FLAG_PHONE",
    # "NAME_EDUCATION_TYPE_Lower secondary",
    "FLAG_OWN_REALTY",
    # "OCCUPATION_TYPE_Medicine staff",
    # "OCCUPATION_TYPE_Cooking staff",
    # "OCCUPATION_TYPE_Core staff",
    # "OCCUPATION_TYPE_Cleaning staff",
    "FLAG_MOBIL",
    "FLAG_CONT_MOBILE",
    # "NAME_EDUCATION_TYPE_Academic degree",
    # "NAME_EDUCATION_TYPE_Higher education",
    # "NAME_EDUCATION_TYPE_Secondary / secondary special",
    # "NAME_EDUCATION_TYPE_nan",
    # "OCCUPATION_TYPE_HR staff",
    # "OCCUPATION_TYPE_IT staff",
    # "OCCUPATION_TYPE_Private service staff",
    # "OCCUPATION_TYPE_Realty agents",
    # "OCCUPATION_TYPE_Secretaries",
    # "OCCUPATION_TYPE_Security staff",
    # "OCCUPATION_TYPE_Waiters/barmen staff",

    'NAME_EDUCATION_TYPE',
    'ORGANIZATION_TYPE',
    'OCCUPATION_TYPE',
]


prev_drop_col = [
    "AMT_CREDIT"
]

bureau_drop_col = [
    "AMT_ANNUITY"
]


"""
[50]	train's auc: 0.769319	valid's auc: 0.758402
[100]	train's auc: 0.778136	valid's auc: 0.76561
[150]	train's auc: 0.785292	valid's auc: 0.771615
[200]	train's auc: 0.790554	valid's auc: 0.775687
[250]	train's auc: 0.794876	valid's auc: 0.779084
[300]	train's auc: 0.798265	valid's auc: 0.781442
[350]	train's auc: 0.801241	valid's auc: 0.782944
[400]	train's auc: 0.803992	valid's auc: 0.784641
[450]	train's auc: 0.806691	valid's auc: 0.786153
[500]	train's auc: 0.809116	valid's auc: 0.787257
[550]	train's auc: 0.811324	valid's auc: 0.788312
[600]	train's auc: 0.813491	valid's auc: 0.789222
[650]	train's auc: 0.81553	valid's auc: 0.790004
[700]	train's auc: 0.817522	valid's auc: 0.790778
[750]	train's auc: 0.819387	valid's auc: 0.791485
[800]	train's auc: 0.821294	valid's auc: 0.792125
[850]	train's auc: 0.823047	valid's auc: 0.792749
[900]	train's auc: 0.824825	valid's auc: 0.793227
[950]	train's auc: 0.8265	valid's auc: 0.793675
[1000]	train's auc: 0.828174	valid's auc: 0.794102
[1050]	train's auc: 0.829732	valid's auc: 0.79445
[1100]	train's auc: 0.831275	valid's auc: 0.794785
[1150]	train's auc: 0.832774	valid's auc: 0.795033
[1200]	train's auc: 0.834321	valid's auc: 0.79534
[1250]	train's auc: 0.835754	valid's auc: 0.795614
[1300]	train's auc: 0.837225	valid's auc: 0.795962
[1350]	train's auc: 0.838635	valid's auc: 0.796209
[1400]	train's auc: 0.840032	valid's auc: 0.796415
[1450]	train's auc: 0.841385	valid's auc: 0.796697
[1500]	train's auc: 0.842732	valid's auc: 0.796922
[1550]	train's auc: 0.84404	valid's auc: 0.797096
[1600]	train's auc: 0.845303	valid's auc: 0.797262
[1650]	train's auc: 0.846605	valid's auc: 0.797495
[1700]	train's auc: 0.847863	valid's auc: 0.797695
[1750]	train's auc: 0.84909	valid's auc: 0.79787
[1800]	train's auc: 0.850257	valid's auc: 0.798017
[1850]	train's auc: 0.851418	valid's auc: 0.798155
[1900]	train's auc: 0.852615	valid's auc: 0.798282
[1950]	train's auc: 0.853754	valid's auc: 0.798363
[2000]	train's auc: 0.854911	valid's auc: 0.798502
[2050]	train's auc: 0.856003	valid's auc: 0.798611
[2100]	train's auc: 0.857073	valid's auc: 0.798713
[2150]	train's auc: 0.858189	valid's auc: 0.798832
[2200]	train's auc: 0.859262	valid's auc: 0.798953
[2250]	train's auc: 0.860333	valid's auc: 0.799014
[2300]	train's auc: 0.861408	valid's auc: 0.799133
[2350]	train's auc: 0.862469	valid's auc: 0.799191
[2400]	train's auc: 0.863489	valid's auc: 0.799227
[2450]	train's auc: 0.864507	valid's auc: 0.79927
[2500]	train's auc: 0.865494	valid's auc: 0.799312
[2550]	train's auc: 0.866474	valid's auc: 0.799376
[2600]	train's auc: 0.867444	valid's auc: 0.799445
[2650]	train's auc: 0.868413	valid's auc: 0.799518
[2700]	train's auc: 0.869361	valid's auc: 0.79958
[2750]	train's auc: 0.87033	valid's auc: 0.799588
[2800]	train's auc: 0.871284	valid's auc: 0.799637
[2850]	train's auc: 0.872249	valid's auc: 0.7997
[2900]	train's auc: 0.873204	valid's auc: 0.799768
[2950]	train's auc: 0.87413	valid's auc: 0.799796
[3000]	train's auc: 0.874988	valid's auc: 0.799815
[3050]	train's auc: 0.875857	valid's auc: 0.799812
[3100]	train's auc: 0.87679	valid's auc: 0.799856
[3150]	train's auc: 0.877669	valid's auc: 0.799899
[3200]	train's auc: 0.878566	valid's auc: 0.799897
[3250]	train's auc: 0.879413	valid's auc: 0.799906
[3300]	train's auc: 0.880226	valid's auc: 0.799901
[3350]	train's auc: 0.88109	valid's auc: 0.799896
[3400]	train's auc: 0.88196	valid's auc: 0.799942
[3450]	train's auc: 0.882826	valid's auc: 0.799961
[3500]	train's auc: 0.883659	valid's auc: 0.799941
[3550]	train's auc: 0.884489	valid's auc: 0.799933
[3600]	train's auc: 0.8853	valid's auc: 0.79995
[3650]	train's auc: 0.886112	valid's auc: 0.799941
[3700]	train's auc: 0.886899	valid's auc: 0.799956
[3750]	train's auc: 0.887768	valid's auc: 0.799972
[3800]	train's auc: 0.888557	valid's auc: 0.79998
[3850]	train's auc: 0.889367	valid's auc: 0.799956
[3900]	train's auc: 0.890165	valid's auc: 0.799978
[3950]	train's auc: 0.890966	valid's auc: 0.799979
[4000]	train's auc: 0.891706	valid's auc: 0.799996
[4050]	train's auc: 0.892415	valid's auc: 0.800019
[4100]	train's auc: 0.89313	valid's auc: 0.799966
[4150]	train's auc: 0.893895	valid's auc: 0.800002
[4200]	train's auc: 0.894673	valid's auc: 0.79995
[4250]	train's auc: 0.895441	valid's auc: 0.799916
[4300]	train's auc: 0.896166	valid's auc: 0.799968
Early stopping, best iteration is:
[4035]	train's auc: 0.892192	valid's auc: 0.800022



fold : 1
[50]	train's auc: 0.76971	valid's auc: 0.755317
[100]	train's auc: 0.778456	valid's auc: 0.763511
[150]	train's auc: 0.785672	valid's auc: 0.769923
[200]	train's auc: 0.790636	valid's auc: 0.77401
[250]	train's auc: 0.794853	valid's auc: 0.777336
[300]	train's auc: 0.798282	valid's auc: 0.779654
[350]	train's auc: 0.801099	valid's auc: 0.781343
[400]	train's auc: 0.803875	valid's auc: 0.783135
[450]	train's auc: 0.806478	valid's auc: 0.784871
[500]	train's auc: 0.808896	valid's auc: 0.786175
[550]	train's auc: 0.811067	valid's auc: 0.787245
[600]	train's auc: 0.813198	valid's auc: 0.788232
[650]	train's auc: 0.815225	valid's auc: 0.789107
[700]	train's auc: 0.817203	valid's auc: 0.789925
[750]	train's auc: 0.819075	valid's auc: 0.790742
[800]	train's auc: 0.820946	valid's auc: 0.791516
[850]	train's auc: 0.8227	valid's auc: 0.792066
[900]	train's auc: 0.824467	valid's auc: 0.792599
[950]	train's auc: 0.826139	valid's auc: 0.793129
[1000]	train's auc: 0.827777	valid's auc: 0.79359
[1050]	train's auc: 0.829306	valid's auc: 0.79401
[1100]	train's auc: 0.830847	valid's auc: 0.794382
[1150]	train's auc: 0.832339	valid's auc: 0.794663
[1200]	train's auc: 0.833864	valid's auc: 0.795047
[1250]	train's auc: 0.835303	valid's auc: 0.795318
[1300]	train's auc: 0.836747	valid's auc: 0.79559
[1350]	train's auc: 0.838184	valid's auc: 0.795889
[1400]	train's auc: 0.839543	valid's auc: 0.796129
[1450]	train's auc: 0.84091	valid's auc: 0.796384
[1500]	train's auc: 0.842274	valid's auc: 0.796564
[1550]	train's auc: 0.843552	valid's auc: 0.796738
[1600]	train's auc: 0.844807	valid's auc: 0.796914
[1650]	train's auc: 0.846086	valid's auc: 0.797086
[1700]	train's auc: 0.847341	valid's auc: 0.797254
[1750]	train's auc: 0.848622	valid's auc: 0.797438
[1800]	train's auc: 0.849848	valid's auc: 0.797601
[1850]	train's auc: 0.851013	valid's auc: 0.797738
[1900]	train's auc: 0.852145	valid's auc: 0.797921
[1950]	train's auc: 0.853347	valid's auc: 0.798009
[2000]	train's auc: 0.854483	valid's auc: 0.798091
[2050]	train's auc: 0.855607	valid's auc: 0.798194
[2100]	train's auc: 0.85666	valid's auc: 0.798292
[2150]	train's auc: 0.857793	valid's auc: 0.798398
[2200]	train's auc: 0.858902	valid's auc: 0.798507
[2250]	train's auc: 0.859939	valid's auc: 0.798666
[2300]	train's auc: 0.861002	valid's auc: 0.798733
[2350]	train's auc: 0.861998	valid's auc: 0.798842
[2400]	train's auc: 0.863025	valid's auc: 0.798898
[2450]	train's auc: 0.864057	valid's auc: 0.79897
[2500]	train's auc: 0.865086	valid's auc: 0.799009
[2550]	train's auc: 0.866035	valid's auc: 0.799068
[2600]	train's auc: 0.867045	valid's auc: 0.799125
[2650]	train's auc: 0.868016	valid's auc: 0.799173
[2700]	train's auc: 0.868997	valid's auc: 0.79927
[2750]	train's auc: 0.869903	valid's auc: 0.799298
[2800]	train's auc: 0.870799	valid's auc: 0.799387
[2850]	train's auc: 0.871804	valid's auc: 0.799403
[2900]	train's auc: 0.872773	valid's auc: 0.799419
[2950]	train's auc: 0.873714	valid's auc: 0.799489
[3000]	train's auc: 0.874634	valid's auc: 0.799533
[3050]	train's auc: 0.875493	valid's auc: 0.799566
[3100]	train's auc: 0.876386	valid's auc: 0.79961
[3150]	train's auc: 0.877254	valid's auc: 0.799672
[3200]	train's auc: 0.878116	valid's auc: 0.799703
[3250]	train's auc: 0.879038	valid's auc: 0.799755
[3300]	train's auc: 0.879884	valid's auc: 0.799777
[3350]	train's auc: 0.880747	valid's auc: 0.799823
[3400]	train's auc: 0.881608	valid's auc: 0.799851
[3450]	train's auc: 0.882442	valid's auc: 0.799926
[3500]	train's auc: 0.883306	valid's auc: 0.799908
[3550]	train's auc: 0.884146	valid's auc: 0.799936
[3600]	train's auc: 0.88496	valid's auc: 0.799924
[3650]	train's auc: 0.885746	valid's auc: 0.799964
[3700]	train's auc: 0.886569	valid's auc: 0.799949
[3750]	train's auc: 0.887409	valid's auc: 0.799979
[3800]	train's auc: 0.888182	valid's auc: 0.799997
[3850]	train's auc: 0.888954	valid's auc: 0.800015
[3900]	train's auc: 0.889759	valid's auc: 0.800026
[3950]	train's auc: 0.890574	valid's auc: 0.800039
[4000]	train's auc: 0.891354	valid's auc: 0.800039
[4050]	train's auc: 0.892121	valid's auc: 0.800046
[4100]	train's auc: 0.892872	valid's auc: 0.800047
[4150]	train's auc: 0.893627	valid's auc: 0.800055
[4200]	train's auc: 0.894433	valid's auc: 0.800051
[4250]	train's auc: 0.895159	valid's auc: 0.80007
[4300]	train's auc: 0.895892	valid's auc: 0.800056
[4350]	train's auc: 0.89664	valid's auc: 0.800044
[4400]	train's auc: 0.897349	valid's auc: 0.800079
[4450]	train's auc: 0.898096	valid's auc: 0.800089
[4500]	train's auc: 0.898849	valid's auc: 0.800087
[4550]	train's auc: 0.899518	valid's auc: 0.800116
[4600]	train's auc: 0.90022	valid's auc: 0.800116
[4650]	train's auc: 0.900951	valid's auc: 0.800078
[4700]	train's auc: 0.90167	valid's auc: 0.800081
[4750]	train's auc: 0.902319	valid's auc: 0.800088
[4800]	train's auc: 0.903022	valid's auc: 0.800093
[4850]	train's auc: 0.903721	valid's auc: 0.800053
[4900]	train's auc: 0.904404	valid's auc: 0.800048
Early stopping, best iteration is:
[4608]	train's auc: 0.900335	valid's auc: 0.800124


fold : 2
[50]	train's auc: 0.769938	valid's auc: 0.754128
[100]	train's auc: 0.777985	valid's auc: 0.762227
[150]	train's auc: 0.78516	valid's auc: 0.769131
[200]	train's auc: 0.790287	valid's auc: 0.773614
[250]	train's auc: 0.794487	valid's auc: 0.777404
[300]	train's auc: 0.797777	valid's auc: 0.779918
[350]	train's auc: 0.80066	valid's auc: 0.781833
[400]	train's auc: 0.803385	valid's auc: 0.783654
[450]	train's auc: 0.806023	valid's auc: 0.785409
[500]	train's auc: 0.80844	valid's auc: 0.786786
[550]	train's auc: 0.810661	valid's auc: 0.788005
[600]	train's auc: 0.812848	valid's auc: 0.789234
[650]	train's auc: 0.814881	valid's auc: 0.790182
[700]	train's auc: 0.816862	valid's auc: 0.791073
[750]	train's auc: 0.818724	valid's auc: 0.79181
[800]	train's auc: 0.820611	valid's auc: 0.792621
[850]	train's auc: 0.822417	valid's auc: 0.793336
[900]	train's auc: 0.824173	valid's auc: 0.793984
[950]	train's auc: 0.825832	valid's auc: 0.794449
[1000]	train's auc: 0.827491	valid's auc: 0.794918
[1050]	train's auc: 0.829009	valid's auc: 0.795318
[1100]	train's auc: 0.83058	valid's auc: 0.795814
[1150]	train's auc: 0.832069	valid's auc: 0.796175
[1200]	train's auc: 0.833654	valid's auc: 0.796604
[1250]	train's auc: 0.835118	valid's auc: 0.796876
[1300]	train's auc: 0.836562	valid's auc: 0.797177
[1350]	train's auc: 0.837924	valid's auc: 0.79747
[1400]	train's auc: 0.839302	valid's auc: 0.7977
[1450]	train's auc: 0.840646	valid's auc: 0.797947
[1500]	train's auc: 0.842011	valid's auc: 0.798159
[1550]	train's auc: 0.843331	valid's auc: 0.798355
[1600]	train's auc: 0.844604	valid's auc: 0.798563
[1650]	train's auc: 0.845899	valid's auc: 0.798729
[1700]	train's auc: 0.847187	valid's auc: 0.798921
[1750]	train's auc: 0.848457	valid's auc: 0.799112
[1800]	train's auc: 0.849668	valid's auc: 0.799226
[1850]	train's auc: 0.850843	valid's auc: 0.79929
[1900]	train's auc: 0.852008	valid's auc: 0.799426
[1950]	train's auc: 0.853176	valid's auc: 0.799581
[2000]	train's auc: 0.85428	valid's auc: 0.799753
[2050]	train's auc: 0.855395	valid's auc: 0.79985
[2100]	train's auc: 0.856485	valid's auc: 0.799898
[2150]	train's auc: 0.857622	valid's auc: 0.800014
[2200]	train's auc: 0.858685	valid's auc: 0.8001
[2250]	train's auc: 0.859709	valid's auc: 0.80023
[2300]	train's auc: 0.860744	valid's auc: 0.800335
[2350]	train's auc: 0.861717	valid's auc: 0.80043
[2400]	train's auc: 0.862721	valid's auc: 0.800461
[2450]	train's auc: 0.863755	valid's auc: 0.800581
[2500]	train's auc: 0.864734	valid's auc: 0.80062
[2550]	train's auc: 0.865716	valid's auc: 0.800665
[2600]	train's auc: 0.866686	valid's auc: 0.800669
[2650]	train's auc: 0.867675	valid's auc: 0.800687
[2700]	train's auc: 0.868636	valid's auc: 0.80075
[2750]	train's auc: 0.869561	valid's auc: 0.800824
[2800]	train's auc: 0.870452	valid's auc: 0.800864
[2850]	train's auc: 0.871417	valid's auc: 0.800899
[2900]	train's auc: 0.872337	valid's auc: 0.800903
[2950]	train's auc: 0.873231	valid's auc: 0.800914
[3000]	train's auc: 0.874116	valid's auc: 0.800951
[3050]	train's auc: 0.874963	valid's auc: 0.800944
[3100]	train's auc: 0.87586	valid's auc: 0.800953
[3150]	train's auc: 0.876775	valid's auc: 0.800976
[3200]	train's auc: 0.877605	valid's auc: 0.80103
[3250]	train's auc: 0.878483	valid's auc: 0.801119
[3300]	train's auc: 0.879336	valid's auc: 0.801117
[3350]	train's auc: 0.880224	valid's auc: 0.801195
[3400]	train's auc: 0.881085	valid's auc: 0.801219
[3450]	train's auc: 0.881896	valid's auc: 0.801208
[3500]	train's auc: 0.882735	valid's auc: 0.801236
[3550]	train's auc: 0.883559	valid's auc: 0.801215
[3600]	train's auc: 0.884349	valid's auc: 0.801229
[3650]	train's auc: 0.885161	valid's auc: 0.801243
[3700]	train's auc: 0.885923	valid's auc: 0.801233
[3750]	train's auc: 0.886723	valid's auc: 0.801243
[3800]	train's auc: 0.887548	valid's auc: 0.801232
[3850]	train's auc: 0.888334	valid's auc: 0.80123
[3900]	train's auc: 0.889079	valid's auc: 0.801216
[3950]	train's auc: 0.889851	valid's auc: 0.801221
[4000]	train's auc: 0.890582	valid's auc: 0.801251
Early stopping, best iteration is:
[3731]	train's auc: 0.886436	valid's auc: 0.801268


fold : 3
[50]	train's auc: 0.76948	valid's auc: 0.764315
[100]	train's auc: 0.778187	valid's auc: 0.77138
[150]	train's auc: 0.785417	valid's auc: 0.777134
[200]	train's auc: 0.790653	valid's auc: 0.780739
[250]	train's auc: 0.794898	valid's auc: 0.783505
[300]	train's auc: 0.798268	valid's auc: 0.785481
[350]	train's auc: 0.801113	valid's auc: 0.786856
[400]	train's auc: 0.803939	valid's auc: 0.788319
[450]	train's auc: 0.806548	valid's auc: 0.789538
[500]	train's auc: 0.80893	valid's auc: 0.790673
[550]	train's auc: 0.811099	valid's auc: 0.791541
[600]	train's auc: 0.813229	valid's auc: 0.792348
[650]	train's auc: 0.81524	valid's auc: 0.792883
[700]	train's auc: 0.817181	valid's auc: 0.793517
[750]	train's auc: 0.819059	valid's auc: 0.794082
[800]	train's auc: 0.821013	valid's auc: 0.794643
[850]	train's auc: 0.822807	valid's auc: 0.795161
[900]	train's auc: 0.824576	valid's auc: 0.795571
[950]	train's auc: 0.826218	valid's auc: 0.795922
[1000]	train's auc: 0.827903	valid's auc: 0.796326
[1050]	train's auc: 0.829435	valid's auc: 0.796605
[1100]	train's auc: 0.831023	valid's auc: 0.796904
[1150]	train's auc: 0.832525	valid's auc: 0.797134
[1200]	train's auc: 0.834086	valid's auc: 0.797396
[1250]	train's auc: 0.835547	valid's auc: 0.797629
[1300]	train's auc: 0.83704	valid's auc: 0.797875
[1350]	train's auc: 0.838455	valid's auc: 0.798039
[1400]	train's auc: 0.839869	valid's auc: 0.798163
[1450]	train's auc: 0.841238	valid's auc: 0.798411
[1500]	train's auc: 0.842605	valid's auc: 0.798527
[1550]	train's auc: 0.843938	valid's auc: 0.79864
[1600]	train's auc: 0.845189	valid's auc: 0.798851
[1650]	train's auc: 0.84651	valid's auc: 0.799005
[1700]	train's auc: 0.847804	valid's auc: 0.799189
[1750]	train's auc: 0.849036	valid's auc: 0.7993
[1800]	train's auc: 0.850264	valid's auc: 0.799366
[1850]	train's auc: 0.85147	valid's auc: 0.799384
[1900]	train's auc: 0.852657	valid's auc: 0.799474
[1950]	train's auc: 0.85385	valid's auc: 0.799603
[2000]	train's auc: 0.855039	valid's auc: 0.799686
[2050]	train's auc: 0.85616	valid's auc: 0.799747
[2100]	train's auc: 0.857256	valid's auc: 0.799847
[2150]	train's auc: 0.858378	valid's auc: 0.799893
[2200]	train's auc: 0.85946	valid's auc: 0.799998
[2250]	train's auc: 0.860528	valid's auc: 0.800094
[2300]	train's auc: 0.861642	valid's auc: 0.800173
[2350]	train's auc: 0.862688	valid's auc: 0.800168
[2400]	train's auc: 0.863715	valid's auc: 0.800158
[2450]	train's auc: 0.864785	valid's auc: 0.800182
[2500]	train's auc: 0.865818	valid's auc: 0.800201
[2550]	train's auc: 0.866786	valid's auc: 0.800278
[2600]	train's auc: 0.867751	valid's auc: 0.800307
[2650]	train's auc: 0.868731	valid's auc: 0.800388
[2700]	train's auc: 0.869742	valid's auc: 0.800431
[2750]	train's auc: 0.870715	valid's auc: 0.800438
[2800]	train's auc: 0.871649	valid's auc: 0.800425
[2850]	train's auc: 0.872639	valid's auc: 0.800464
[2900]	train's auc: 0.873558	valid's auc: 0.800498
[2950]	train's auc: 0.874491	valid's auc: 0.800534
[3000]	train's auc: 0.87541	valid's auc: 0.800583
[3050]	train's auc: 0.876287	valid's auc: 0.800577
[3100]	train's auc: 0.877151	valid's auc: 0.800657
[3150]	train's auc: 0.878038	valid's auc: 0.800662
[3200]	train's auc: 0.878923	valid's auc: 0.800714
[3250]	train's auc: 0.87984	valid's auc: 0.800722
[3300]	train's auc: 0.880694	valid's auc: 0.800775
[3350]	train's auc: 0.881542	valid's auc: 0.800787
[3400]	train's auc: 0.882437	valid's auc: 0.800807
[3450]	train's auc: 0.883283	valid's auc: 0.800787
[3500]	train's auc: 0.884128	valid's auc: 0.800768
[3550]	train's auc: 0.884938	valid's auc: 0.800765
[3600]	train's auc: 0.885749	valid's auc: 0.800796
[3650]	train's auc: 0.886599	valid's auc: 0.800793
[3700]	train's auc: 0.88737	valid's auc: 0.800762
Early stopping, best iteration is:
[3426]	train's auc: 0.882899	valid's auc: 0.800829


fold : 4
[50]	train's auc: 0.770347	valid's auc: 0.757142
[100]	train's auc: 0.779508	valid's auc: 0.76415
[150]	train's auc: 0.78647	valid's auc: 0.769581
[200]	train's auc: 0.791767	valid's auc: 0.773188
[250]	train's auc: 0.796121	valid's auc: 0.776189
[300]	train's auc: 0.799502	valid's auc: 0.778353
[350]	train's auc: 0.802334	valid's auc: 0.779726
[400]	train's auc: 0.804976	valid's auc: 0.781294
[450]	train's auc: 0.807602	valid's auc: 0.782653
[500]	train's auc: 0.810018	valid's auc: 0.78383
[550]	train's auc: 0.812154	valid's auc: 0.784778
[600]	train's auc: 0.814262	valid's auc: 0.785734
[650]	train's auc: 0.816235	valid's auc: 0.78642
[700]	train's auc: 0.818121	valid's auc: 0.787099
[750]	train's auc: 0.819969	valid's auc: 0.787702
[800]	train's auc: 0.821826	valid's auc: 0.788295
[850]	train's auc: 0.823574	valid's auc: 0.788805
[900]	train's auc: 0.825317	valid's auc: 0.789226
[950]	train's auc: 0.826949	valid's auc: 0.789586
[1000]	train's auc: 0.828642	valid's auc: 0.790071
[1050]	train's auc: 0.830186	valid's auc: 0.790337
[1100]	train's auc: 0.831758	valid's auc: 0.790632
[1150]	train's auc: 0.833283	valid's auc: 0.791021
[1200]	train's auc: 0.834791	valid's auc: 0.791307
[1250]	train's auc: 0.836246	valid's auc: 0.791574
[1300]	train's auc: 0.837723	valid's auc: 0.791828
[1350]	train's auc: 0.839116	valid's auc: 0.792048
[1400]	train's auc: 0.840444	valid's auc: 0.792289
[1450]	train's auc: 0.841818	valid's auc: 0.79248
[1500]	train's auc: 0.843203	valid's auc: 0.792664
[1550]	train's auc: 0.844493	valid's auc: 0.792832
[1600]	train's auc: 0.845733	valid's auc: 0.792947
[1650]	train's auc: 0.84701	valid's auc: 0.793122
[1700]	train's auc: 0.848233	valid's auc: 0.79326
[1750]	train's auc: 0.849426	valid's auc: 0.793395
[1800]	train's auc: 0.850661	valid's auc: 0.793507
[1850]	train's auc: 0.851838	valid's auc: 0.793637
[1900]	train's auc: 0.853052	valid's auc: 0.793786
[1950]	train's auc: 0.85421	valid's auc: 0.793943
[2000]	train's auc: 0.855332	valid's auc: 0.794072
[2050]	train's auc: 0.85647	valid's auc: 0.794182
[2100]	train's auc: 0.857543	valid's auc: 0.794303
[2150]	train's auc: 0.858644	valid's auc: 0.794353
[2200]	train's auc: 0.859714	valid's auc: 0.794469
[2250]	train's auc: 0.860756	valid's auc: 0.794565
[2300]	train's auc: 0.861796	valid's auc: 0.794613
[2350]	train's auc: 0.862785	valid's auc: 0.794712
[2400]	train's auc: 0.863828	valid's auc: 0.794758
[2450]	train's auc: 0.864863	valid's auc: 0.794778
[2500]	train's auc: 0.865817	valid's auc: 0.794847
[2550]	train's auc: 0.866751	valid's auc: 0.794887
[2600]	train's auc: 0.867705	valid's auc: 0.794925
[2650]	train's auc: 0.86869	valid's auc: 0.794963
[2700]	train's auc: 0.869654	valid's auc: 0.795044
[2750]	train's auc: 0.870626	valid's auc: 0.795029
[2800]	train's auc: 0.87158	valid's auc: 0.795073
[2850]	train's auc: 0.872545	valid's auc: 0.795149
[2900]	train's auc: 0.87351	valid's auc: 0.795199
[2950]	train's auc: 0.87441	valid's auc: 0.795251
[3000]	train's auc: 0.875327	valid's auc: 0.795247
[3050]	train's auc: 0.876211	valid's auc: 0.7953
[3100]	train's auc: 0.877185	valid's auc: 0.795295
[3150]	train's auc: 0.878098	valid's auc: 0.795348
[3200]	train's auc: 0.878972	valid's auc: 0.795374
[3250]	train's auc: 0.879837	valid's auc: 0.7954
[3300]	train's auc: 0.880715	valid's auc: 0.795452
[3350]	train's auc: 0.88155	valid's auc: 0.795444
[3400]	train's auc: 0.882425	valid's auc: 0.795512
[3450]	train's auc: 0.8833	valid's auc: 0.795532
[3500]	train's auc: 0.884085	valid's auc: 0.795505
[3550]	train's auc: 0.884906	valid's auc: 0.79551
[3600]	train's auc: 0.885752	valid's auc: 0.795554
[3650]	train's auc: 0.886576	valid's auc: 0.795585
[3700]	train's auc: 0.88734	valid's auc: 0.795597
[3750]	train's auc: 0.888167	valid's auc: 0.795604
[3800]	train's auc: 0.888953	valid's auc: 0.795643
[3850]	train's auc: 0.889785	valid's auc: 0.795645
[3900]	train's auc: 0.890559	valid's auc: 0.795672
[3950]	train's auc: 0.891384	valid's auc: 0.79563
[4000]	train's auc: 0.892162	valid's auc: 0.795621
[4050]	train's auc: 0.892883	valid's auc: 0.795631
[4100]	train's auc: 0.893613	valid's auc: 0.795618
[4150]	train's auc: 0.894368	valid's auc: 0.795636
Early stopping, best iteration is:
[3891]	train's auc: 0.89042	valid's auc: 0.795681
Full AUC score 0.799537
"""
























