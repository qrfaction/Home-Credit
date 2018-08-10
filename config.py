






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
[50]	train's auc: 0.758266	valid's auc: 0.745831
[100]	train's auc: 0.774093	valid's auc: 0.760655
[150]	train's auc: 0.782997	valid's auc: 0.768294
[200]	train's auc: 0.788513	valid's auc: 0.772985
[250]	train's auc: 0.793205	valid's auc: 0.776777
[300]	train's auc: 0.796953	valid's auc: 0.779518
[350]	train's auc: 0.80049	valid's auc: 0.782242
[400]	train's auc: 0.80354	valid's auc: 0.784172
[450]	train's auc: 0.806388	valid's auc: 0.785673
[500]	train's auc: 0.808789	valid's auc: 0.786924
[550]	train's auc: 0.811096	valid's auc: 0.788118
[600]	train's auc: 0.813335	valid's auc: 0.78888
[650]	train's auc: 0.815443	valid's auc: 0.789676
[700]	train's auc: 0.817416	valid's auc: 0.790568
[750]	train's auc: 0.819367	valid's auc: 0.791302
[800]	train's auc: 0.82128	valid's auc: 0.792089
[850]	train's auc: 0.823175	valid's auc: 0.79271
[900]	train's auc: 0.824904	valid's auc: 0.793164
[950]	train's auc: 0.826596	valid's auc: 0.793658
[1000]	train's auc: 0.828323	valid's auc: 0.794141
[1050]	train's auc: 0.829895	valid's auc: 0.794589
[1100]	train's auc: 0.831485	valid's auc: 0.795018
[1150]	train's auc: 0.833033	valid's auc: 0.795365
[1200]	train's auc: 0.834537	valid's auc: 0.795704
[1250]	train's auc: 0.835994	valid's auc: 0.796092
[1300]	train's auc: 0.837458	valid's auc: 0.796372
[1350]	train's auc: 0.838856	valid's auc: 0.796598
[1400]	train's auc: 0.840226	valid's auc: 0.796904
[1450]	train's auc: 0.841619	valid's auc: 0.797132
[1500]	train's auc: 0.842952	valid's auc: 0.797282
[1550]	train's auc: 0.844246	valid's auc: 0.79751
[1600]	train's auc: 0.845523	valid's auc: 0.797677
[1650]	train's auc: 0.846803	valid's auc: 0.797828
[1700]	train's auc: 0.848007	valid's auc: 0.797943
[1750]	train's auc: 0.849259	valid's auc: 0.798094
[1800]	train's auc: 0.85047	valid's auc: 0.798238
[1850]	train's auc: 0.851693	valid's auc: 0.79842
[1900]	train's auc: 0.852911	valid's auc: 0.798562
[1950]	train's auc: 0.854033	valid's auc: 0.79867
[2000]	train's auc: 0.855211	valid's auc: 0.798819
[2050]	train's auc: 0.856359	valid's auc: 0.798918
[2100]	train's auc: 0.857447	valid's auc: 0.79908
[2150]	train's auc: 0.858554	valid's auc: 0.799209
[2200]	train's auc: 0.859645	valid's auc: 0.799321
[2250]	train's auc: 0.86073	valid's auc: 0.799454
[2300]	train's auc: 0.861824	valid's auc: 0.799601
[2350]	train's auc: 0.86291	valid's auc: 0.799678
[2400]	train's auc: 0.863953	valid's auc: 0.79974
[2450]	train's auc: 0.86496	valid's auc: 0.799758
[2500]	train's auc: 0.865979	valid's auc: 0.799824
[2550]	train's auc: 0.86693	valid's auc: 0.799935
[2600]	train's auc: 0.867981	valid's auc: 0.800001
[2650]	train's auc: 0.868978	valid's auc: 0.800089
[2700]	train's auc: 0.869901	valid's auc: 0.800134
[2750]	train's auc: 0.87089	valid's auc: 0.800103
[2800]	train's auc: 0.87187	valid's auc: 0.800139
[2850]	train's auc: 0.872807	valid's auc: 0.80016
[2900]	train's auc: 0.873754	valid's auc: 0.800202
[2950]	train's auc: 0.874708	valid's auc: 0.800219
[3000]	train's auc: 0.875683	valid's auc: 0.800296
[3050]	train's auc: 0.876621	valid's auc: 0.800295
[3100]	train's auc: 0.877528	valid's auc: 0.800297
[3150]	train's auc: 0.878452	valid's auc: 0.800343
[3200]	train's auc: 0.879307	valid's auc: 0.800359
[3250]	train's auc: 0.880228	valid's auc: 0.800387
[3300]	train's auc: 0.881098	valid's auc: 0.800415
[3350]	train's auc: 0.881986	valid's auc: 0.800409
[3400]	train's auc: 0.882845	valid's auc: 0.800436
[3450]	train's auc: 0.883705	valid's auc: 0.800476
[3500]	train's auc: 0.884511	valid's auc: 0.8005
[3550]	train's auc: 0.885361	valid's auc: 0.800547
[3600]	train's auc: 0.886166	valid's auc: 0.800553
[3650]	train's auc: 0.886989	valid's auc: 0.800558
[3700]	train's auc: 0.887757	valid's auc: 0.800538
[3750]	train's auc: 0.888567	valid's auc: 0.800559
[3800]	train's auc: 0.889362	valid's auc: 0.800612
[3850]	train's auc: 0.890175	valid's auc: 0.800646
[3900]	train's auc: 0.891054	valid's auc: 0.800628
[3950]	train's auc: 0.891834	valid's auc: 0.800622
[4000]	train's auc: 0.892641	valid's auc: 0.800589
[4050]	train's auc: 0.893391	valid's auc: 0.800589
[4100]	train's auc: 0.89417	valid's auc: 0.800578
[4150]	train's auc: 0.894908	valid's auc: 0.800587
Early stopping, best iteration is:
[3859]	train's auc: 0.890316	valid's auc: 0.800653


fold : 1
[50]	train's auc: 0.758702	valid's auc: 0.746111
[100]	train's auc: 0.77459	valid's auc: 0.759975
[150]	train's auc: 0.78319	valid's auc: 0.767516
[200]	train's auc: 0.788778	valid's auc: 0.77222
[250]	train's auc: 0.793382	valid's auc: 0.776096
[300]	train's auc: 0.797164	valid's auc: 0.778942
[350]	train's auc: 0.800616	valid's auc: 0.781429
[400]	train's auc: 0.80357	valid's auc: 0.783353
[450]	train's auc: 0.806251	valid's auc: 0.784843
[500]	train's auc: 0.808603	valid's auc: 0.786175
[550]	train's auc: 0.810924	valid's auc: 0.787387
[600]	train's auc: 0.813103	valid's auc: 0.788292
[650]	train's auc: 0.81518	valid's auc: 0.789148
[700]	train's auc: 0.817182	valid's auc: 0.790071
[750]	train's auc: 0.819182	valid's auc: 0.790969
[800]	train's auc: 0.821073	valid's auc: 0.791674
[850]	train's auc: 0.8229	valid's auc: 0.792277
[900]	train's auc: 0.824672	valid's auc: 0.792917
[950]	train's auc: 0.826332	valid's auc: 0.793499
[1000]	train's auc: 0.828039	valid's auc: 0.793979
[1050]	train's auc: 0.829628	valid's auc: 0.794429
[1100]	train's auc: 0.83123	valid's auc: 0.794862
[1150]	train's auc: 0.832779	valid's auc: 0.795182
[1200]	train's auc: 0.834222	valid's auc: 0.795446
[1250]	train's auc: 0.835705	valid's auc: 0.795737
[1300]	train's auc: 0.837149	valid's auc: 0.796003
[1350]	train's auc: 0.838515	valid's auc: 0.796258
[1400]	train's auc: 0.83995	valid's auc: 0.796583
[1450]	train's auc: 0.841321	valid's auc: 0.796837
[1500]	train's auc: 0.842669	valid's auc: 0.797046
[1550]	train's auc: 0.843958	valid's auc: 0.797256
[1600]	train's auc: 0.845257	valid's auc: 0.797464
[1650]	train's auc: 0.846554	valid's auc: 0.797601
[1700]	train's auc: 0.847761	valid's auc: 0.79774
[1750]	train's auc: 0.848975	valid's auc: 0.79787
[1800]	train's auc: 0.850209	valid's auc: 0.79805
[1850]	train's auc: 0.851351	valid's auc: 0.798212
[1900]	train's auc: 0.852601	valid's auc: 0.798344
[1950]	train's auc: 0.853785	valid's auc: 0.798452
[2000]	train's auc: 0.854962	valid's auc: 0.798533
[2050]	train's auc: 0.856116	valid's auc: 0.798672
[2100]	train's auc: 0.857224	valid's auc: 0.798817
[2150]	train's auc: 0.858327	valid's auc: 0.798952
[2200]	train's auc: 0.859404	valid's auc: 0.799009
[2250]	train's auc: 0.860528	valid's auc: 0.799141
[2300]	train's auc: 0.861596	valid's auc: 0.799194
[2350]	train's auc: 0.862661	valid's auc: 0.799272
[2400]	train's auc: 0.863673	valid's auc: 0.799357
[2450]	train's auc: 0.864667	valid's auc: 0.799386
[2500]	train's auc: 0.865684	valid's auc: 0.799424
[2550]	train's auc: 0.866639	valid's auc: 0.799493
[2600]	train's auc: 0.867619	valid's auc: 0.799526
[2650]	train's auc: 0.868609	valid's auc: 0.799604
[2700]	train's auc: 0.86958	valid's auc: 0.799665
[2750]	train's auc: 0.870533	valid's auc: 0.799762
[2800]	train's auc: 0.871497	valid's auc: 0.799843
[2850]	train's auc: 0.872469	valid's auc: 0.799915
[2900]	train's auc: 0.873372	valid's auc: 0.799949
[2950]	train's auc: 0.874331	valid's auc: 0.799982
[3000]	train's auc: 0.875258	valid's auc: 0.800069
[3050]	train's auc: 0.876206	valid's auc: 0.800093
[3100]	train's auc: 0.877078	valid's auc: 0.80014
[3150]	train's auc: 0.878045	valid's auc: 0.800226
[3200]	train's auc: 0.878973	valid's auc: 0.800262
[3250]	train's auc: 0.879933	valid's auc: 0.800333
[3300]	train's auc: 0.880812	valid's auc: 0.800346
[3350]	train's auc: 0.88167	valid's auc: 0.800384
[3400]	train's auc: 0.882537	valid's auc: 0.800391
[3450]	train's auc: 0.883385	valid's auc: 0.800381
[3500]	train's auc: 0.884246	valid's auc: 0.800421
[3550]	train's auc: 0.885076	valid's auc: 0.800489
[3600]	train's auc: 0.885848	valid's auc: 0.800493
[3650]	train's auc: 0.886677	valid's auc: 0.800494
[3700]	train's auc: 0.887477	valid's auc: 0.800529
[3750]	train's auc: 0.888312	valid's auc: 0.80056
[3800]	train's auc: 0.889097	valid's auc: 0.800622
[3850]	train's auc: 0.889868	valid's auc: 0.800604
[3900]	train's auc: 0.890679	valid's auc: 0.800616
[3950]	train's auc: 0.891433	valid's auc: 0.800622
[4000]	train's auc: 0.892202	valid's auc: 0.800662
[4050]	train's auc: 0.893013	valid's auc: 0.800674
[4100]	train's auc: 0.893781	valid's auc: 0.800697
[4150]	train's auc: 0.89452	valid's auc: 0.800734
[4200]	train's auc: 0.895289	valid's auc: 0.800738
[4250]	train's auc: 0.896027	valid's auc: 0.800772
[4300]	train's auc: 0.896719	valid's auc: 0.800793
[4350]	train's auc: 0.897445	valid's auc: 0.800809
[4400]	train's auc: 0.898135	valid's auc: 0.800863
[4450]	train's auc: 0.89883	valid's auc: 0.800917
[4500]	train's auc: 0.89958	valid's auc: 0.800914
[4550]	train's auc: 0.900289	valid's auc: 0.800893
[4600]	train's auc: 0.900949	valid's auc: 0.800879
[4650]	train's auc: 0.901667	valid's auc: 0.800875
[4700]	train's auc: 0.902373	valid's auc: 0.800916
[4750]	train's auc: 0.903095	valid's auc: 0.800933
[4800]	train's auc: 0.903799	valid's auc: 0.800925
[4850]	train's auc: 0.9045	valid's auc: 0.800959
[4900]	train's auc: 0.905181	valid's auc: 0.800948
[4950]	train's auc: 0.905869	valid's auc: 0.800943
[5000]	train's auc: 0.906538	valid's auc: 0.800972
[5050]	train's auc: 0.907195	valid's auc: 0.800963
[5100]	train's auc: 0.907873	valid's auc: 0.800991
[5150]	train's auc: 0.908504	valid's auc: 0.800978
[5200]	train's auc: 0.909108	valid's auc: 0.801003
[5250]	train's auc: 0.909808	valid's auc: 0.800949
[5300]	train's auc: 0.910443	valid's auc: 0.800944
[5350]	train's auc: 0.911092	valid's auc: 0.800909
[5400]	train's auc: 0.911747	valid's auc: 0.800932
Early stopping, best iteration is:
[5123]	train's auc: 0.908169	valid's auc: 0.801012



[50]	train's auc: 0.757746	valid's auc: 0.740397
[100]	train's auc: 0.77366	valid's auc: 0.756463
[150]	train's auc: 0.782388	valid's auc: 0.76519
[200]	train's auc: 0.787888	valid's auc: 0.770146
[250]	train's auc: 0.792539	valid's auc: 0.774587
[300]	train's auc: 0.796336	valid's auc: 0.777822
[350]	train's auc: 0.799919	valid's auc: 0.780903
[400]	train's auc: 0.802876	valid's auc: 0.783204
[450]	train's auc: 0.805616	valid's auc: 0.784986
[500]	train's auc: 0.807977	valid's auc: 0.786375
[550]	train's auc: 0.810324	valid's auc: 0.78773
[600]	train's auc: 0.812576	valid's auc: 0.788693
[650]	train's auc: 0.814629	valid's auc: 0.78979
[700]	train's auc: 0.816627	valid's auc: 0.790684
[750]	train's auc: 0.818609	valid's auc: 0.791574
[800]	train's auc: 0.820546	valid's auc: 0.792414
[850]	train's auc: 0.822372	valid's auc: 0.793118
[900]	train's auc: 0.824123	valid's auc: 0.79377
[950]	train's auc: 0.825803	valid's auc: 0.794345
[1000]	train's auc: 0.827519	valid's auc: 0.79493
[1050]	train's auc: 0.829154	valid's auc: 0.795484
[1100]	train's auc: 0.830706	valid's auc: 0.795862
[1150]	train's auc: 0.832196	valid's auc: 0.796139
[1200]	train's auc: 0.833649	valid's auc: 0.796469
[1250]	train's auc: 0.835134	valid's auc: 0.796793
[1300]	train's auc: 0.836538	valid's auc: 0.797008
[1350]	train's auc: 0.837909	valid's auc: 0.797282
[1400]	train's auc: 0.839272	valid's auc: 0.797645
[1450]	train's auc: 0.840594	valid's auc: 0.797809
[1500]	train's auc: 0.841957	valid's auc: 0.798104
[1550]	train's auc: 0.843254	valid's auc: 0.798266
[1600]	train's auc: 0.844555	valid's auc: 0.79844
[1650]	train's auc: 0.845812	valid's auc: 0.798591
[1700]	train's auc: 0.847036	valid's auc: 0.79878
[1750]	train's auc: 0.84823	valid's auc: 0.798972
[1800]	train's auc: 0.849499	valid's auc: 0.799139
[1850]	train's auc: 0.850683	valid's auc: 0.79928
[1900]	train's auc: 0.851864	valid's auc: 0.799404
[1950]	train's auc: 0.853008	valid's auc: 0.799495
[2000]	train's auc: 0.854188	valid's auc: 0.799615
[2050]	train's auc: 0.855288	valid's auc: 0.799718
[2100]	train's auc: 0.856464	valid's auc: 0.799813
[2150]	train's auc: 0.857586	valid's auc: 0.799896
[2200]	train's auc: 0.858702	valid's auc: 0.80003
[2250]	train's auc: 0.859753	valid's auc: 0.800108
[2300]	train's auc: 0.86082	valid's auc: 0.80018
[2350]	train's auc: 0.861898	valid's auc: 0.800298
[2400]	train's auc: 0.862945	valid's auc: 0.800389
[2450]	train's auc: 0.863961	valid's auc: 0.800474
[2500]	train's auc: 0.864996	valid's auc: 0.800578
[2550]	train's auc: 0.865975	valid's auc: 0.800632
[2600]	train's auc: 0.866954	valid's auc: 0.800664
[2650]	train's auc: 0.867938	valid's auc: 0.800659
[2700]	train's auc: 0.868899	valid's auc: 0.800668
[2750]	train's auc: 0.869877	valid's auc: 0.80072
[2800]	train's auc: 0.870802	valid's auc: 0.800774
[2850]	train's auc: 0.871791	valid's auc: 0.800833
[2900]	train's auc: 0.872692	valid's auc: 0.800843
[2950]	train's auc: 0.873615	valid's auc: 0.800883
[3000]	train's auc: 0.874519	valid's auc: 0.800907
[3050]	train's auc: 0.875417	valid's auc: 0.800934
[3100]	train's auc: 0.876355	valid's auc: 0.800959
[3150]	train's auc: 0.877236	valid's auc: 0.800968
[3200]	train's auc: 0.878117	valid's auc: 0.801007
[3250]	train's auc: 0.879026	valid's auc: 0.801052
[3300]	train's auc: 0.879891	valid's auc: 0.801049
[3350]	train's auc: 0.880758	valid's auc: 0.801071
[3400]	train's auc: 0.881602	valid's auc: 0.80111
[3450]	train's auc: 0.882457	valid's auc: 0.80112
[3500]	train's auc: 0.883257	valid's auc: 0.80109
[3550]	train's auc: 0.884069	valid's auc: 0.801127
[3600]	train's auc: 0.884888	valid's auc: 0.801165
[3650]	train's auc: 0.885681	valid's auc: 0.801219
[3700]	train's auc: 0.886495	valid's auc: 0.801219
[3750]	train's auc: 0.887255	valid's auc: 0.801256
[3800]	train's auc: 0.888015	valid's auc: 0.80129
[3850]	train's auc: 0.888847	valid's auc: 0.801309
[3900]	train's auc: 0.889652	valid's auc: 0.801313
[3950]	train's auc: 0.890438	valid's auc: 0.80133
[4000]	train's auc: 0.891213	valid's auc: 0.801337
[4050]	train's auc: 0.891963	valid's auc: 0.801342
[4100]	train's auc: 0.892744	valid's auc: 0.801378
[4150]	train's auc: 0.893488	valid's auc: 0.801378
[4200]	train's auc: 0.894275	valid's auc: 0.801407
[4250]	train's auc: 0.895034	valid's auc: 0.801439
[4300]	train's auc: 0.895778	valid's auc: 0.801461
[4350]	train's auc: 0.896488	valid's auc: 0.801467
[4400]	train's auc: 0.897231	valid's auc: 0.801456
[4450]	train's auc: 0.897956	valid's auc: 0.801532
[4500]	train's auc: 0.898627	valid's auc: 0.801552
[4550]	train's auc: 0.899344	valid's auc: 0.801522
[4600]	train's auc: 0.9	valid's auc: 0.801532
[4650]	train's auc: 0.900704	valid's auc: 0.801513
[4700]	train's auc: 0.901383	valid's auc: 0.801526
[4750]	train's auc: 0.902079	valid's auc: 0.80153
[4800]	train's auc: 0.902789	valid's auc: 0.801551
Early stopping, best iteration is:
[4521]	train's auc: 0.898934	valid's auc: 0.801568


[50]	train's auc: 0.757685	valid's auc: 0.752235
[100]	train's auc: 0.773974	valid's auc: 0.76647
[150]	train's auc: 0.78269	valid's auc: 0.774018
[200]	train's auc: 0.788305	valid's auc: 0.77816
[250]	train's auc: 0.792952	valid's auc: 0.781525
[300]	train's auc: 0.796748	valid's auc: 0.783825
[350]	train's auc: 0.800272	valid's auc: 0.786174
[400]	train's auc: 0.803217	valid's auc: 0.787911
[450]	train's auc: 0.805971	valid's auc: 0.789212
[500]	train's auc: 0.808362	valid's auc: 0.79017
[550]	train's auc: 0.810724	valid's auc: 0.791143
[600]	train's auc: 0.812943	valid's auc: 0.791823
[650]	train's auc: 0.814982	valid's auc: 0.792505
[700]	train's auc: 0.816971	valid's auc: 0.793212
[750]	train's auc: 0.818954	valid's auc: 0.793846
[800]	train's auc: 0.820862	valid's auc: 0.79448
[850]	train's auc: 0.822735	valid's auc: 0.794948
[900]	train's auc: 0.82453	valid's auc: 0.795415
[950]	train's auc: 0.826238	valid's auc: 0.795851
[1000]	train's auc: 0.827957	valid's auc: 0.796266
[1050]	train's auc: 0.829587	valid's auc: 0.796612
[1100]	train's auc: 0.831142	valid's auc: 0.796908
[1150]	train's auc: 0.83272	valid's auc: 0.797158
[1200]	train's auc: 0.834235	valid's auc: 0.797439
[1250]	train's auc: 0.835759	valid's auc: 0.797725
[1300]	train's auc: 0.837241	valid's auc: 0.797942
[1350]	train's auc: 0.838634	valid's auc: 0.798101
[1400]	train's auc: 0.840032	valid's auc: 0.798313
[1450]	train's auc: 0.84141	valid's auc: 0.79849
[1500]	train's auc: 0.842736	valid's auc: 0.798597
[1550]	train's auc: 0.844049	valid's auc: 0.798764
[1600]	train's auc: 0.845355	valid's auc: 0.798903
[1650]	train's auc: 0.846679	valid's auc: 0.799012
[1700]	train's auc: 0.847865	valid's auc: 0.799159
[1750]	train's auc: 0.849118	valid's auc: 0.79926
[1800]	train's auc: 0.850328	valid's auc: 0.799388
[1850]	train's auc: 0.851505	valid's auc: 0.799464
[1900]	train's auc: 0.852748	valid's auc: 0.799557
[1950]	train's auc: 0.853878	valid's auc: 0.799625
[2000]	train's auc: 0.855067	valid's auc: 0.799695
[2050]	train's auc: 0.856187	valid's auc: 0.799745
[2100]	train's auc: 0.857315	valid's auc: 0.799811
[2150]	train's auc: 0.85843	valid's auc: 0.799846
[2200]	train's auc: 0.859534	valid's auc: 0.799938
[2250]	train's auc: 0.860642	valid's auc: 0.800042
[2300]	train's auc: 0.861728	valid's auc: 0.800067
[2350]	train's auc: 0.862801	valid's auc: 0.80013
[2400]	train's auc: 0.863837	valid's auc: 0.800172
[2450]	train's auc: 0.864883	valid's auc: 0.800275
[2500]	train's auc: 0.865922	valid's auc: 0.800349
[2550]	train's auc: 0.86696	valid's auc: 0.800352
[2600]	train's auc: 0.867941	valid's auc: 0.80038
[2650]	train's auc: 0.868947	valid's auc: 0.800369
[2700]	train's auc: 0.869921	valid's auc: 0.800424
[2750]	train's auc: 0.870902	valid's auc: 0.800472
[2800]	train's auc: 0.871857	valid's auc: 0.80046
[2850]	train's auc: 0.872785	valid's auc: 0.800521
[2900]	train's auc: 0.873731	valid's auc: 0.800515
[2950]	train's auc: 0.87468	valid's auc: 0.800546
[3000]	train's auc: 0.875605	valid's auc: 0.800608
[3050]	train's auc: 0.876509	valid's auc: 0.800613
[3100]	train's auc: 0.877432	valid's auc: 0.800609
[3150]	train's auc: 0.878359	valid's auc: 0.800639
[3200]	train's auc: 0.879285	valid's auc: 0.800634
[3250]	train's auc: 0.880215	valid's auc: 0.800658
[3300]	train's auc: 0.881096	valid's auc: 0.800678
[3350]	train's auc: 0.88199	valid's auc: 0.8007
[3400]	train's auc: 0.88287	valid's auc: 0.800675
[3450]	train's auc: 0.883722	valid's auc: 0.800704
[3500]	train's auc: 0.884551	valid's auc: 0.800667
[3550]	train's auc: 0.885411	valid's auc: 0.800686
[3600]	train's auc: 0.886227	valid's auc: 0.800676
[3650]	train's auc: 0.887065	valid's auc: 0.800707
[3700]	train's auc: 0.887881	valid's auc: 0.8007
[3750]	train's auc: 0.888708	valid's auc: 0.800725
[3800]	train's auc: 0.889524	valid's auc: 0.800728
[3850]	train's auc: 0.890305	valid's auc: 0.800716
[3900]	train's auc: 0.891123	valid's auc: 0.800698
[3950]	train's auc: 0.891907	valid's auc: 0.800696
[4000]	train's auc: 0.892683	valid's auc: 0.800683
[4050]	train's auc: 0.893428	valid's auc: 0.800654
Early stopping, best iteration is:
[3759]	train's auc: 0.888839	valid's auc: 0.800735


[50]	train's auc: 0.759084	valid's auc: 0.745489
[100]	train's auc: 0.775064	valid's auc: 0.759404
[150]	train's auc: 0.783826	valid's auc: 0.766656
[200]	train's auc: 0.78932	valid's auc: 0.771202
[250]	train's auc: 0.793962	valid's auc: 0.774289
[300]	train's auc: 0.797558	valid's auc: 0.776844
[350]	train's auc: 0.801049	valid's auc: 0.779271
[400]	train's auc: 0.804131	valid's auc: 0.781075
[450]	train's auc: 0.806906	valid's auc: 0.782578
[500]	train's auc: 0.809262	valid's auc: 0.78366
[550]	train's auc: 0.811619	valid's auc: 0.784609
[600]	train's auc: 0.81377	valid's auc: 0.785367
[650]	train's auc: 0.815796	valid's auc: 0.786142
[700]	train's auc: 0.817782	valid's auc: 0.786853
[750]	train's auc: 0.81974	valid's auc: 0.78762
[800]	train's auc: 0.821638	valid's auc: 0.788245
[850]	train's auc: 0.823461	valid's auc: 0.788848
[900]	train's auc: 0.825224	valid's auc: 0.78936
[950]	train's auc: 0.826962	valid's auc: 0.789842
[1000]	train's auc: 0.828708	valid's auc: 0.790306
[1050]	train's auc: 0.830338	valid's auc: 0.79073
[1100]	train's auc: 0.831904	valid's auc: 0.791067
[1150]	train's auc: 0.833429	valid's auc: 0.791328
[1200]	train's auc: 0.834921	valid's auc: 0.791577
[1250]	train's auc: 0.836438	valid's auc: 0.791817
[1300]	train's auc: 0.8379	valid's auc: 0.792072
[1350]	train's auc: 0.839278	valid's auc: 0.79225
[1400]	train's auc: 0.840635	valid's auc: 0.792455
[1450]	train's auc: 0.841964	valid's auc: 0.792645
[1500]	train's auc: 0.843296	valid's auc: 0.792809
[1550]	train's auc: 0.844578	valid's auc: 0.792957
[1600]	train's auc: 0.845893	valid's auc: 0.79309
[1650]	train's auc: 0.847188	valid's auc: 0.79323
[1700]	train's auc: 0.848335	valid's auc: 0.79338
[1750]	train's auc: 0.849558	valid's auc: 0.793522
[1800]	train's auc: 0.850761	valid's auc: 0.793685
[1850]	train's auc: 0.851973	valid's auc: 0.793814
[1900]	train's auc: 0.853177	valid's auc: 0.793936
[1950]	train's auc: 0.854301	valid's auc: 0.794015
[2000]	train's auc: 0.855491	valid's auc: 0.794129
[2050]	train's auc: 0.856597	valid's auc: 0.794273
[2100]	train's auc: 0.857735	valid's auc: 0.794426
[2150]	train's auc: 0.858829	valid's auc: 0.7945
[2200]	train's auc: 0.859954	valid's auc: 0.794587
[2250]	train's auc: 0.861083	valid's auc: 0.794608
[2300]	train's auc: 0.862152	valid's auc: 0.794684
[2350]	train's auc: 0.863188	valid's auc: 0.794721
[2400]	train's auc: 0.864244	valid's auc: 0.7948
[2450]	train's auc: 0.865274	valid's auc: 0.794857
[2500]	train's auc: 0.866316	valid's auc: 0.794878
[2550]	train's auc: 0.867291	valid's auc: 0.794956
[2600]	train's auc: 0.868245	valid's auc: 0.795017
[2650]	train's auc: 0.869303	valid's auc: 0.795026
[2700]	train's auc: 0.870313	valid's auc: 0.795094
[2750]	train's auc: 0.871294	valid's auc: 0.7951
[2800]	train's auc: 0.872231	valid's auc: 0.795137
[2850]	train's auc: 0.873184	valid's auc: 0.795135
[2900]	train's auc: 0.874101	valid's auc: 0.795128
[2950]	train's auc: 0.875002	valid's auc: 0.79515
[3000]	train's auc: 0.875905	valid's auc: 0.795213
[3050]	train's auc: 0.876785	valid's auc: 0.795229
[3100]	train's auc: 0.877735	valid's auc: 0.79527
[3150]	train's auc: 0.878623	valid's auc: 0.795288
[3200]	train's auc: 0.879561	valid's auc: 0.795318
[3250]	train's auc: 0.880489	valid's auc: 0.795343
[3300]	train's auc: 0.881364	valid's auc: 0.79536
[3350]	train's auc: 0.882234	valid's auc: 0.795442
[3400]	train's auc: 0.883121	valid's auc: 0.795478
[3450]	train's auc: 0.883981	valid's auc: 0.79551
[3500]	train's auc: 0.884806	valid's auc: 0.795527
[3550]	train's auc: 0.885618	valid's auc: 0.795569
[3600]	train's auc: 0.88643	valid's auc: 0.795581
[3650]	train's auc: 0.887252	valid's auc: 0.795622
[3700]	train's auc: 0.888067	valid's auc: 0.795652
[3750]	train's auc: 0.888868	valid's auc: 0.795672
[3800]	train's auc: 0.889707	valid's auc: 0.79568
[3850]	train's auc: 0.890499	valid's auc: 0.795687
[3900]	train's auc: 0.891301	valid's auc: 0.795704
[3950]	train's auc: 0.892069	valid's auc: 0.795676
[4000]	train's auc: 0.89285	valid's auc: 0.795692
[4050]	train's auc: 0.893638	valid's auc: 0.795687
[4100]	train's auc: 0.894381	valid's auc: 0.7957
[4150]	train's auc: 0.895119	valid's auc: 0.795655
Early stopping, best iteration is:
[3863]	train's auc: 0.8907	valid's auc: 0.795717
Full AUC score 0.799916
"""
























