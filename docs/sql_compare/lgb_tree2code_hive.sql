select
    `idx`
    ,1.0 / (1.0 + exp(-(((case when ((`thirdparty_info_period1_6` is null or (`thirdparty_info_period1_6` <> `thirdparty_info_period1_6`)) or ((not (`thirdparty_info_period1_6` is null or (`thirdparty_info_period1_6` <> `thirdparty_info_period1_6`))) and `thirdparty_info_period1_6` <= 14.500000000000002)) then
         (case when ((`thirdparty_info_period5_1` is null or (`thirdparty_info_period5_1` <> `thirdparty_info_period5_1`)) or ((not (`thirdparty_info_period5_1` is null or (`thirdparty_info_period5_1` <> `thirdparty_info_period5_1`))) and `thirdparty_info_period5_1` <= 1e-13)) then
             -2.4628822481842358
         else
             -2.489020191444419
         end)
     else
         -2.4295699792503966
     end) + (case when ((`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`)) or ((not (`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`))) and `thirdparty_info_period2_6` <= 23.500000000000004)) then
         (case when ((`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`)) or ((not (`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`))) and `userinfo_14` <= 3.5000000000000004)) then
             -0.019324384994685515
         else
             0.0073109151833848987
         end)
     else
         0.039935963366007805
     end) + (case when ((`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`)) or ((not (`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`))) and `thirdparty_info_period2_6` <= 25.500000000000004)) then
         (case when ((`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`)) or ((not (`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`))) and `userinfo_14` <= 3.5000000000000004)) then
             -0.018291967585472187
         else
             0.007151912716598369
         end)
     else
         0.038499405054906399
     end) + (case when ((`thirdparty_info_period1_6` is null or (`thirdparty_info_period1_6` <> `thirdparty_info_period1_6`)) or ((not (`thirdparty_info_period1_6` is null or (`thirdparty_info_period1_6` <> `thirdparty_info_period1_6`))) and `thirdparty_info_period1_6` <= 14.500000000000002)) then
         (case when ((`thirdparty_info_period5_1` is null or (`thirdparty_info_period5_1` <> `thirdparty_info_period5_1`)) or ((not (`thirdparty_info_period5_1` is null or (`thirdparty_info_period5_1` <> `thirdparty_info_period5_1`))) and `thirdparty_info_period5_1` <= 1e-13)) then
             0.008418998885988448
         else
             -0.016905859572355516
         end)
     else
         0.034415959832898392
     end) + (case when ((`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`)) or ((not (`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`))) and `thirdparty_info_period2_6` <= 14.500000000000002)) then
         -0.010683633147590037
     else
         (case when ((`thirdparty_info_period4_2` is null or (`thirdparty_info_period4_2` <> `thirdparty_info_period4_2`)) or ((not (`thirdparty_info_period4_2` is null or (`thirdparty_info_period4_2` <> `thirdparty_info_period4_2`))) and `thirdparty_info_period4_2` <= 1e-13)) then
             0.054706905369382289
         else
             0.013624238570792344
         end)
     end) + (case when ((`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`)) or ((not (`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`))) and `thirdparty_info_period2_6` <= 14.500000000000002)) then
         (case when ((`thirdparty_info_period6_1` is null or (`thirdparty_info_period6_1` <> `thirdparty_info_period6_1`)) or ((not (`thirdparty_info_period6_1` is null or (`thirdparty_info_period6_1` <> `thirdparty_info_period6_1`))) and `thirdparty_info_period6_1` <= 1e-13)) then
             0.0012477348096436517
         else
             -0.022718978698989683
         end)
     else
         0.023666342845193498
     end) + (case when ((`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`)) or ((not (`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`))) and `thirdparty_info_period2_6` <= 14.500000000000002)) then
         (case when ((`thirdparty_info_period5_1` is null or (`thirdparty_info_period5_1` <> `thirdparty_info_period5_1`)) or ((not (`thirdparty_info_period5_1` is null or (`thirdparty_info_period5_1` <> `thirdparty_info_period5_1`))) and `thirdparty_info_period5_1` <= 1e-13)) then
             0.0056295611338307242
         else
             -0.018552836412776698
         end)
     else
         0.022204118845676926
     end) + (case when ((`thirdparty_info_period1_6` is null or (`thirdparty_info_period1_6` <> `thirdparty_info_period1_6`)) or ((not (`thirdparty_info_period1_6` is null or (`thirdparty_info_period1_6` <> `thirdparty_info_period1_6`))) and `thirdparty_info_period1_6` <= 13.500000000000002)) then
         (case when ((`thirdparty_info_period6_1` is null or (`thirdparty_info_period6_1` <> `thirdparty_info_period6_1`)) or ((not (`thirdparty_info_period6_1` is null or (`thirdparty_info_period6_1` <> `thirdparty_info_period6_1`))) and `thirdparty_info_period6_1` <= 1e-13)) then
             0.0037908520179377268
         else
             -0.019257761567318916
         end)
     else
         0.026948557782490747
     end) + (case when ((`thirdparty_info_period1_6` is null or (`thirdparty_info_period1_6` <> `thirdparty_info_period1_6`)) or ((not (`thirdparty_info_period1_6` is null or (`thirdparty_info_period1_6` <> `thirdparty_info_period1_6`))) and `thirdparty_info_period1_6` <= 13.500000000000002)) then
         (case when ((`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`)) or ((not (`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`))) and `userinfo_14` <= 3.5000000000000004)) then
             -0.01626341335098435
         else
             0.0065303346185426854
         end)
     else
         0.025221039258161257
     end) + (case when ((`thirdparty_info_period5_2` is null or (`thirdparty_info_period5_2` <> `thirdparty_info_period5_2`)) or ((not (`thirdparty_info_period5_2` is null or (`thirdparty_info_period5_2` <> `thirdparty_info_period5_2`))) and `thirdparty_info_period5_2` <= 1e-13)) then
         (case when ((`thirdparty_info_period1_6` is null or (`thirdparty_info_period1_6` <> `thirdparty_info_period1_6`)) or ((not (`thirdparty_info_period1_6` is null or (`thirdparty_info_period1_6` <> `thirdparty_info_period1_6`))) and `thirdparty_info_period1_6` <= 15.500000000000002)) then
             0.0072000281642714955
         else
             0.051511265642508165
         end)
     else
         -0.010121182351034506
     end) + (case when ((`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`)) or ((not (`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`))) and `thirdparty_info_period2_6` <= 34.500000000000007)) then
         (case when ((`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`)) or ((not (`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`))) and `userinfo_14` <= 3.5000000000000004)) then
             -0.015402415703284945
         else
             0.0087501655617911664
         end)
     else
         0.030937223459711307
     end) + (case when ((`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`)) or ((not (`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`))) and `thirdparty_info_period2_6` <= 11.500000000000002)) then
         -0.00957996781860526
     else
         (case when ((`thirdparty_info_period5_2` is null or (`thirdparty_info_period5_2` <> `thirdparty_info_period5_2`)) or ((not (`thirdparty_info_period5_2` is null or (`thirdparty_info_period5_2` <> `thirdparty_info_period5_2`))) and `thirdparty_info_period5_2` <= 1e-13)) then
             0.037058036909436987
         else
             0.0036217913133995347
         end)
     end) + (case when ((`thirdparty_info_period6_2` is null or (`thirdparty_info_period6_2` <> `thirdparty_info_period6_2`)) or ((not (`thirdparty_info_period6_2` is null or (`thirdparty_info_period6_2` <> `thirdparty_info_period6_2`))) and `thirdparty_info_period6_2` <= 1e-13)) then
         (case when ((`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`)) or ((not (`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`))) and `thirdparty_info_period2_6` <= 9.5000000000000018)) then
             -0.00048790121227694142
         else
             0.027267082181530761
         end)
     else
         -0.013139533509006202
     end) + (case when ((`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`)) or ((not (`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`))) and `thirdparty_info_period2_6` <= 45.500000000000007)) then
         (case when ((`thirdparty_info_period6_1` is null or (`thirdparty_info_period6_1` <> `thirdparty_info_period6_1`)) or ((not (`thirdparty_info_period6_1` is null or (`thirdparty_info_period6_1` <> `thirdparty_info_period6_1`))) and `thirdparty_info_period6_1` <= 1e-13)) then
             0.0062776272833541761
         else
             -0.015815941335823716
         end)
     else
         0.031572520509753746
     end) + (case when ((`thirdparty_info_period5_2` is null or (`thirdparty_info_period5_2` <> `thirdparty_info_period5_2`)) or ((not (`thirdparty_info_period5_2` is null or (`thirdparty_info_period5_2` <> `thirdparty_info_period5_2`))) and `thirdparty_info_period5_2` <= 1e-13)) then
         0.014091203142360759
     else
         (case when ((`thirdparty_info_period4_6` is null or (`thirdparty_info_period4_6` <> `thirdparty_info_period4_6`)) or ((not (`thirdparty_info_period4_6` is null or (`thirdparty_info_period4_6` <> `thirdparty_info_period4_6`))) and `thirdparty_info_period4_6` <= 10.500000000000002)) then
             -0.018931765659086799
         else
             0.0060731731243174568
         end)
     end) + (case when ((`thirdparty_info_period1_15` is null or (`thirdparty_info_period1_15` <> `thirdparty_info_period1_15`)) or ((not (`thirdparty_info_period1_15` is null or (`thirdparty_info_period1_15` <> `thirdparty_info_period1_15`))) and `thirdparty_info_period1_15` <= 450.50000000000006)) then
         -0.0088697465654303288
     else
         (case when ((`thirdparty_info_period4_2` is null or (`thirdparty_info_period4_2` <> `thirdparty_info_period4_2`)) or ((not (`thirdparty_info_period4_2` is null or (`thirdparty_info_period4_2` <> `thirdparty_info_period4_2`))) and `thirdparty_info_period4_2` <= 1e-13)) then
             0.033594426296331643
         else
             0.004694753074927208
         end)
     end) + (case when ((`thirdparty_info_period5_1` is null or (`thirdparty_info_period5_1` <> `thirdparty_info_period5_1`)) or ((not (`thirdparty_info_period5_1` is null or (`thirdparty_info_period5_1` <> `thirdparty_info_period5_1`))) and `thirdparty_info_period5_1` <= 1e-13)) then
         0.014387711368448537
     else
         (case when ((`thirdparty_info_period4_6` is null or (`thirdparty_info_period4_6` <> `thirdparty_info_period4_6`)) or ((not (`thirdparty_info_period4_6` is null or (`thirdparty_info_period4_6` <> `thirdparty_info_period4_6`))) and `thirdparty_info_period4_6` <= 16.500000000000004)) then
             -0.016096192149103419
         else
             0.010432901487853299
         end)
     end) + (case when ((`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`)) or ((not (`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`))) and `userinfo_14` <= 3.5000000000000004)) then
         -0.00955581081601381
     else
         (case when ((`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`)) or ((not (`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`))) and `userinfo_16` <= 1.5000000000000002)) then
             0.024293950772789355
         else
             -0.002806400276973639
         end)
     end) + (case when ((`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`)) or ((not (`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`))) and `thirdparty_info_period2_6` <= 14.500000000000002)) then
         -0.0075759086470408247
     else
         (case when ((`webloginfo_7` is null or (`webloginfo_7` <> `webloginfo_7`)) or ((not (`webloginfo_7` is null or (`webloginfo_7` <> `webloginfo_7`))) and `webloginfo_7` <= 20.500000000000004)) then
             0.0082561785275601547
         else
             0.051749477183743411
         end)
     end) + (case when ((`thirdparty_info_period6_2` is null or (`thirdparty_info_period6_2` <> `thirdparty_info_period6_2`)) or ((not (`thirdparty_info_period6_2` is null or (`thirdparty_info_period6_2` <> `thirdparty_info_period6_2`))) and `thirdparty_info_period6_2` <= 1e-13)) then
         (case when ((`userinfo_15` is null or (`userinfo_15` <> `userinfo_15`)) or ((not (`userinfo_15` is null or (`userinfo_15` <> `userinfo_15`))) and `userinfo_15` <= 2.5000000000000004)) then
             -0.016246768738504832
         else
             0.015154459715390471
         end)
     else
         -0.011949488806590363
     end) + (case when ((`thirdparty_info_period1_15` is null or (`thirdparty_info_period1_15` <> `thirdparty_info_period1_15`)) or ((not (`thirdparty_info_period1_15` is null or (`thirdparty_info_period1_15` <> `thirdparty_info_period1_15`))) and `thirdparty_info_period1_15` <= 382.50000000000006)) then
         -0.0087889265190990665
     else
         (case when ((`thirdparty_info_period5_2` is null or (`thirdparty_info_period5_2` <> `thirdparty_info_period5_2`)) or ((not (`thirdparty_info_period5_2` is null or (`thirdparty_info_period5_2` <> `thirdparty_info_period5_2`))) and `thirdparty_info_period5_2` <= 1e-13)) then
             0.027228186180819292
         else
             0.0014836064675661585
         end)
     end) + (case when ((`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`)) or ((not (`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`))) and `userinfo_14` <= 3.5000000000000004)) then
         -0.0090140018601388965
     else
         (case when ((`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`)) or ((not (`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`))) and `userinfo_16` <= 1.5000000000000002)) then
             0.022255045802607024
         else
             -0.0024957638217521011
         end)
     end) + (case when ((`thirdparty_info_period6_1` is null or (`thirdparty_info_period6_1` <> `thirdparty_info_period6_1`)) or ((not (`thirdparty_info_period6_1` is null or (`thirdparty_info_period6_1` <> `thirdparty_info_period6_1`))) and `thirdparty_info_period6_1` <= 1e-13)) then
         (case when ((`thirdparty_info_period2_15` is null or (`thirdparty_info_period2_15` <> `thirdparty_info_period2_15`)) or ((not (`thirdparty_info_period2_15` is null or (`thirdparty_info_period2_15` <> `thirdparty_info_period2_15`))) and `thirdparty_info_period2_15` <= 383.50000000000006)) then
             -0.0025060494957937357
         else
             0.020443513665912016
         end)
     else
         -0.01088763102175091
     end) + (case when ((`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`)) or ((not (`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`))) and `userinfo_14` <= 2.5000000000000004)) then
         -0.020246066290781746
     else
         (case when ((`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`)) or ((not (`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`))) and `userinfo_16` <= 1.5000000000000002)) then
             0.013748785406705131
         else
             -0.0086646748833850411
         end)
     end) + (case when ((`thirdparty_info_period5_1` is null or (`thirdparty_info_period5_1` <> `thirdparty_info_period5_1`)) or ((not (`thirdparty_info_period5_1` is null or (`thirdparty_info_period5_1` <> `thirdparty_info_period5_1`))) and `thirdparty_info_period5_1` <= 1e-13)) then
         0.012601744982983533
     else
         (case when ((`thirdparty_info_period3_15` is null or (`thirdparty_info_period3_15` <> `thirdparty_info_period3_15`)) or ((not (`thirdparty_info_period3_15` is null or (`thirdparty_info_period3_15` <> `thirdparty_info_period3_15`))) and `thirdparty_info_period3_15` <= 1257.5000000000002)) then
             -0.015591097020586808
         else
             0.0072036304684054645
         end)
     end) + (case when ((`thirdparty_info_period6_9` is null or (`thirdparty_info_period6_9` <> `thirdparty_info_period6_9`)) or ((not (`thirdparty_info_period6_9` is null or (`thirdparty_info_period6_9` <> `thirdparty_info_period6_9`))) and `thirdparty_info_period6_9` <= 1e-13)) then
         (case when ((`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`)) or ((not (`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`))) and `thirdparty_info_period2_6` <= 7.5000000000000009)) then
             -0.0051713018907514783
         else
             0.015894101564951659
         end)
     else
         -0.017925537140112465
     end) + (case when ((`thirdparty_info_period5_2` is null or (`thirdparty_info_period5_2` <> `thirdparty_info_period5_2`)) or ((not (`thirdparty_info_period5_2` is null or (`thirdparty_info_period5_2` <> `thirdparty_info_period5_2`))) and `thirdparty_info_period5_2` <= 1e-13)) then
         0.011236907487583507
     else
         (case when ((`thirdparty_info_period4_6` is null or (`thirdparty_info_period4_6` <> `thirdparty_info_period4_6`)) or ((not (`thirdparty_info_period4_6` is null or (`thirdparty_info_period4_6` <> `thirdparty_info_period4_6`))) and `thirdparty_info_period4_6` <= 10.500000000000002)) then
             -0.017015605591210063
         else
             0.0050753504748189109
         end)
     end) + (case when ((`userinfo_15` is null or (`userinfo_15` <> `userinfo_15`)) or ((not (`userinfo_15` is null or (`userinfo_15` <> `userinfo_15`))) and `userinfo_15` <= 2.5000000000000004)) then
         -0.019425325129218733
     else
         (case when ((`thirdparty_info_period6_2` is null or (`thirdparty_info_period6_2` <> `thirdparty_info_period6_2`)) or ((not (`thirdparty_info_period6_2` is null or (`thirdparty_info_period6_2` <> `thirdparty_info_period6_2`))) and `thirdparty_info_period6_2` <= 1e-13)) then
             0.012796262236659698
         else
             -0.0072458353188200935
         end)
     end) + (case when ((`thirdparty_info_period5_10` is null or (`thirdparty_info_period5_10` <> `thirdparty_info_period5_10`)) or ((not (`thirdparty_info_period5_10` is null or (`thirdparty_info_period5_10` <> `thirdparty_info_period5_10`))) and `thirdparty_info_period5_10` <= 1e-13)) then
         (case when ((`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`)) or ((not (`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`))) and `thirdparty_info_period2_6` <= 6.5000000000000009)) then
             -0.0048557271896470158
         else
             0.016334556726702375
         end)
     else
         -0.014014976044327219
     end) + (case when ((`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`)) or ((not (`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`))) and `userinfo_14` <= 3.5000000000000004)) then
         (case when ((`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`)) or ((not (`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`))) and `thirdparty_info_period2_6` <= 32.500000000000007)) then
             -0.012721151159235364
         else
             0.015891100555479133
         end)
     else
         0.0099557344618717708
     end) + (case when ((`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`)) or ((not (`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`))) and `userinfo_16` <= 1.5000000000000002)) then
         (case when ((`thirdparty_info_period4_9` is null or (`thirdparty_info_period4_9` <> `thirdparty_info_period4_9`)) or ((not (`thirdparty_info_period4_9` is null or (`thirdparty_info_period4_9` <> `thirdparty_info_period4_9`))) and `thirdparty_info_period4_9` <= 1e-13)) then
             0.015014600325827561
         else
             -0.0071724524063081817
         end)
     else
         -0.011831776837191801
     end) + (case when ((`thirdparty_info_period5_1` is null or (`thirdparty_info_period5_1` <> `thirdparty_info_period5_1`)) or ((not (`thirdparty_info_period5_1` is null or (`thirdparty_info_period5_1` <> `thirdparty_info_period5_1`))) and `thirdparty_info_period5_1` <= 1e-13)) then
         0.011137470051898614
     else
         (case when ((`thirdparty_info_period4_6` is null or (`thirdparty_info_period4_6` <> `thirdparty_info_period4_6`)) or ((not (`thirdparty_info_period4_6` is null or (`thirdparty_info_period4_6` <> `thirdparty_info_period4_6`))) and `thirdparty_info_period4_6` <= 15.500000000000002)) then
             -0.014024697090446632
         else
             0.0076435929469874852
         end)
     end) + (case when ((`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`)) or ((not (`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`))) and `userinfo_16` <= 1.5000000000000002)) then
         (case when ((`education_info1` is null or (`education_info1` <> `education_info1`)) or ((not (`education_info1` is null or (`education_info1` <> `education_info1`))) and `education_info1` <= 1e-13)) then
             0.0096593385794973789
         else
             -0.032070886085127315
         end)
     else
         -0.011360006399658607
     end) + (case when ((`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`)) or ((not (`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`))) and `userinfo_14` <= 2.5000000000000004)) then
         -0.018358923163148067
     else
         (case when ((`thirdparty_info_period6_9` is null or (`thirdparty_info_period6_9` <> `thirdparty_info_period6_9`)) or ((not (`thirdparty_info_period6_9` is null or (`thirdparty_info_period6_9` <> `thirdparty_info_period6_9`))) and `thirdparty_info_period6_9` <= 1e-13)) then
             0.0088475114618395256
         else
             -0.013888622379827334
         end)
     end) + (case when ((`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`)) or ((not (`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`))) and `userinfo_16` <= 1.5000000000000002)) then
         (case when ((`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`)) or ((not (`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`))) and `thirdparty_info_period1_10` <= 1.5000000000000002)) then
             0.012398402994436855
         else
             -0.010754492053989439
         end)
     else
         -0.010885713468001587
     end) + (case when ((`thirdparty_info_period1_15` is null or (`thirdparty_info_period1_15` <> `thirdparty_info_period1_15`)) or ((not (`thirdparty_info_period1_15` is null or (`thirdparty_info_period1_15` <> `thirdparty_info_period1_15`))) and `thirdparty_info_period1_15` <= 382.50000000000006)) then
         -0.0074288607748409889
     else
         (case when ((`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`)) or ((not (`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`))) and `webloginfo_15` <= 5.5000000000000009)) then
             0.0064310053351155265
         else
             0.050067488340102564
         end)
     end) + (case when ((`thirdparty_info_period6_1` is null or (`thirdparty_info_period6_1` <> `thirdparty_info_period6_1`)) or ((not (`thirdparty_info_period6_1` is null or (`thirdparty_info_period6_1` <> `thirdparty_info_period6_1`))) and `thirdparty_info_period6_1` <= 1e-13)) then
         (case when ((`thirdparty_info_period2_15` is null or (`thirdparty_info_period2_15` <> `thirdparty_info_period2_15`)) or ((not (`thirdparty_info_period2_15` is null or (`thirdparty_info_period2_15` <> `thirdparty_info_period2_15`))) and `thirdparty_info_period2_15` <= 215.50000000000003)) then
             -0.004229939815536563
         else
             0.014721783421377064
         end)
     else
         -0.0093567938079617257
     end) + (case when ((`thirdparty_info_period5_9` is null or (`thirdparty_info_period5_9` <> `thirdparty_info_period5_9`)) or ((not (`thirdparty_info_period5_9` is null or (`thirdparty_info_period5_9` <> `thirdparty_info_period5_9`))) and `thirdparty_info_period5_9` <= 1e-13)) then
         (case when ((`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`)) or ((not (`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`))) and `userinfo_16` <= 1.5000000000000002)) then
             0.012486621214733028
         else
             -0.0067703400520713669
         end)
     else
         -0.012771682664543323
     end) + (case when ((`thirdparty_info_period5_2` is null or (`thirdparty_info_period5_2` <> `thirdparty_info_period5_2`)) or ((not (`thirdparty_info_period5_2` is null or (`thirdparty_info_period5_2` <> `thirdparty_info_period5_2`))) and `thirdparty_info_period5_2` <= 1e-13)) then
         0.009528166810729731
     else
         (case when ((`thirdparty_info_period4_6` is null or (`thirdparty_info_period4_6` <> `thirdparty_info_period4_6`)) or ((not (`thirdparty_info_period4_6` is null or (`thirdparty_info_period4_6` <> `thirdparty_info_period4_6`))) and `thirdparty_info_period4_6` <= 7.5000000000000009)) then
             -0.016676400807535061
         else
             0.0027027831704477799
         end)
     end) + (case when ((`userinfo_15` is null or (`userinfo_15` <> `userinfo_15`)) or ((not (`userinfo_15` is null or (`userinfo_15` <> `userinfo_15`))) and `userinfo_15` <= 3.5000000000000004)) then
         (case when ((`thirdparty_info_period2_8` is null or (`thirdparty_info_period2_8` <> `thirdparty_info_period2_8`)) or ((not (`thirdparty_info_period2_8` is null or (`thirdparty_info_period2_8` <> `thirdparty_info_period2_8`))) and `thirdparty_info_period2_8` <= 257.50000000000006)) then
             -0.011156596811970149
         else
             0.020533302396988584
         end)
     else
         0.0088372764802229185
     end) + (case when ((`thirdparty_info_period4_1` is null or (`thirdparty_info_period4_1` <> `thirdparty_info_period4_1`)) or ((not (`thirdparty_info_period4_1` is null or (`thirdparty_info_period4_1` <> `thirdparty_info_period4_1`))) and `thirdparty_info_period4_1` <= 1e-13)) then
         0.011915491630970228
     else
         (case when ((`thirdparty_info_period3_6` is null or (`thirdparty_info_period3_6` <> `thirdparty_info_period3_6`)) or ((not (`thirdparty_info_period3_6` is null or (`thirdparty_info_period3_6` <> `thirdparty_info_period3_6`))) and `thirdparty_info_period3_6` <= 3.5000000000000004)) then
             -0.019070801097472521
         else
             0.00082462580167543638
         end)
     end) + (case when ((`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`)) or ((not (`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`))) and `userinfo_14` <= 2.5000000000000004)) then
         -0.017181000498122143
     else
         (case when ((`thirdparty_info_period6_9` is null or (`thirdparty_info_period6_9` <> `thirdparty_info_period6_9`)) or ((not (`thirdparty_info_period6_9` is null or (`thirdparty_info_period6_9` <> `thirdparty_info_period6_9`))) and `thirdparty_info_period6_9` <= 1e-13)) then
             0.0079515873563552903
         else
             -0.012914947040829718
         end)
     end) + (case when ((`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`)) or ((not (`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`))) and `userinfo_16` <= 1.5000000000000002)) then
         (case when ((`education_info1` is null or (`education_info1` <> `education_info1`)) or ((not (`education_info1` is null or (`education_info1` <> `education_info1`))) and `education_info1` <= 1e-13)) then
             0.0083854609255509839
         else
             -0.030256358886643148
         end)
     else
         -0.010028170161081228
     end) + (case when ((`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`)) or ((not (`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`))) and `webloginfo_15` <= 5.5000000000000009)) then
         (case when ((`thirdparty_info_period6_2` is null or (`thirdparty_info_period6_2` <> `thirdparty_info_period6_2`)) or ((not (`thirdparty_info_period6_2` is null or (`thirdparty_info_period6_2` <> `thirdparty_info_period6_2`))) and `thirdparty_info_period6_2` <= 1e-13)) then
             0.0044956900812135187
         else
             -0.010987936483549364
         end)
     else
         0.031550880606673173
     end) + (case when ((`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`)) or ((not (`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`))) and `thirdparty_info_period1_10` <= 2.5000000000000004)) then
         (case when ((`thirdparty_info_period1_15` is null or (`thirdparty_info_period1_15` <> `thirdparty_info_period1_15`)) or ((not (`thirdparty_info_period1_15` is null or (`thirdparty_info_period1_15` <> `thirdparty_info_period1_15`))) and `thirdparty_info_period1_15` <= 382.50000000000006)) then
             -0.004390682141468343
         else
             0.012908884367225582
         end)
     else
         -0.020230109965988358
     end) + (case when ((`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`)) or ((not (`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`))) and `thirdparty_info_period2_6` <= 45.500000000000007)) then
         (case when ((`userinfo_15` is null or (`userinfo_15` <> `userinfo_15`)) or ((not (`userinfo_15` is null or (`userinfo_15` <> `userinfo_15`))) and `userinfo_15` <= 3.5000000000000004)) then
             -0.010229494598236077
         else
             0.0055541929743736229
         end)
     else
         0.019161119347118984
     end) + (case when ((`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`)) or ((not (`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`))) and `userinfo_17` <= 1.5000000000000002)) then
         (case when ((`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`)) or ((not (`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`))) and `userinfo_16` <= 1.5000000000000002)) then
             0.0091301662121777288
         else
             -0.0078249543168390553
         end)
     else
         -0.020805957187076528
     end) + (case when ((`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`)) or ((not (`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`))) and `thirdparty_info_period1_10` <= 2.5000000000000004)) then
         (case when ((`thirdparty_info_period4_1` is null or (`thirdparty_info_period4_1` <> `thirdparty_info_period4_1`)) or ((not (`thirdparty_info_period4_1` is null or (`thirdparty_info_period4_1` <> `thirdparty_info_period4_1`))) and `thirdparty_info_period4_1` <= 1e-13)) then
             0.01506503976366802
         else
             -0.0027406792147852375
         end)
     else
         -0.019539005440341518
     end) + (case when ((`thirdparty_info_period2_8` is null or (`thirdparty_info_period2_8` <> `thirdparty_info_period2_8`)) or ((not (`thirdparty_info_period2_8` is null or (`thirdparty_info_period2_8` <> `thirdparty_info_period2_8`))) and `thirdparty_info_period2_8` <= 192.50000000000003)) then
         (case when ((`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`)) or ((not (`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`))) and `userinfo_14` <= 2.5000000000000004)) then
             -0.021469775568127791
         else
             -0.00025789681689403161
         end)
     else
         0.013683091667625283
     end) + (case when ((`thirdparty_info_period4_2` is null or (`thirdparty_info_period4_2` <> `thirdparty_info_period4_2`)) or ((not (`thirdparty_info_period4_2` is null or (`thirdparty_info_period4_2` <> `thirdparty_info_period4_2`))) and `thirdparty_info_period4_2` <= 1e-13)) then
         0.0098416305390266259
     else
         (case when ((`thirdparty_info_period4_15` is null or (`thirdparty_info_period4_15` <> `thirdparty_info_period4_15`)) or ((not (`thirdparty_info_period4_15` is null or (`thirdparty_info_period4_15` <> `thirdparty_info_period4_15`))) and `thirdparty_info_period4_15` <= 196.50000000000003)) then
             -0.017260313368175594
         else
             0.00066208709781991114
         end)
     end) + (case when ((`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`)) or ((not (`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`))) and `webloginfo_15` <= 1.5000000000000002)) then
         (case when ((`thirdparty_info_period3_10` is null or (`thirdparty_info_period3_10` <> `thirdparty_info_period3_10`)) or ((not (`thirdparty_info_period3_10` is null or (`thirdparty_info_period3_10` <> `thirdparty_info_period3_10`))) and `thirdparty_info_period3_10` <= 2.5000000000000004)) then
             -0.0015462678286328776
         else
             -0.026115874297408987
         end)
     else
         0.013545175978227695
     end) + (case when ((`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`)) or ((not (`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`))) and `userinfo_17` <= 1.5000000000000002)) then
         (case when ((`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`)) or ((not (`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`))) and `userinfo_16` <= 1.5000000000000002)) then
             0.0085637261217881341
         else
             -0.00744222190232243
         end)
     else
         -0.019897611364543287
     end) + (case when ((`thirdparty_info_period6_14` is null or (`thirdparty_info_period6_14` <> `thirdparty_info_period6_14`)) or ((not (`thirdparty_info_period6_14` is null or (`thirdparty_info_period6_14` <> `thirdparty_info_period6_14`))) and `thirdparty_info_period6_14` <= 2351.5000000000005)) then
         0.0087333344532606796
     else
         (case when ((`thirdparty_info_period6_6` is null or (`thirdparty_info_period6_6` <> `thirdparty_info_period6_6`)) or ((not (`thirdparty_info_period6_6` is null or (`thirdparty_info_period6_6` <> `thirdparty_info_period6_6`))) and `thirdparty_info_period6_6` <= 21.500000000000004)) then
             -0.011107391452027852
         else
             0.01040965779959591
         end)
     end) + (case when ((`thirdparty_info_period6_9` is null or (`thirdparty_info_period6_9` <> `thirdparty_info_period6_9`)) or ((not (`thirdparty_info_period6_9` is null or (`thirdparty_info_period6_9` <> `thirdparty_info_period6_9`))) and `thirdparty_info_period6_9` <= 1e-13)) then
         (case when ((`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`)) or ((not (`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`))) and `thirdparty_info_period2_6` <= 2.5000000000000004)) then
             -0.0088373386688814209
         else
             0.0084727734914154442
         end)
     else
         -0.014164217351115296
     end) + (case when ((`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`)) or ((not (`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`))) and `thirdparty_info_period1_10` <= 2.5000000000000004)) then
         (case when ((`thirdparty_info_period4_1` is null or (`thirdparty_info_period4_1` <> `thirdparty_info_period4_1`)) or ((not (`thirdparty_info_period4_1` is null or (`thirdparty_info_period4_1` <> `thirdparty_info_period4_1`))) and `thirdparty_info_period4_1` <= 1e-13)) then
             0.013611600342336456
         else
             -0.0026563788068411438
         end)
     else
         -0.018744238813878641
     end) + (case when ((`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`)) or ((not (`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`))) and `webloginfo_15` <= 1.5000000000000002)) then
         (case when ((`thirdparty_info_period6_5` is null or (`thirdparty_info_period6_5` <> `thirdparty_info_period6_5`)) or ((not (`thirdparty_info_period6_5` is null or (`thirdparty_info_period6_5` <> `thirdparty_info_period6_5`))) and `thirdparty_info_period6_5` <= 65.500000000000014)) then
             0.0010920108188996497
         else
             -0.013808417836625947
         end)
     else
         0.01261025205947377
     end) + (case when ((`thirdparty_info_period5_9` is null or (`thirdparty_info_period5_9` <> `thirdparty_info_period5_9`)) or ((not (`thirdparty_info_period5_9` is null or (`thirdparty_info_period5_9` <> `thirdparty_info_period5_9`))) and `thirdparty_info_period5_9` <= 1e-13)) then
         (case when ((`thirdparty_info_period4_6` is null or (`thirdparty_info_period4_6` <> `thirdparty_info_period4_6`)) or ((not (`thirdparty_info_period4_6` is null or (`thirdparty_info_period4_6` <> `thirdparty_info_period4_6`))) and `thirdparty_info_period4_6` <= 21.500000000000004)) then
             0.00027218776528114836
         else
             0.0186350641201713
         end)
     else
         -0.010933309636034554
     end) + (case when ((`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`)) or ((not (`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`))) and `userinfo_17` <= 1.5000000000000002)) then
         (case when ((`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`)) or ((not (`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`))) and `userinfo_16` <= 1.5000000000000002)) then
             0.0079557729415166405
         else
             -0.0070039651686499603
         end)
     else
         -0.019287194114605055
     end) + (case when ((`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`)) or ((not (`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`))) and `userinfo_14` <= 2.5000000000000004)) then
         -0.015212955996736489
     else
         (case when ((`thirdparty_info_period3_10` is null or (`thirdparty_info_period3_10` <> `thirdparty_info_period3_10`)) or ((not (`thirdparty_info_period3_10` is null or (`thirdparty_info_period3_10` <> `thirdparty_info_period3_10`))) and `thirdparty_info_period3_10` <= 1e-13)) then
             0.0083536624850551675
         else
             -0.0064573759889835231
         end)
     end) + (case when ((`thirdparty_info_period2_8` is null or (`thirdparty_info_period2_8` <> `thirdparty_info_period2_8`)) or ((not (`thirdparty_info_period2_8` is null or (`thirdparty_info_period2_8` <> `thirdparty_info_period2_8`))) and `thirdparty_info_period2_8` <= 192.50000000000003)) then
         (case when ((`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`)) or ((not (`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`))) and `userinfo_14` <= 2.5000000000000004)) then
             -0.019975652151133921
         else
             -0.00033249013025029683
         end)
     else
         0.012363079588216853
     end) + (case when ((`thirdparty_info_period5_2` is null or (`thirdparty_info_period5_2` <> `thirdparty_info_period5_2`)) or ((not (`thirdparty_info_period5_2` is null or (`thirdparty_info_period5_2` <> `thirdparty_info_period5_2`))) and `thirdparty_info_period5_2` <= 1e-13)) then
         0.0076774065818251414
     else
         (case when ((`thirdparty_info_period4_6` is null or (`thirdparty_info_period4_6` <> `thirdparty_info_period4_6`)) or ((not (`thirdparty_info_period4_6` is null or (`thirdparty_info_period4_6` <> `thirdparty_info_period4_6`))) and `thirdparty_info_period4_6` <= 3.5000000000000004)) then
             -0.018326181465486063
         else
             -0.00018494926654721812
         end)
     end) + (case when ((`thirdparty_info_period4_2` is null or (`thirdparty_info_period4_2` <> `thirdparty_info_period4_2`)) or ((not (`thirdparty_info_period4_2` is null or (`thirdparty_info_period4_2` <> `thirdparty_info_period4_2`))) and `thirdparty_info_period4_2` <= 1e-13)) then
         0.0088159391541196164
     else
         (case when ((`thirdparty_info_period4_6` is null or (`thirdparty_info_period4_6` <> `thirdparty_info_period4_6`)) or ((not (`thirdparty_info_period4_6` is null or (`thirdparty_info_period4_6` <> `thirdparty_info_period4_6`))) and `thirdparty_info_period4_6` <= 7.5000000000000009)) then
             -0.012976733093149596
         else
             0.0025306481928173657
         end)
     end) + (case when ((`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`)) or ((not (`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`))) and `userinfo_17` <= 1.5000000000000002)) then
         (case when ((`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`)) or ((not (`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`))) and `userinfo_16` <= 1.5000000000000002)) then
             0.0076755064526000524
         else
             -0.0068997720510901696
         end)
     else
         -0.018767171645464997
     end) + (case when ((`education_info1` is null or (`education_info1` <> `education_info1`)) or ((not (`education_info1` is null or (`education_info1` <> `education_info1`))) and `education_info1` <= 1e-13)) then
         (case when ((`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`)) or ((not (`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`))) and `userinfo_16` <= 1.5000000000000002)) then
             0.0067658180770385342
         else
             -0.0076426847520855079
         end)
     else
         -0.029558967931558155
     end) + (case when ((`thirdparty_info_period2_10` is null or (`thirdparty_info_period2_10` <> `thirdparty_info_period2_10`)) or ((not (`thirdparty_info_period2_10` is null or (`thirdparty_info_period2_10` <> `thirdparty_info_period2_10`))) and `thirdparty_info_period2_10` <= 1.5000000000000002)) then
         (case when ((`thirdparty_info_period2_8` is null or (`thirdparty_info_period2_8` <> `thirdparty_info_period2_8`)) or ((not (`thirdparty_info_period2_8` is null or (`thirdparty_info_period2_8` <> `thirdparty_info_period2_8`))) and `thirdparty_info_period2_8` <= 192.50000000000003)) then
             -0.00015717972869373013
         else
             0.01668441710550694
         end)
     else
         -0.012330942682136435
     end) + (case when ((`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`)) or ((not (`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`))) and `thirdparty_info_period1_10` <= 2.5000000000000004)) then
         (case when ((`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`)) or ((not (`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`))) and `webloginfo_15` <= 1.5000000000000002)) then
             -0.0014009737080725995
         else
             0.015123479834218086
         end)
     else
         -0.017463820905455351
     end) + (case when ((`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`)) or ((not (`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`))) and `webloginfo_15` <= 5.5000000000000009)) then
         (case when ((`thirdparty_info_period3_9` is null or (`thirdparty_info_period3_9` <> `thirdparty_info_period3_9`)) or ((not (`thirdparty_info_period3_9` is null or (`thirdparty_info_period3_9` <> `thirdparty_info_period3_9`))) and `thirdparty_info_period3_9` <= 1e-13)) then
             0.0030043946131804336
         else
             -0.010216863131916068
         end)
     else
         0.025400842748621335
     end) + (case when ((`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`)) or ((not (`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`))) and `thirdparty_info_period2_6` <= 2.5000000000000004)) then
         -0.010886945274254139
     else
         (case when ((`thirdparty_info_period6_14` is null or (`thirdparty_info_period6_14` <> `thirdparty_info_period6_14`)) or ((not (`thirdparty_info_period6_14` is null or (`thirdparty_info_period6_14` <> `thirdparty_info_period6_14`))) and `thirdparty_info_period6_14` <= 3438.5000000000005)) then
             0.012741032478889025
         else
             -0.0024410072650946418
         end)
     end) + (case when ((`education_info1` is null or (`education_info1` <> `education_info1`)) or ((not (`education_info1` is null or (`education_info1` <> `education_info1`))) and `education_info1` <= 1e-13)) then
         (case when ((`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`)) or ((not (`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`))) and `userinfo_16` <= 1.5000000000000002)) then
             0.0064462434683737763
         else
             -0.0070955724637126634
         end)
     else
         -0.029249166727213879
     end) + (case when ((`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`)) or ((not (`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`))) and `thirdparty_info_period2_3` <= 426.50000000000006)) then
         -0.0027606772976732762
     else
         (case when ((`thirdparty_info_period3_5` is null or (`thirdparty_info_period3_5` <> `thirdparty_info_period3_5`)) or ((not (`thirdparty_info_period3_5` is null or (`thirdparty_info_period3_5` <> `thirdparty_info_period3_5`))) and `thirdparty_info_period3_5` <= 161.50000000000003)) then
             0.025692281766151029
         else
             -0.007251550862327343
         end)
     end) + (case when ((`thirdparty_info_period4_1` is null or (`thirdparty_info_period4_1` <> `thirdparty_info_period4_1`)) or ((not (`thirdparty_info_period4_1` is null or (`thirdparty_info_period4_1` <> `thirdparty_info_period4_1`))) and `thirdparty_info_period4_1` <= 1e-13)) then
         0.0089395624764591029
     else
         (case when ((`thirdparty_info_period3_6` is null or (`thirdparty_info_period3_6` <> `thirdparty_info_period3_6`)) or ((not (`thirdparty_info_period3_6` is null or (`thirdparty_info_period3_6` <> `thirdparty_info_period3_6`))) and `thirdparty_info_period3_6` <= 3.5000000000000004)) then
             -0.016319869063886473
         else
             0.00062923804046889241
         end)
     end) + (case when ((`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`)) or ((not (`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`))) and `thirdparty_info_period1_10` <= 2.5000000000000004)) then
         (case when ((`thirdparty_info_period1_15` is null or (`thirdparty_info_period1_15` <> `thirdparty_info_period1_15`)) or ((not (`thirdparty_info_period1_15` is null or (`thirdparty_info_period1_15` <> `thirdparty_info_period1_15`))) and `thirdparty_info_period1_15` <= 115.50000000000001)) then
             -0.0058301358232116032
         else
             0.0076012770616142658
         end)
     else
         -0.01701084614994559
     end) + (case when ((`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`)) or ((not (`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`))) and `userinfo_17` <= 1.5000000000000002)) then
         (case when ((`userinfo_15` is null or (`userinfo_15` <> `userinfo_15`)) or ((not (`userinfo_15` is null or (`userinfo_15` <> `userinfo_15`))) and `userinfo_15` <= 3.5000000000000004)) then
             -0.0041516056357307589
         else
             0.0090369802908066964
         end)
     else
         -0.017714935763963689
     end) + (case when ((`thirdparty_info_period6_14` is null or (`thirdparty_info_period6_14` <> `thirdparty_info_period6_14`)) or ((not (`thirdparty_info_period6_14` is null or (`thirdparty_info_period6_14` <> `thirdparty_info_period6_14`))) and `thirdparty_info_period6_14` <= 2351.5000000000005)) then
         0.00714157759108364
     else
         (case when ((`thirdparty_info_period6_15` is null or (`thirdparty_info_period6_15` <> `thirdparty_info_period6_15`)) or ((not (`thirdparty_info_period6_15` is null or (`thirdparty_info_period6_15` <> `thirdparty_info_period6_15`))) and `thirdparty_info_period6_15` <= 414.50000000000006)) then
             -0.014324439914961988
         else
             0.0030502561739427607
         end)
     end) + (case when ((`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`)) or ((not (`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`))) and `userinfo_14` <= 2.5000000000000004)) then
         -0.013612685527976148
     else
         (case when ((`thirdparty_info_period2_10` is null or (`thirdparty_info_period2_10` <> `thirdparty_info_period2_10`)) or ((not (`thirdparty_info_period2_10` is null or (`thirdparty_info_period2_10` <> `thirdparty_info_period2_10`))) and `thirdparty_info_period2_10` <= 1.5000000000000002)) then
             0.0058446572066255956
         else
             -0.0093022531698549061
         end)
     end) + (case when ((`thirdparty_info_period5_1` is null or (`thirdparty_info_period5_1` <> `thirdparty_info_period5_1`)) or ((not (`thirdparty_info_period5_1` is null or (`thirdparty_info_period5_1` <> `thirdparty_info_period5_1`))) and `thirdparty_info_period5_1` <= 1e-13)) then
         0.0072732431879966881
     else
         (case when ((`thirdparty_info_period3_6` is null or (`thirdparty_info_period3_6` <> `thirdparty_info_period3_6`)) or ((not (`thirdparty_info_period3_6` is null or (`thirdparty_info_period3_6` <> `thirdparty_info_period3_6`))) and `thirdparty_info_period3_6` <= 3.5000000000000004)) then
             -0.016891604508238622
         else
             2.3332093540659132e-05
         end)
     end) + (case when ((`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`)) or ((not (`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`))) and `userinfo_17` <= 1.5000000000000002)) then
         (case when ((`userinfo_15` is null or (`userinfo_15` <> `userinfo_15`)) or ((not (`userinfo_15` is null or (`userinfo_15` <> `userinfo_15`))) and `userinfo_15` <= 3.5000000000000004)) then
             -0.0037592885301220035
         else
             0.0081112431267463311
         end)
     else
         -0.017055467911961667
     end) + (case when ((`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`)) or ((not (`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`))) and `webloginfo_15` <= 5.5000000000000009)) then
         (case when ((`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`)) or ((not (`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`))) and `thirdparty_info_period1_10` <= 1.5000000000000002)) then
             0.0015488657127521179
         else
             -0.012825332280571464
         end)
     else
         0.022626507744164224
     end) + (case when ((`thirdparty_info_period3_8` is null or (`thirdparty_info_period3_8` <> `thirdparty_info_period3_8`)) or ((not (`thirdparty_info_period3_8` is null or (`thirdparty_info_period3_8` <> `thirdparty_info_period3_8`))) and `thirdparty_info_period3_8` <= 484.50000000000006)) then
         (case when ((`thirdparty_info_period5_1` is null or (`thirdparty_info_period5_1` <> `thirdparty_info_period5_1`)) or ((not (`thirdparty_info_period5_1` is null or (`thirdparty_info_period5_1` <> `thirdparty_info_period5_1`))) and `thirdparty_info_period5_1` <= 1e-13)) then
             0.0065400537862560773
         else
             -0.0059009293359204278
         end)
     else
         0.04209925779325388
     end) + (case when ((`education_info1` is null or (`education_info1` <> `education_info1`)) or ((not (`education_info1` is null or (`education_info1` <> `education_info1`))) and `education_info1` <= 1e-13)) then
         (case when ((`thirdparty_info_period4_2` is null or (`thirdparty_info_period4_2` <> `thirdparty_info_period4_2`)) or ((not (`thirdparty_info_period4_2` is null or (`thirdparty_info_period4_2` <> `thirdparty_info_period4_2`))) and `thirdparty_info_period4_2` <= 1e-13)) then
             0.0091791684346042204
         else
             -0.0032213993876063331
         end)
     else
         -0.027588518259356876
     end) + (case when ((`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`)) or ((not (`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`))) and `thirdparty_info_period2_3` <= 426.50000000000006)) then
         -0.0026419751242369831
     else
         (case when ((`thirdparty_info_period3_5` is null or (`thirdparty_info_period3_5` <> `thirdparty_info_period3_5`)) or ((not (`thirdparty_info_period3_5` is null or (`thirdparty_info_period3_5` <> `thirdparty_info_period3_5`))) and `thirdparty_info_period3_5` <= 161.50000000000003)) then
             0.023611306684714461
         else
             -0.007105332328962855
         end)
     end) + (case when ((`education_info1` is null or (`education_info1` <> `education_info1`)) or ((not (`education_info1` is null or (`education_info1` <> `education_info1`))) and `education_info1` <= 1e-13)) then
         (case when ((`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`)) or ((not (`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`))) and `userinfo_17` <= 1.5000000000000002)) then
             0.003219235453477012
         else
             -0.015596246667372724
         end)
     else
         -0.026823179942248556
     end) + (case when ((`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`)) or ((not (`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`))) and `webloginfo_15` <= 1e-13)) then
         (case when ((`thirdparty_info_period3_10` is null or (`thirdparty_info_period3_10` <> `thirdparty_info_period3_10`)) or ((not (`thirdparty_info_period3_10` is null or (`thirdparty_info_period3_10` <> `thirdparty_info_period3_10`))) and `thirdparty_info_period3_10` <= 2.5000000000000004)) then
             -0.0018516216784246261
         else
             -0.024665293076471546
         end)
     else
         0.0081009938816987651
     end) + (case when ((`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`)) or ((not (`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`))) and `userinfo_16` <= 1.5000000000000002)) then
         (case when ((`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`)) or ((not (`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`))) and `thirdparty_info_period1_10` <= 1.5000000000000002)) then
             0.0077876880179024227
         else
             -0.0081253659919799572
         end)
     else
         -0.0075811856875240115
     end) + (case when ((`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`)) or ((not (`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`))) and `thirdparty_info_period2_3` <= 184.50000000000003)) then
         -0.0059842166591075469
     else
         (case when ((`thirdparty_info_period5_5` is null or (`thirdparty_info_period5_5` <> `thirdparty_info_period5_5`)) or ((not (`thirdparty_info_period5_5` is null or (`thirdparty_info_period5_5` <> `thirdparty_info_period5_5`))) and `thirdparty_info_period5_5` <= 82.500000000000014)) then
             0.015572136552182808
         else
             -0.0042044865213428425
         end)
     end) + (case when ((`thirdparty_info_period2_8` is null or (`thirdparty_info_period2_8` <> `thirdparty_info_period2_8`)) or ((not (`thirdparty_info_period2_8` is null or (`thirdparty_info_period2_8` <> `thirdparty_info_period2_8`))) and `thirdparty_info_period2_8` <= 257.50000000000006)) then
         (case when ((`thirdparty_info_period5_5` is null or (`thirdparty_info_period5_5` <> `thirdparty_info_period5_5`)) or ((not (`thirdparty_info_period5_5` is null or (`thirdparty_info_period5_5` <> `thirdparty_info_period5_5`))) and `thirdparty_info_period5_5` <= 46.500000000000007)) then
             0.0052218252693657522
         else
             -0.0078922559035768305
         end)
     else
         0.013679232594430152
     end) + (case when ((`thirdparty_info_period4_2` is null or (`thirdparty_info_period4_2` <> `thirdparty_info_period4_2`)) or ((not (`thirdparty_info_period4_2` is null or (`thirdparty_info_period4_2` <> `thirdparty_info_period4_2`))) and `thirdparty_info_period4_2` <= 1e-13)) then
         0.0071935442714035043
     else
         (case when ((`thirdparty_info_period4_6` is null or (`thirdparty_info_period4_6` <> `thirdparty_info_period4_6`)) or ((not (`thirdparty_info_period4_6` is null or (`thirdparty_info_period4_6` <> `thirdparty_info_period4_6`))) and `thirdparty_info_period4_6` <= 39.500000000000007)) then
             -0.0072061108213528485
         else
             0.010813038962429147
         end)
     end) + (case when ((`thirdparty_info_period6_14` is null or (`thirdparty_info_period6_14` <> `thirdparty_info_period6_14`)) or ((not (`thirdparty_info_period6_14` is null or (`thirdparty_info_period6_14` <> `thirdparty_info_period6_14`))) and `thirdparty_info_period6_14` <= 2351.5000000000005)) then
         0.0062371306005366625
     else
         (case when ((`thirdparty_info_period6_15` is null or (`thirdparty_info_period6_15` <> `thirdparty_info_period6_15`)) or ((not (`thirdparty_info_period6_15` is null or (`thirdparty_info_period6_15` <> `thirdparty_info_period6_15`))) and `thirdparty_info_period6_15` <= 192.50000000000003)) then
             -0.015539636508257348
         else
             0.0011534479172392853
         end)
     end) + (case when ((`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`)) or ((not (`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`))) and `thirdparty_info_period1_10` <= 2.5000000000000004)) then
         (case when ((`education_info5` is null or (`education_info5` <> `education_info5`)) or ((not (`education_info5` is null or (`education_info5` <> `education_info5`))) and `education_info5` <= 1e-13)) then
             0.0029508992352049097
         else
             -0.032991998242846231
         end)
     else
         -0.015253439047782057
     end) + (case when ((`education_info1` is null or (`education_info1` <> `education_info1`)) or ((not (`education_info1` is null or (`education_info1` <> `education_info1`))) and `education_info1` <= 1e-13)) then
         (case when ((`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`)) or ((not (`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`))) and `webloginfo_15` <= 5.5000000000000009)) then
             -0.00036919539318756687
         else
             0.022601694690081976
         end)
     else
         -0.026044298605751526
     end) + (case when ((`thirdparty_info_period6_9` is null or (`thirdparty_info_period6_9` <> `thirdparty_info_period6_9`)) or ((not (`thirdparty_info_period6_9` is null or (`thirdparty_info_period6_9` <> `thirdparty_info_period6_9`))) and `thirdparty_info_period6_9` <= 1e-13)) then
         (case when ((`education_info5` is null or (`education_info5` <> `education_info5`)) or ((not (`education_info5` is null or (`education_info5` <> `education_info5`))) and `education_info5` <= 1e-13)) then
             0.0035987120758263409
         else
             -0.031267159733482451
         end)
     else
         -0.010945952029616736
     end) + (case when ((`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`)) or ((not (`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`))) and `userinfo_17` <= 1.5000000000000002)) then
         (case when ((`userinfo_5` is null or (`userinfo_5` <> `userinfo_5`)) or ((not (`userinfo_5` is null or (`userinfo_5` <> `userinfo_5`))) and `userinfo_5` <= 2.5000000000000004)) then
             0.00032121848099252675
         else
             0.026230004075447417
         end)
     else
         -0.015590680278621769
     end) + (case when ((`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`)) or ((not (`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`))) and `thirdparty_info_period2_6` <= 2.5000000000000004)) then
         -0.0091378291836960168
     else
         (case when ((`thirdparty_info_period4_9` is null or (`thirdparty_info_period4_9` <> `thirdparty_info_period4_9`)) or ((not (`thirdparty_info_period4_9` is null or (`thirdparty_info_period4_9` <> `thirdparty_info_period4_9`))) and `thirdparty_info_period4_9` <= 1.5000000000000002)) then
             0.0068694101508815497
         else
             -0.0080076753132772068
         end)
     end) + (case when ((`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`)) or ((not (`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`))) and `userinfo_16` <= 1.5000000000000002)) then
         (case when ((`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`)) or ((not (`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`))) and `thirdparty_info_period2_3` <= 426.50000000000006)) then
             0.0013209306266953923
         else
             0.018822657579687093
         end)
     else
         -0.0071928856752750264
     end) + (case when ((`thirdparty_info_period3_8` is null or (`thirdparty_info_period3_8` <> `thirdparty_info_period3_8`)) or ((not (`thirdparty_info_period3_8` is null or (`thirdparty_info_period3_8` <> `thirdparty_info_period3_8`))) and `thirdparty_info_period3_8` <= 484.50000000000006)) then
         (case when ((`thirdparty_info_period6_5` is null or (`thirdparty_info_period6_5` <> `thirdparty_info_period6_5`)) or ((not (`thirdparty_info_period6_5` is null or (`thirdparty_info_period6_5` <> `thirdparty_info_period6_5`))) and `thirdparty_info_period6_5` <= 96.500000000000014)) then
             0.0017967832344479352
         else
             -0.012758908728914742
         end)
     else
         0.035368349466279127
     end) + (case when ((`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`)) or ((not (`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`))) and `thirdparty_info_period2_3` <= 184.50000000000003)) then
         -0.0055812060701325144
     else
         (case when ((`thirdparty_info_period5_5` is null or (`thirdparty_info_period5_5` <> `thirdparty_info_period5_5`)) or ((not (`thirdparty_info_period5_5` is null or (`thirdparty_info_period5_5` <> `thirdparty_info_period5_5`))) and `thirdparty_info_period5_5` <= 87.500000000000014)) then
             0.013490717635320729
         else
             -0.0045648555476758583
         end)
     end) + (case when ((`education_info1` is null or (`education_info1` <> `education_info1`)) or ((not (`education_info1` is null or (`education_info1` <> `education_info1`))) and `education_info1` <= 1e-13)) then
         (case when ((`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`)) or ((not (`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`))) and `userinfo_16` <= 1.5000000000000002)) then
             0.0052145623409894796
         else
             -0.0062361209862123604
         end)
     else
         -0.025364697841014652
     end) + (case when ((`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`)) or ((not (`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`))) and `thirdparty_info_period1_10` <= 2.5000000000000004)) then
         (case when ((`thirdparty_info_period4_1` is null or (`thirdparty_info_period4_1` <> `thirdparty_info_period4_1`)) or ((not (`thirdparty_info_period4_1` is null or (`thirdparty_info_period4_1` <> `thirdparty_info_period4_1`))) and `thirdparty_info_period4_1` <= 1e-13)) then
             0.0097764639293613839
         else
             -0.0020767734687120896
         end)
     else
         -0.01430610630061133
     end) + (case when ((`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`)) or ((not (`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`))) and `userinfo_17` <= 1.5000000000000002)) then
         (case when ((`userinfo_5` is null or (`userinfo_5` <> `userinfo_5`)) or ((not (`userinfo_5` is null or (`userinfo_5` <> `userinfo_5`))) and `userinfo_5` <= 2.5000000000000004)) then
             0.00036073772913034152
         else
             0.023781197033135647
         end)
     else
         -0.015123316594501949
     end) + (case when ((`thirdparty_info_period4_2` is null or (`thirdparty_info_period4_2` <> `thirdparty_info_period4_2`)) or ((not (`thirdparty_info_period4_2` is null or (`thirdparty_info_period4_2` <> `thirdparty_info_period4_2`))) and `thirdparty_info_period4_2` <= 1e-13)) then
         0.0065817256383438579
     else
         (case when ((`thirdparty_info_period4_15` is null or (`thirdparty_info_period4_15` <> `thirdparty_info_period4_15`)) or ((not (`thirdparty_info_period4_15` is null or (`thirdparty_info_period4_15` <> `thirdparty_info_period4_15`))) and `thirdparty_info_period4_15` <= 196.50000000000003)) then
             -0.013358450548808791
         else
             0.00062215626769995412
         end)
     end) + (case when ((`userinfo_15` is null or (`userinfo_15` <> `userinfo_15`)) or ((not (`userinfo_15` is null or (`userinfo_15` <> `userinfo_15`))) and `userinfo_15` <= 2.5000000000000004)) then
         -0.011921103204623071
     else
         (case when ((`thirdparty_info_period2_10` is null or (`thirdparty_info_period2_10` <> `thirdparty_info_period2_10`)) or ((not (`thirdparty_info_period2_10` is null or (`thirdparty_info_period2_10` <> `thirdparty_info_period2_10`))) and `thirdparty_info_period2_10` <= 1.5000000000000002)) then
             0.0050863612845005179
         else
             -0.0082268888809492891
         end)
     end) + (case when ((`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`)) or ((not (`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`))) and `webloginfo_15` <= 1.5000000000000002)) then
         (case when ((`thirdparty_info_period6_5` is null or (`thirdparty_info_period6_5` <> `thirdparty_info_period6_5`)) or ((not (`thirdparty_info_period6_5` is null or (`thirdparty_info_period6_5` <> `thirdparty_info_period6_5`))) and `thirdparty_info_period6_5` <= 65.500000000000014)) then
             0.0013701793370216998
         else
             -0.011242556446327946
         end)
     else
         0.0090408201715821337
     end) + (case when ((`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`)) or ((not (`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`))) and `thirdparty_info_period2_3` <= 304.50000000000006)) then
         -0.0033818091052459525
     else
         (case when ((`thirdparty_info_period3_5` is null or (`thirdparty_info_period3_5` <> `thirdparty_info_period3_5`)) or ((not (`thirdparty_info_period3_5` is null or (`thirdparty_info_period3_5` <> `thirdparty_info_period3_5`))) and `thirdparty_info_period3_5` <= 121.50000000000001)) then
             0.017865119595041581
         else
             -0.0037134755196687624
         end)
     end) + (case when ((`thirdparty_info_period3_8` is null or (`thirdparty_info_period3_8` <> `thirdparty_info_period3_8`)) or ((not (`thirdparty_info_period3_8` is null or (`thirdparty_info_period3_8` <> `thirdparty_info_period3_8`))) and `thirdparty_info_period3_8` <= 484.50000000000006)) then
         (case when ((`thirdparty_info_period6_1` is null or (`thirdparty_info_period6_1` <> `thirdparty_info_period6_1`)) or ((not (`thirdparty_info_period6_1` is null or (`thirdparty_info_period6_1` <> `thirdparty_info_period6_1`))) and `thirdparty_info_period6_1` <= 2.5000000000000004)) then
             0.0032741767425172371
         else
             -0.0076982372682245261
         end)
     else
         0.033184163684634727
     end) + (case when ((`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`)) or ((not (`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`))) and `userinfo_17` <= 1.5000000000000002)) then
         (case when ((`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`)) or ((not (`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`))) and `userinfo_14` <= 3.5000000000000004)) then
             -0.0032886604375268144
         else
             0.0067845930587170644
         end)
     else
         -0.014759200942206955
     end) + (case when ((`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`)) or ((not (`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`))) and `thirdparty_info_period1_10` <= 2.5000000000000004)) then
         (case when ((`education_info5` is null or (`education_info5` <> `education_info5`)) or ((not (`education_info5` is null or (`education_info5` <> `education_info5`))) and `education_info5` <= 1e-13)) then
             0.0026010922654924919
         else
             -0.030545665225466513
         end)
     else
         -0.013839412520292471
     end) + (case when ((`education_info1` is null or (`education_info1` <> `education_info1`)) or ((not (`education_info1` is null or (`education_info1` <> `education_info1`))) and `education_info1` <= 1e-13)) then
         (case when ((`education_info5` is null or (`education_info5` <> `education_info5`)) or ((not (`education_info5` is null or (`education_info5` <> `education_info5`))) and `education_info5` <= 1e-13)) then
             0.0017358261688452871
         else
             -0.0322387858938053
         end)
     else
         -0.024293950514334122
     end) + (case when ((`thirdparty_info_period3_10` is null or (`thirdparty_info_period3_10` <> `thirdparty_info_period3_10`)) or ((not (`thirdparty_info_period3_10` is null or (`thirdparty_info_period3_10` <> `thirdparty_info_period3_10`))) and `thirdparty_info_period3_10` <= 2.5000000000000004)) then
         (case when ((`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`)) or ((not (`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`))) and `thirdparty_info_period2_6` <= 3.5000000000000004)) then
             -0.0063241196962790002
         else
             0.004975030657432193
         end)
     else
         -0.015789830898154569
     end) + (case when ((`thirdparty_info_period4_2` is null or (`thirdparty_info_period4_2` <> `thirdparty_info_period4_2`)) or ((not (`thirdparty_info_period4_2` is null or (`thirdparty_info_period4_2` <> `thirdparty_info_period4_2`))) and `thirdparty_info_period4_2` <= 1e-13)) then
         0.0062917444325520716
     else
         (case when ((`thirdparty_info_period4_15` is null or (`thirdparty_info_period4_15` <> `thirdparty_info_period4_15`)) or ((not (`thirdparty_info_period4_15` is null or (`thirdparty_info_period4_15` <> `thirdparty_info_period4_15`))) and `thirdparty_info_period4_15` <= 196.50000000000003)) then
             -0.012525685796968375
         else
             0.00051046088803626281
         end)
     end) + (case when ((`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`)) or ((not (`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`))) and `userinfo_16` <= 1.5000000000000002)) then
         (case when ((`education_info1` is null or (`education_info1` <> `education_info1`)) or ((not (`education_info1` is null or (`education_info1` <> `education_info1`))) and `education_info1` <= 1e-13)) then
             0.0047485458976660247
         else
             -0.022960039421755216
         end)
     else
         -0.0063380930518059488
     end) + (case when ((`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`)) or ((not (`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`))) and `thirdparty_info_period2_3` <= 426.50000000000006)) then
         (case when ((`thirdparty_info_period2_5` is null or (`thirdparty_info_period2_5` <> `thirdparty_info_period2_5`)) or ((not (`thirdparty_info_period2_5` is null or (`thirdparty_info_period2_5` <> `thirdparty_info_period2_5`))) and `thirdparty_info_period2_5` <= 125.50000000000001)) then
             -9.4326104411988066e-05
         else
             -0.019281304070506395
         end)
     else
         0.010376441105425425
     end) + (case when ((`thirdparty_info_period3_9` is null or (`thirdparty_info_period3_9` <> `thirdparty_info_period3_9`)) or ((not (`thirdparty_info_period3_9` is null or (`thirdparty_info_period3_9` <> `thirdparty_info_period3_9`))) and `thirdparty_info_period3_9` <= 1e-13)) then
         (case when ((`thirdparty_info_period1_15` is null or (`thirdparty_info_period1_15` <> `thirdparty_info_period1_15`)) or ((not (`thirdparty_info_period1_15` is null or (`thirdparty_info_period1_15` <> `thirdparty_info_period1_15`))) and `thirdparty_info_period1_15` <= 34.500000000000007)) then
             -0.0064517115270028283
         else
             0.0073490035914934833
         end)
     else
         -0.0065910043948412475
     end) + (case when ((`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`)) or ((not (`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`))) and `webloginfo_15` <= 5.5000000000000009)) then
         (case when ((`socialnetwork_13` is null or (`socialnetwork_13` <> `socialnetwork_13`)) or ((not (`socialnetwork_13` is null or (`socialnetwork_13` <> `socialnetwork_13`))) and `socialnetwork_13` <= 1e-13)) then
             0.0015134587728129103
         else
             -0.012245059715310935
         end)
     else
         0.018206204331140438
     end) + (case when ((`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`)) or ((not (`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`))) and `userinfo_17` <= 1.5000000000000002)) then
         (case when ((`thirdparty_info_period6_5` is null or (`thirdparty_info_period6_5` <> `thirdparty_info_period6_5`)) or ((not (`thirdparty_info_period6_5` is null or (`thirdparty_info_period6_5` <> `thirdparty_info_period6_5`))) and `thirdparty_info_period6_5` <= 75.500000000000014)) then
             0.0045942511385497174
         else
             -0.0061444072001339417
         end)
     else
         -0.013958599489509402
     end) + (case when ((`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`)) or ((not (`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`))) and `thirdparty_info_period2_3` <= 184.50000000000003)) then
         (case when ((`thirdparty_info_period3_3` is null or (`thirdparty_info_period3_3` <> `thirdparty_info_period3_3`)) or ((not (`thirdparty_info_period3_3` is null or (`thirdparty_info_period3_3` <> `thirdparty_info_period3_3`))) and `thirdparty_info_period3_3` <= 264.50000000000006)) then
             -0.0068081548467824023
         else
             0.043445245900617324
         end)
     else
         0.0045723950327347411
     end) + (case when ((`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`)) or ((not (`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`))) and `thirdparty_info_period1_10` <= 4.5000000000000009)) then
         (case when ((`thirdparty_info_period4_6` is null or (`thirdparty_info_period4_6` <> `thirdparty_info_period4_6`)) or ((not (`thirdparty_info_period4_6` is null or (`thirdparty_info_period4_6` <> `thirdparty_info_period4_6`))) and `thirdparty_info_period4_6` <= 40.500000000000007)) then
             -0.0010523135578731594
         else
             0.012784086538521625
         end)
     else
         -0.023858550925708211
     end) + (case when ((`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`)) or ((not (`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`))) and `webloginfo_15` <= 1e-13)) then
         (case when ((`socialnetwork_13` is null or (`socialnetwork_13` <> `socialnetwork_13`)) or ((not (`socialnetwork_13` is null or (`socialnetwork_13` <> `socialnetwork_13`))) and `socialnetwork_13` <= 1e-13)) then
             -0.00050713573413819991
         else
             -0.016999382076130717
         end)
     else
         0.006806568742028795
     end) + (case when ((`thirdparty_info_period5_5` is null or (`thirdparty_info_period5_5` <> `thirdparty_info_period5_5`)) or ((not (`thirdparty_info_period5_5` is null or (`thirdparty_info_period5_5` <> `thirdparty_info_period5_5`))) and `thirdparty_info_period5_5` <= 44.500000000000007)) then
         0.0059577034485222167
     else
         (case when ((`thirdparty_info_period4_3` is null or (`thirdparty_info_period4_3` <> `thirdparty_info_period4_3`)) or ((not (`thirdparty_info_period4_3` is null or (`thirdparty_info_period4_3` <> `thirdparty_info_period4_3`))) and `thirdparty_info_period4_3` <= 242.50000000000003)) then
             -0.011587625650905306
         else
             0.0038885358563291728
         end)
     end) + (case when ((`thirdparty_info_period3_1` is null or (`thirdparty_info_period3_1` <> `thirdparty_info_period3_1`)) or ((not (`thirdparty_info_period3_1` is null or (`thirdparty_info_period3_1` <> `thirdparty_info_period3_1`))) and `thirdparty_info_period3_1` <= 1e-13)) then
         (case when ((`thirdparty_info_period1_1` is null or (`thirdparty_info_period1_1` <> `thirdparty_info_period1_1`)) or ((not (`thirdparty_info_period1_1` is null or (`thirdparty_info_period1_1` <> `thirdparty_info_period1_1`))) and `thirdparty_info_period1_1` <= 4.5000000000000009)) then
             0.00071456118504376813
         else
             0.026886139004318868
         end)
     else
         -0.0027676520587518578
     end) + (case when ((`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`)) or ((not (`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`))) and `thirdparty_info_period1_10` <= 4.5000000000000009)) then
         (case when ((`education_info5` is null or (`education_info5` <> `education_info5`)) or ((not (`education_info5` is null or (`education_info5` <> `education_info5`))) and `education_info5` <= 1e-13)) then
             0.001596031176573182
         else
             -0.02963619427115155
         end)
     else
         -0.023757918256384718
     end) + (case when ((`thirdparty_info_period3_2` is null or (`thirdparty_info_period3_2` <> `thirdparty_info_period3_2`)) or ((not (`thirdparty_info_period3_2` is null or (`thirdparty_info_period3_2` <> `thirdparty_info_period3_2`))) and `thirdparty_info_period3_2` <= 1e-13)) then
         (case when ((`thirdparty_info_period1_2` is null or (`thirdparty_info_period1_2` <> `thirdparty_info_period1_2`)) or ((not (`thirdparty_info_period1_2` is null or (`thirdparty_info_period1_2` <> `thirdparty_info_period1_2`))) and `thirdparty_info_period1_2` <= 8.5000000000000018)) then
             0.0020258916904842559
         else
             0.025330021211679012
         end)
     else
         -0.0030547203244139986
     end) + (case when ((`thirdparty_info_period2_9` is null or (`thirdparty_info_period2_9` <> `thirdparty_info_period2_9`)) or ((not (`thirdparty_info_period2_9` is null or (`thirdparty_info_period2_9` <> `thirdparty_info_period2_9`))) and `thirdparty_info_period2_9` <= 1e-13)) then
         (case when ((`education_info5` is null or (`education_info5` <> `education_info5`)) or ((not (`education_info5` is null or (`education_info5` <> `education_info5`))) and `education_info5` <= 1e-13)) then
             0.0046464508274316101
         else
             -0.028143875868354887
         end)
     else
         -0.0055377765116291864
     end) + (case when ((`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`)) or ((not (`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`))) and `userinfo_17` <= 1.5000000000000002)) then
         (case when ((`userinfo_5` is null or (`userinfo_5` <> `userinfo_5`)) or ((not (`userinfo_5` is null or (`userinfo_5` <> `userinfo_5`))) and `userinfo_5` <= 2.5000000000000004)) then
             0.00022618999187618349
         else
             0.021106220837556679
         end)
     else
         -0.013466562625759499
     end) + (case when ((`education_info1` is null or (`education_info1` <> `education_info1`)) or ((not (`education_info1` is null or (`education_info1` <> `education_info1`))) and `education_info1` <= 1e-13)) then
         (case when ((`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`)) or ((not (`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`))) and `userinfo_16` <= 1.5000000000000002)) then
             0.004273705340407611
         else
             -0.0054136881714771526
         end)
     else
         -0.022589815344294391
     end) + (case when ((`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`)) or ((not (`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`))) and `thirdparty_info_period2_3` <= 437.50000000000006)) then
         (case when ((`thirdparty_info_period2_5` is null or (`thirdparty_info_period2_5` <> `thirdparty_info_period2_5`)) or ((not (`thirdparty_info_period2_5` is null or (`thirdparty_info_period2_5` <> `thirdparty_info_period2_5`))) and `thirdparty_info_period2_5` <= 125.50000000000001)) then
             0.00020677745090532849
         else
             -0.018628437447235125
         end)
     else
         0.0099032819963762939
     end) + (case when ((`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`)) or ((not (`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`))) and `thirdparty_info_period2_3` <= 184.50000000000003)) then
         (case when ((`thirdparty_info_period5_3` is null or (`thirdparty_info_period5_3` <> `thirdparty_info_period5_3`)) or ((not (`thirdparty_info_period5_3` is null or (`thirdparty_info_period5_3` <> `thirdparty_info_period5_3`))) and `thirdparty_info_period5_3` <= 312.50000000000006)) then
             -0.0062948049697502638
         else
             0.044555787144565678
         end)
     else
         0.0041493855572431954
     end) + (case when ((`thirdparty_info_period5_5` is null or (`thirdparty_info_period5_5` <> `thirdparty_info_period5_5`)) or ((not (`thirdparty_info_period5_5` is null or (`thirdparty_info_period5_5` <> `thirdparty_info_period5_5`))) and `thirdparty_info_period5_5` <= 44.500000000000007)) then
         0.0057914500722230861
     else
         (case when ((`thirdparty_info_period5_3` is null or (`thirdparty_info_period5_3` <> `thirdparty_info_period5_3`)) or ((not (`thirdparty_info_period5_3` is null or (`thirdparty_info_period5_3` <> `thirdparty_info_period5_3`))) and `thirdparty_info_period5_3` <= 248.50000000000003)) then
             -0.010922441459638603
         else
             0.0038872923725846715
         end)
     end) + (case when ((`thirdparty_info_period2_10` is null or (`thirdparty_info_period2_10` <> `thirdparty_info_period2_10`)) or ((not (`thirdparty_info_period2_10` is null or (`thirdparty_info_period2_10` <> `thirdparty_info_period2_10`))) and `thirdparty_info_period2_10` <= 1.5000000000000002)) then
         (case when ((`thirdparty_info_period6_5` is null or (`thirdparty_info_period6_5` <> `thirdparty_info_period6_5`)) or ((not (`thirdparty_info_period6_5` is null or (`thirdparty_info_period6_5` <> `thirdparty_info_period6_5`))) and `thirdparty_info_period6_5` <= 83.500000000000014)) then
             0.004774970215925026
         else
             -0.0071016514253969473
         end)
     else
         -0.0087458931610403367
     end) + (case when ((`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`)) or ((not (`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`))) and `webloginfo_15` <= 1e-13)) then
         (case when ((`socialnetwork_13` is null or (`socialnetwork_13` <> `socialnetwork_13`)) or ((not (`socialnetwork_13` is null or (`socialnetwork_13` <> `socialnetwork_13`))) and `socialnetwork_13` <= 1e-13)) then
             -0.00044977003720687815
         else
             -0.015928615310698651
         end)
     else
         0.0062171465686190232
     end) + (case when ((`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`)) or ((not (`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`))) and `userinfo_14` <= 2.5000000000000004)) then
         -0.010187419697623329
     else
         (case when ((`thirdparty_info_period3_5` is null or (`thirdparty_info_period3_5` <> `thirdparty_info_period3_5`)) or ((not (`thirdparty_info_period3_5` is null or (`thirdparty_info_period3_5` <> `thirdparty_info_period3_5`))) and `thirdparty_info_period3_5` <= 133.50000000000003)) then
             0.0038386196750917773
         else
             -0.008691589879221898
         end)
     end) + (case when ((`thirdparty_info_period3_8` is null or (`thirdparty_info_period3_8` <> `thirdparty_info_period3_8`)) or ((not (`thirdparty_info_period3_8` is null or (`thirdparty_info_period3_8` <> `thirdparty_info_period3_8`))) and `thirdparty_info_period3_8` <= 484.50000000000006)) then
         (case when ((`thirdparty_info_period5_5` is null or (`thirdparty_info_period5_5` <> `thirdparty_info_period5_5`)) or ((not (`thirdparty_info_period5_5` is null or (`thirdparty_info_period5_5` <> `thirdparty_info_period5_5`))) and `thirdparty_info_period5_5` <= 46.500000000000007)) then
             0.0051625787378938711
         else
             -0.0046384979171851751
         end)
     else
         0.02838025133734683
     end) + (case when ((`thirdparty_info_period4_15` is null or (`thirdparty_info_period4_15` <> `thirdparty_info_period4_15`)) or ((not (`thirdparty_info_period4_15` is null or (`thirdparty_info_period4_15` <> `thirdparty_info_period4_15`))) and `thirdparty_info_period4_15` <= 528.50000000000011)) then
         (case when ((`thirdparty_info_period5_5` is null or (`thirdparty_info_period5_5` <> `thirdparty_info_period5_5`)) or ((not (`thirdparty_info_period5_5` is null or (`thirdparty_info_period5_5` <> `thirdparty_info_period5_5`))) and `thirdparty_info_period5_5` <= 53.500000000000007)) then
             0.002419226020504579
         else
             -0.013241066615066197
         end)
     else
         0.0045191934514959677
     end) + (case when ((`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`)) or ((not (`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`))) and `thirdparty_info_period2_3` <= 184.50000000000003)) then
         (case when ((`thirdparty_info_period5_3` is null or (`thirdparty_info_period5_3` <> `thirdparty_info_period5_3`)) or ((not (`thirdparty_info_period5_3` is null or (`thirdparty_info_period5_3` <> `thirdparty_info_period5_3`))) and `thirdparty_info_period5_3` <= 312.50000000000006)) then
             -0.0061856668984385755
         else
             0.04061796600417978
         end)
     else
         0.0040008716709551894
     end) + (case when ((`thirdparty_info_period2_10` is null or (`thirdparty_info_period2_10` <> `thirdparty_info_period2_10`)) or ((not (`thirdparty_info_period2_10` is null or (`thirdparty_info_period2_10` <> `thirdparty_info_period2_10`))) and `thirdparty_info_period2_10` <= 4.5000000000000009)) then
         (case when ((`thirdparty_info_period3_15` is null or (`thirdparty_info_period3_15` <> `thirdparty_info_period3_15`)) or ((not (`thirdparty_info_period3_15` is null or (`thirdparty_info_period3_15` <> `thirdparty_info_period3_15`))) and `thirdparty_info_period3_15` <= 361.50000000000006)) then
             -0.0042492021976995708
         else
             0.0045941917009074927
         end)
     else
         -0.022126345318072317
     end) + (case when ((`thirdparty_info_period3_1` is null or (`thirdparty_info_period3_1` <> `thirdparty_info_period3_1`)) or ((not (`thirdparty_info_period3_1` is null or (`thirdparty_info_period3_1` <> `thirdparty_info_period3_1`))) and `thirdparty_info_period3_1` <= 1e-13)) then
         (case when ((`thirdparty_info_period1_1` is null or (`thirdparty_info_period1_1` <> `thirdparty_info_period1_1`)) or ((not (`thirdparty_info_period1_1` is null or (`thirdparty_info_period1_1` <> `thirdparty_info_period1_1`))) and `thirdparty_info_period1_1` <= 4.5000000000000009)) then
             0.0008293104857805488
         else
             0.024269030091077053
         end)
     else
         -0.0026179653779725785
     end) + (case when ((`education_info1` is null or (`education_info1` <> `education_info1`)) or ((not (`education_info1` is null or (`education_info1` <> `education_info1`))) and `education_info1` <= 1e-13)) then
         (case when ((`education_info5` is null or (`education_info5` <> `education_info5`)) or ((not (`education_info5` is null or (`education_info5` <> `education_info5`))) and `education_info5` <= 1e-13)) then
             0.0014971048995832065
         else
             -0.029416370543376827
         end)
     else
         -0.02192846194816209
     end) + (case when ((`thirdparty_info_period3_2` is null or (`thirdparty_info_period3_2` <> `thirdparty_info_period3_2`)) or ((not (`thirdparty_info_period3_2` is null or (`thirdparty_info_period3_2` <> `thirdparty_info_period3_2`))) and `thirdparty_info_period3_2` <= 1e-13)) then
         (case when ((`thirdparty_info_period1_2` is null or (`thirdparty_info_period1_2` <> `thirdparty_info_period1_2`)) or ((not (`thirdparty_info_period1_2` is null or (`thirdparty_info_period1_2` <> `thirdparty_info_period1_2`))) and `thirdparty_info_period1_2` <= 8.5000000000000018)) then
             0.0020543344721166258
         else
             0.02298887814514541
         end)
     else
         -0.0028432735702687431
     end) + (case when ((`thirdparty_info_period3_10` is null or (`thirdparty_info_period3_10` <> `thirdparty_info_period3_10`)) or ((not (`thirdparty_info_period3_10` is null or (`thirdparty_info_period3_10` <> `thirdparty_info_period3_10`))) and `thirdparty_info_period3_10` <= 2.5000000000000004)) then
         (case when ((`userinfo_18` is null or (`userinfo_18` <> `userinfo_18`)) or ((not (`userinfo_18` is null or (`userinfo_18` <> `userinfo_18`))) and `userinfo_18` <= 21.500000000000004)) then
             -0.018057153372347364
         else
             0.0021630491332428662
         end)
     else
         -0.013897776392685555
     end) + (case when ((`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`)) or ((not (`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`))) and `thirdparty_info_period1_10` <= 4.5000000000000009)) then
         (case when ((`userinfo_5` is null or (`userinfo_5` <> `userinfo_5`)) or ((not (`userinfo_5` is null or (`userinfo_5` <> `userinfo_5`))) and `userinfo_5` <= 2.5000000000000004)) then
             -0.00028880876171279455
         else
             0.017340894250731233
         end)
     else
         -0.022451707849546199
     end) + (case when ((`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`)) or ((not (`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`))) and `userinfo_17` <= 1.5000000000000002)) then
         (case when ((`thirdparty_info_period3_5` is null or (`thirdparty_info_period3_5` <> `thirdparty_info_period3_5`)) or ((not (`thirdparty_info_period3_5` is null or (`thirdparty_info_period3_5` <> `thirdparty_info_period3_5`))) and `thirdparty_info_period3_5` <= 162.50000000000003)) then
             0.0028677291263015745
         else
             -0.011355558932915835
         end)
     else
         -0.012717706235491592
     end) + (case when ((`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`)) or ((not (`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`))) and `webloginfo_15` <= 1e-13)) then
         (case when ((`socialnetwork_13` is null or (`socialnetwork_13` <> `socialnetwork_13`)) or ((not (`socialnetwork_13` is null or (`socialnetwork_13` <> `socialnetwork_13`))) and `socialnetwork_13` <= 1e-13)) then
             -0.00063649844233996467
         else
             -0.015260610286578694
         end)
     else
         0.0057162122803048002
     end) + (case when ((`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`)) or ((not (`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`))) and `thirdparty_info_period2_3` <= 184.50000000000003)) then
         (case when ((`thirdparty_info_period3_3` is null or (`thirdparty_info_period3_3` <> `thirdparty_info_period3_3`)) or ((not (`thirdparty_info_period3_3` is null or (`thirdparty_info_period3_3` <> `thirdparty_info_period3_3`))) and `thirdparty_info_period3_3` <= 264.50000000000006)) then
             -0.0062399476316512686
         else
             0.038118578677572089
         end)
     else
         0.0036786625780627843
     end) + (case when ((`thirdparty_info_period5_8` is null or (`thirdparty_info_period5_8` <> `thirdparty_info_period5_8`)) or ((not (`thirdparty_info_period5_8` is null or (`thirdparty_info_period5_8` <> `thirdparty_info_period5_8`))) and `thirdparty_info_period5_8` <= 488.50000000000006)) then
         (case when ((`thirdparty_info_period5_1` is null or (`thirdparty_info_period5_1` <> `thirdparty_info_period5_1`)) or ((not (`thirdparty_info_period5_1` is null or (`thirdparty_info_period5_1` <> `thirdparty_info_period5_1`))) and `thirdparty_info_period5_1` <= 5.5000000000000009)) then
             0.0031977975092339055
         else
             -0.0056297965770866227
         end)
     else
         0.031523777166612227
     end) + (case when ((`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`)) or ((not (`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`))) and `webloginfo_15` <= 5.5000000000000009)) then
         -0.0012766497571899519
     else
         (case when ((`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`)) or ((not (`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`))) and `thirdparty_info_period2_6` <= 33.500000000000007)) then
             0.0029246613047291844
         else
             0.03947781581478798
         end)
     end) + (case when ((`thirdparty_info_period4_14` is null or (`thirdparty_info_period4_14` <> `thirdparty_info_period4_14`)) or ((not (`thirdparty_info_period4_14` is null or (`thirdparty_info_period4_14` <> `thirdparty_info_period4_14`))) and `thirdparty_info_period4_14` <= 4409.5000000000009)) then
         0.0077359041129074577
     else
         (case when ((`thirdparty_info_period4_15` is null or (`thirdparty_info_period4_15` <> `thirdparty_info_period4_15`)) or ((not (`thirdparty_info_period4_15` is null or (`thirdparty_info_period4_15` <> `thirdparty_info_period4_15`))) and `thirdparty_info_period4_15` <= 196.50000000000003)) then
             -0.0121273089882806
         else
             0.0016754237155456955
         end)
     end) + (case when ((`thirdparty_info_period6_14` is null or (`thirdparty_info_period6_14` <> `thirdparty_info_period6_14`)) or ((not (`thirdparty_info_period6_14` is null or (`thirdparty_info_period6_14` <> `thirdparty_info_period6_14`))) and `thirdparty_info_period6_14` <= 2351.5000000000005)) then
         0.0045918098066176204
     else
         (case when ((`thirdparty_info_period6_15` is null or (`thirdparty_info_period6_15` <> `thirdparty_info_period6_15`)) or ((not (`thirdparty_info_period6_15` is null or (`thirdparty_info_period6_15` <> `thirdparty_info_period6_15`))) and `thirdparty_info_period6_15` <= 192.50000000000003)) then
             -0.012836163911457319
         else
             0.0012836480479917489
         end)
     end) + (case when ((`userinfo_18` is null or (`userinfo_18` <> `userinfo_18`)) or ((not (`userinfo_18` is null or (`userinfo_18` <> `userinfo_18`))) and `userinfo_18` <= 21.500000000000004)) then
         -0.018811305250413336
     else
         (case when ((`thirdparty_info_period4_5` is null or (`thirdparty_info_period4_5` <> `thirdparty_info_period4_5`)) or ((not (`thirdparty_info_period4_5` is null or (`thirdparty_info_period4_5` <> `thirdparty_info_period4_5`))) and `thirdparty_info_period4_5` <= 57.500000000000007)) then
             0.006186530180908761
         else
             -0.0030349127487054703
         end)
     end) + (case when ((`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`)) or ((not (`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`))) and `thirdparty_info_period1_10` <= 2.5000000000000004)) then
         (case when ((`thirdparty_info_period1_5` is null or (`thirdparty_info_period1_5` <> `thirdparty_info_period1_5`)) or ((not (`thirdparty_info_period1_5` is null or (`thirdparty_info_period1_5` <> `thirdparty_info_period1_5`))) and `thirdparty_info_period1_5` <= 153.50000000000003)) then
             0.0025734802661918931
         else
             -0.017289807874116117
         end)
     else
         -0.011564406125410763
     end) + (case when ((`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`)) or ((not (`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`))) and `thirdparty_info_period2_3` <= 184.50000000000003)) then
         -0.0043782225086474212
     else
         (case when ((`thirdparty_info_period3_4` is null or (`thirdparty_info_period3_4` <> `thirdparty_info_period3_4`)) or ((not (`thirdparty_info_period3_4` is null or (`thirdparty_info_period3_4` <> `thirdparty_info_period3_4`))) and `thirdparty_info_period3_4` <= 190.50000000000003)) then
             0.015253938610060629
         else
             -0.0011233838707160567
         end)
     end) + (case when ((`thirdparty_info_period1_9` is null or (`thirdparty_info_period1_9` <> `thirdparty_info_period1_9`)) or ((not (`thirdparty_info_period1_9` is null or (`thirdparty_info_period1_9` <> `thirdparty_info_period1_9`))) and `thirdparty_info_period1_9` <= 1e-13)) then
         (case when ((`userinfo_5` is null or (`userinfo_5` <> `userinfo_5`)) or ((not (`userinfo_5` is null or (`userinfo_5` <> `userinfo_5`))) and `userinfo_5` <= 2.5000000000000004)) then
             0.0018169219694871596
         else
             0.024916985962203098
         end)
     else
         -0.004790784464243962
     end) + (case when ((`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`)) or ((not (`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`))) and `userinfo_17` <= 1.5000000000000002)) then
         (case when ((`education_info1` is null or (`education_info1` <> `education_info1`)) or ((not (`education_info1` is null or (`education_info1` <> `education_info1`))) and `education_info1` <= 1e-13)) then
             0.0020851416657608024
         else
             -0.02060290397881831
         end)
     else
         -0.012585579851274337
     end) + (case when ((`thirdparty_info_period4_3` is null or (`thirdparty_info_period4_3` <> `thirdparty_info_period4_3`)) or ((not (`thirdparty_info_period4_3` is null or (`thirdparty_info_period4_3` <> `thirdparty_info_period4_3`))) and `thirdparty_info_period4_3` <= 339.50000000000006)) then
         -0.0023052724836301504
     else
         (case when ((`thirdparty_info_period2_7` is null or (`thirdparty_info_period2_7` <> `thirdparty_info_period2_7`)) or ((not (`thirdparty_info_period2_7` is null or (`thirdparty_info_period2_7` <> `thirdparty_info_period2_7`))) and `thirdparty_info_period2_7` <= 159.50000000000003)) then
             0.080396157135723026
         else
             0.005339549857086289
         end)
     end) + (case when ((`thirdparty_info_period2_10` is null or (`thirdparty_info_period2_10` <> `thirdparty_info_period2_10`)) or ((not (`thirdparty_info_period2_10` is null or (`thirdparty_info_period2_10` <> `thirdparty_info_period2_10`))) and `thirdparty_info_period2_10` <= 4.5000000000000009)) then
         (case when ((`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`)) or ((not (`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`))) and `userinfo_16` <= 1.5000000000000002)) then
             0.0036984343151158366
         else
             -0.0049623153195366282
         end)
     else
         -0.020870659255877902
     end) + (case when ((`thirdparty_info_period6_1` is null or (`thirdparty_info_period6_1` <> `thirdparty_info_period6_1`)) or ((not (`thirdparty_info_period6_1` is null or (`thirdparty_info_period6_1` <> `thirdparty_info_period6_1`))) and `thirdparty_info_period6_1` <= 2.5000000000000004)) then
         0.0028742701089020865
     else
         (case when ((`thirdparty_info_period3_8` is null or (`thirdparty_info_period3_8` <> `thirdparty_info_period3_8`)) or ((not (`thirdparty_info_period3_8` is null or (`thirdparty_info_period3_8` <> `thirdparty_info_period3_8`))) and `thirdparty_info_period3_8` <= 484.50000000000006)) then
             -0.0063110675631637969
         else
             0.0323095900542631
         end)
     end) + (case when ((`thirdparty_info_period3_2` is null or (`thirdparty_info_period3_2` <> `thirdparty_info_period3_2`)) or ((not (`thirdparty_info_period3_2` is null or (`thirdparty_info_period3_2` <> `thirdparty_info_period3_2`))) and `thirdparty_info_period3_2` <= 1e-13)) then
         (case when ((`thirdparty_info_period6_14` is null or (`thirdparty_info_period6_14` <> `thirdparty_info_period6_14`)) or ((not (`thirdparty_info_period6_14` is null or (`thirdparty_info_period6_14` <> `thirdparty_info_period6_14`))) and `thirdparty_info_period6_14` <= 1005.5000000000001)) then
             0.013269688037714356
         else
             -0.0012956177135207518
         end)
     else
         -0.002583251316282308
     end) + (case when ((`thirdparty_info_period4_3` is null or (`thirdparty_info_period4_3` <> `thirdparty_info_period4_3`)) or ((not (`thirdparty_info_period4_3` is null or (`thirdparty_info_period4_3` <> `thirdparty_info_period4_3`))) and `thirdparty_info_period4_3` <= 339.50000000000006)) then
         (case when ((`thirdparty_info_period4_5` is null or (`thirdparty_info_period4_5` <> `thirdparty_info_period4_5`)) or ((not (`thirdparty_info_period4_5` is null or (`thirdparty_info_period4_5` <> `thirdparty_info_period4_5`))) and `thirdparty_info_period4_5` <= 57.500000000000007)) then
             0.0035853920150453107
         else
             -0.0091650330279537465
         end)
     else
         0.007203699779225828
     end) + (case when ((`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`)) or ((not (`userinfo_14` is null or (`userinfo_14` <> `userinfo_14`))) and `userinfo_14` <= 2.5000000000000004)) then
         -0.0093438263394334392
     else
         (case when ((`thirdparty_info_period3_5` is null or (`thirdparty_info_period3_5` <> `thirdparty_info_period3_5`)) or ((not (`thirdparty_info_period3_5` is null or (`thirdparty_info_period3_5` <> `thirdparty_info_period3_5`))) and `thirdparty_info_period3_5` <= 133.50000000000003)) then
             0.0033458638684606256
         else
             -0.008258698738223276
         end)
     end) + (case when ((`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`)) or ((not (`thirdparty_info_period2_6` is null or (`thirdparty_info_period2_6` <> `thirdparty_info_period2_6`))) and `thirdparty_info_period2_6` <= 2.5000000000000004)) then
         (case when ((`thirdparty_info_period3_6` is null or (`thirdparty_info_period3_6` <> `thirdparty_info_period3_6`)) or ((not (`thirdparty_info_period3_6` is null or (`thirdparty_info_period3_6` <> `thirdparty_info_period3_6`))) and `thirdparty_info_period3_6` <= 4.5000000000000009)) then
             -0.011774122251315258
         else
             0.01147273651151509
         end)
     else
         0.0020981184267027677
     end) + (case when ((`thirdparty_info_period3_8` is null or (`thirdparty_info_period3_8` <> `thirdparty_info_period3_8`)) or ((not (`thirdparty_info_period3_8` is null or (`thirdparty_info_period3_8` <> `thirdparty_info_period3_8`))) and `thirdparty_info_period3_8` <= 484.50000000000006)) then
         (case when ((`thirdparty_info_period3_5` is null or (`thirdparty_info_period3_5` <> `thirdparty_info_period3_5`)) or ((not (`thirdparty_info_period3_5` is null or (`thirdparty_info_period3_5` <> `thirdparty_info_period3_5`))) and `thirdparty_info_period3_5` <= 121.50000000000001)) then
             0.0015520738811285514
         else
             -0.0096134482666225887
         end)
     else
         0.024950135277146963
     end) + (case when ((`education_info5` is null or (`education_info5` <> `education_info5`)) or ((not (`education_info5` is null or (`education_info5` <> `education_info5`))) and `education_info5` <= 1e-13)) then
         (case when ((`webloginfo_17` is null or (`webloginfo_17` <> `webloginfo_17`)) or ((not (`webloginfo_17` is null or (`webloginfo_17` <> `webloginfo_17`))) and `webloginfo_17` <= 6.5000000000000009)) then
             -0.0019679186714506047
         else
             0.0072410570640366913
         end)
     else
         -0.026145728209452226
     end) + (case when ((`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`)) or ((not (`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`))) and `thirdparty_info_period2_3` <= 304.50000000000006)) then
         -0.0026172873523970701
     else
         (case when ((`thirdparty_info_period3_4` is null or (`thirdparty_info_period3_4` <> `thirdparty_info_period3_4`)) or ((not (`thirdparty_info_period3_4` is null or (`thirdparty_info_period3_4` <> `thirdparty_info_period3_4`))) and `thirdparty_info_period3_4` <= 296.50000000000006)) then
             0.01688142659907307
         else
             -0.0015279116896172839
         end)
     end) + (case when ((`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`)) or ((not (`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`))) and `thirdparty_info_period1_10` <= 4.5000000000000009)) then
         (case when ((`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`)) or ((not (`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`))) and `webloginfo_15` <= 1e-13)) then
             -0.0021321870982036846
         else
             0.0061577217998026387
         end)
     else
         -0.020855506765355903
     end) + (case when ((`userinfo_18` is null or (`userinfo_18` <> `userinfo_18`)) or ((not (`userinfo_18` is null or (`userinfo_18` <> `userinfo_18`))) and `userinfo_18` <= 21.500000000000004)) then
         -0.017813217758165564
     else
         (case when ((`education_info1` is null or (`education_info1` <> `education_info1`)) or ((not (`education_info1` is null or (`education_info1` <> `education_info1`))) and `education_info1` <= 1e-13)) then
             0.0016060684024233247
         else
             -0.020327933625446559
         end)
     end) + (case when ((`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`)) or ((not (`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`))) and `userinfo_17` <= 1.5000000000000002)) then
         (case when ((`thirdparty_info_period2_5` is null or (`thirdparty_info_period2_5` <> `thirdparty_info_period2_5`)) or ((not (`thirdparty_info_period2_5` is null or (`thirdparty_info_period2_5` <> `thirdparty_info_period2_5`))) and `thirdparty_info_period2_5` <= 170.50000000000003)) then
             0.0025270567968915564
         else
             -0.01081154615131423
         end)
     else
         -0.011494456358807597
     end) + (case when ((`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`)) or ((not (`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`))) and `thirdparty_info_period2_3` <= 486.50000000000006)) then
         (case when ((`thirdparty_info_period2_5` is null or (`thirdparty_info_period2_5` <> `thirdparty_info_period2_5`)) or ((not (`thirdparty_info_period2_5` is null or (`thirdparty_info_period2_5` <> `thirdparty_info_period2_5`))) and `thirdparty_info_period2_5` <= 138.50000000000003)) then
             0.00016139941785549188
         else
             -0.01739340848118447
         end)
     else
         0.0094828698888913265
     end) + (case when ((`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`)) or ((not (`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`))) and `thirdparty_info_period2_3` <= 145.50000000000003)) then
         (case when ((`thirdparty_info_period4_3` is null or (`thirdparty_info_period4_3` <> `thirdparty_info_period4_3`)) or ((not (`thirdparty_info_period4_3` is null or (`thirdparty_info_period4_3` <> `thirdparty_info_period4_3`))) and `thirdparty_info_period4_3` <= 246.50000000000003)) then
             -0.0067975429395147257
         else
             0.036922603767843697
         end)
     else
         0.0028884031437670064
     end) + (case when ((`thirdparty_info_period3_2` is null or (`thirdparty_info_period3_2` <> `thirdparty_info_period3_2`)) or ((not (`thirdparty_info_period3_2` is null or (`thirdparty_info_period3_2` <> `thirdparty_info_period3_2`))) and `thirdparty_info_period3_2` <= 1e-13)) then
         (case when ((`thirdparty_info_period1_2` is null or (`thirdparty_info_period1_2` <> `thirdparty_info_period1_2`)) or ((not (`thirdparty_info_period1_2` is null or (`thirdparty_info_period1_2` <> `thirdparty_info_period1_2`))) and `thirdparty_info_period1_2` <= 5.5000000000000009)) then
             0.0012140540782377566
         else
             0.018412327014905971
         end)
     else
         -0.0023812035540704221
     end) + (case when ((`socialnetwork_8` is null or (`socialnetwork_8` <> `socialnetwork_8`)) or ((not (`socialnetwork_8` is null or (`socialnetwork_8` <> `socialnetwork_8`))) and `socialnetwork_8` <= 133.50000000000003)) then
         (case when ((`thirdparty_info_period4_9` is null or (`thirdparty_info_period4_9` <> `thirdparty_info_period4_9`)) or ((not (`thirdparty_info_period4_9` is null or (`thirdparty_info_period4_9` <> `thirdparty_info_period4_9`))) and `thirdparty_info_period4_9` <= 1.5000000000000002)) then
             0.00317203394476073
         else
             -0.00634472079565608
         end)
     else
         -0.014804709501878611
     end) + (case when ((`userinfo_18` is null or (`userinfo_18` <> `userinfo_18`)) or ((not (`userinfo_18` is null or (`userinfo_18` <> `userinfo_18`))) and `userinfo_18` <= 21.500000000000004)) then
         -0.0173884500988368
     else
         (case when ((`thirdparty_info_period6_5` is null or (`thirdparty_info_period6_5` <> `thirdparty_info_period6_5`)) or ((not (`thirdparty_info_period6_5` is null or (`thirdparty_info_period6_5` <> `thirdparty_info_period6_5`))) and `thirdparty_info_period6_5` <= 81.500000000000014)) then
             0.0030875004591237338
         else
             -0.0064805465637732627
         end)
     end) + (case when ((`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`)) or ((not (`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`))) and `thirdparty_info_period2_3` <= 145.50000000000003)) then
         (case when ((`thirdparty_info_period3_3` is null or (`thirdparty_info_period3_3` <> `thirdparty_info_period3_3`)) or ((not (`thirdparty_info_period3_3` is null or (`thirdparty_info_period3_3` <> `thirdparty_info_period3_3`))) and `thirdparty_info_period3_3` <= 264.50000000000006)) then
             -0.0061525068742399654
         else
             0.050866459338786411
         end)
     else
         0.0027321223768814948
     end) + (case when ((`thirdparty_info_period2_9` is null or (`thirdparty_info_period2_9` <> `thirdparty_info_period2_9`)) or ((not (`thirdparty_info_period2_9` is null or (`thirdparty_info_period2_9` <> `thirdparty_info_period2_9`))) and `thirdparty_info_period2_9` <= 1e-13)) then
         0.0029179793625941993
     else
         (case when ((`thirdparty_info_period2_13` is null or (`thirdparty_info_period2_13` <> `thirdparty_info_period2_13`)) or ((not (`thirdparty_info_period2_13` is null or (`thirdparty_info_period2_13` <> `thirdparty_info_period2_13`))) and `thirdparty_info_period2_13` <= 37733.500000000007)) then
             -0.0085018632238527021
         else
             0.0055867644825081126
         end)
     end) + (case when ((`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`)) or ((not (`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`))) and `userinfo_16` <= 1.5000000000000002)) then
         (case when ((`thirdparty_info_period4_8` is null or (`thirdparty_info_period4_8` <> `thirdparty_info_period4_8`)) or ((not (`thirdparty_info_period4_8` is null or (`thirdparty_info_period4_8` <> `thirdparty_info_period4_8`))) and `thirdparty_info_period4_8` <= 372.50000000000006)) then
             0.0015755624915684216
         else
             0.023759768055732503
         end)
     else
         -0.0052788681262849208
     end) + (case when ((`thirdparty_info_period2_10` is null or (`thirdparty_info_period2_10` <> `thirdparty_info_period2_10`)) or ((not (`thirdparty_info_period2_10` is null or (`thirdparty_info_period2_10` <> `thirdparty_info_period2_10`))) and `thirdparty_info_period2_10` <= 4.5000000000000009)) then
         0.00075315945816512627
     else
         (case when ((`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`)) or ((not (`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`))) and `thirdparty_info_period2_3` <= 942.50000000000011)) then
             -0.024377691819540435
         else
             0.072660117152298087
         end)
     end) + (case when ((`thirdparty_info_period1_9` is null or (`thirdparty_info_period1_9` <> `thirdparty_info_period1_9`)) or ((not (`thirdparty_info_period1_9` is null or (`thirdparty_info_period1_9` <> `thirdparty_info_period1_9`))) and `thirdparty_info_period1_9` <= 1e-13)) then
         (case when ((`userinfo_5` is null or (`userinfo_5` <> `userinfo_5`)) or ((not (`userinfo_5` is null or (`userinfo_5` <> `userinfo_5`))) and `userinfo_5` <= 2.5000000000000004)) then
             0.0016279377665722496
         else
             0.02332406561265284
         end)
     else
         -0.0042170014016568343
     end) + (case when ((`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`)) or ((not (`webloginfo_15` is null or (`webloginfo_15` <> `webloginfo_15`))) and `webloginfo_15` <= 5.5000000000000009)) then
         (case when ((`socialnetwork_13` is null or (`socialnetwork_13` <> `socialnetwork_13`)) or ((not (`socialnetwork_13` is null or (`socialnetwork_13` <> `socialnetwork_13`))) and `socialnetwork_13` <= 1e-13)) then
             0.0012585302930994318
         else
             -0.010369513116113196
         end)
     else
         0.013502240814590172
     end) + (case when ((`webloginfo_17` is null or (`webloginfo_17` <> `webloginfo_17`)) or ((not (`webloginfo_17` is null or (`webloginfo_17` <> `webloginfo_17`))) and `webloginfo_17` <= 6.5000000000000009)) then
         -0.0023110107993791337
     else
         (case when ((`thirdparty_info_period5_3` is null or (`thirdparty_info_period5_3` <> `thirdparty_info_period5_3`)) or ((not (`thirdparty_info_period5_3` is null or (`thirdparty_info_period5_3` <> `thirdparty_info_period5_3`))) and `thirdparty_info_period5_3` <= 307.50000000000006)) then
             0.0019449285609586299
         else
             0.021175407944136859
         end)
     end) + (case when ((`thirdparty_info_period3_1` is null or (`thirdparty_info_period3_1` <> `thirdparty_info_period3_1`)) or ((not (`thirdparty_info_period3_1` is null or (`thirdparty_info_period3_1` <> `thirdparty_info_period3_1`))) and `thirdparty_info_period3_1` <= 1e-13)) then
         (case when ((`thirdparty_info_period1_1` is null or (`thirdparty_info_period1_1` <> `thirdparty_info_period1_1`)) or ((not (`thirdparty_info_period1_1` is null or (`thirdparty_info_period1_1` <> `thirdparty_info_period1_1`))) and `thirdparty_info_period1_1` <= 4.5000000000000009)) then
             0.0002056275424193977
         else
             0.021029396538876154
         end)
     else
         -0.002198673045346081
     end) + (case when ((`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`)) or ((not (`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`))) and `userinfo_17` <= 1.5000000000000002)) then
         (case when ((`education_info1` is null or (`education_info1` <> `education_info1`)) or ((not (`education_info1` is null or (`education_info1` <> `education_info1`))) and `education_info1` <= 1e-13)) then
             0.0019081857734437617
         else
             -0.019066061212641497
         end)
     else
         -0.011198836124336394
     end) + (case when ((`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`)) or ((not (`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`))) and `thirdparty_info_period1_10` <= 4.5000000000000009)) then
         (case when ((`thirdparty_info_period1_5` is null or (`thirdparty_info_period1_5` <> `thirdparty_info_period1_5`)) or ((not (`thirdparty_info_period1_5` is null or (`thirdparty_info_period1_5` <> `thirdparty_info_period1_5`))) and `thirdparty_info_period1_5` <= 155.50000000000003)) then
             0.001555942608622676
         else
             -0.014643317832996239
         end)
     else
         -0.02010745790939009
     end) + (case when ((`education_info5` is null or (`education_info5` <> `education_info5`)) or ((not (`education_info5` is null or (`education_info5` <> `education_info5`))) and `education_info5` <= 1e-13)) then
         (case when ((`thirdparty_info_period3_2` is null or (`thirdparty_info_period3_2` <> `thirdparty_info_period3_2`)) or ((not (`thirdparty_info_period3_2` is null or (`thirdparty_info_period3_2` <> `thirdparty_info_period3_2`))) and `thirdparty_info_period3_2` <= 1e-13)) then
             0.0062763032216488534
         else
             -0.0020642852814903695
         end)
     else
         -0.025236047096318538
     end) + (case when ((`thirdparty_info_period3_6` is null or (`thirdparty_info_period3_6` <> `thirdparty_info_period3_6`)) or ((not (`thirdparty_info_period3_6` is null or (`thirdparty_info_period3_6` <> `thirdparty_info_period3_6`))) and `thirdparty_info_period3_6` <= 3.5000000000000004)) then
         (case when ((`thirdparty_info_period4_5` is null or (`thirdparty_info_period4_5` <> `thirdparty_info_period4_5`)) or ((not (`thirdparty_info_period4_5` is null or (`thirdparty_info_period4_5` <> `thirdparty_info_period4_5`))) and `thirdparty_info_period4_5` <= 12.500000000000002)) then
             0.010618932087362793
         else
             -0.0091116915597920702
         end)
     else
         0.0024758215391816386
     end) + (case when ((`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`)) or ((not (`userinfo_16` is null or (`userinfo_16` <> `userinfo_16`))) and `userinfo_16` <= 1.5000000000000002)) then
         (case when ((`thirdparty_info_period5_8` is null or (`thirdparty_info_period5_8` <> `thirdparty_info_period5_8`)) or ((not (`thirdparty_info_period5_8` is null or (`thirdparty_info_period5_8` <> `thirdparty_info_period5_8`))) and `thirdparty_info_period5_8` <= 488.50000000000006)) then
             0.0019853380267240892
         else
             0.04168778652343462
         end)
     else
         -0.0048909705232652598
     end) + (case when ((`thirdparty_info_period3_1` is null or (`thirdparty_info_period3_1` <> `thirdparty_info_period3_1`)) or ((not (`thirdparty_info_period3_1` is null or (`thirdparty_info_period3_1` <> `thirdparty_info_period3_1`))) and `thirdparty_info_period3_1` <= 1e-13)) then
         0.0057524936930564638
     else
         (case when ((`thirdparty_info_period3_15` is null or (`thirdparty_info_period3_15` <> `thirdparty_info_period3_15`)) or ((not (`thirdparty_info_period3_15` is null or (`thirdparty_info_period3_15` <> `thirdparty_info_period3_15`))) and `thirdparty_info_period3_15` <= 368.50000000000006)) then
             -0.0075727769460489022
         else
             0.0013593327254439367
         end)
     end) + (case when ((`socialnetwork_8` is null or (`socialnetwork_8` <> `socialnetwork_8`)) or ((not (`socialnetwork_8` is null or (`socialnetwork_8` <> `socialnetwork_8`))) and `socialnetwork_8` <= 143.50000000000003)) then
         (case when ((`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`)) or ((not (`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`))) and `thirdparty_info_period2_3` <= 145.50000000000003)) then
             -0.0041131420056215477
         else
             0.0036908627336395476
         end)
     else
         -0.015366300118251158
     end) + (case when ((`userinfo_18` is null or (`userinfo_18` <> `userinfo_18`)) or ((not (`userinfo_18` is null or (`userinfo_18` <> `userinfo_18`))) and `userinfo_18` <= 21.500000000000004)) then
         -0.016726705873237446
     else
         (case when ((`webloginfo_17` is null or (`webloginfo_17` <> `webloginfo_17`)) or ((not (`webloginfo_17` is null or (`webloginfo_17` <> `webloginfo_17`))) and `webloginfo_17` <= 6.5000000000000009)) then
             -0.0017926663264109365
         else
             0.0068930056172013202
         end)
     end) + (case when ((`thirdparty_info_period6_5` is null or (`thirdparty_info_period6_5` <> `thirdparty_info_period6_5`)) or ((not (`thirdparty_info_period6_5` is null or (`thirdparty_info_period6_5` <> `thirdparty_info_period6_5`))) and `thirdparty_info_period6_5` <= 96.500000000000014)) then
         (case when ((`thirdparty_info_period4_3` is null or (`thirdparty_info_period4_3` <> `thirdparty_info_period4_3`)) or ((not (`thirdparty_info_period4_3` is null or (`thirdparty_info_period4_3` <> `thirdparty_info_period4_3`))) and `thirdparty_info_period4_3` <= 316.50000000000006)) then
             -0.0007830509477711441
         else
             0.012400629224038392
         end)
     else
         -0.0073638733892642571
     end) + (case when ((`thirdparty_info_period1_9` is null or (`thirdparty_info_period1_9` <> `thirdparty_info_period1_9`)) or ((not (`thirdparty_info_period1_9` is null or (`thirdparty_info_period1_9` <> `thirdparty_info_period1_9`))) and `thirdparty_info_period1_9` <= 1e-13)) then
         0.0028448099950754476
     else
         (case when ((`thirdparty_info_period1_3` is null or (`thirdparty_info_period1_3` <> `thirdparty_info_period1_3`)) or ((not (`thirdparty_info_period1_3` is null or (`thirdparty_info_period1_3` <> `thirdparty_info_period1_3`))) and `thirdparty_info_period1_3` <= 325.50000000000006)) then
             -0.0071465340144421284
         else
             0.0083424875143002578
         end)
     end) + (case when ((`education_info1` is null or (`education_info1` <> `education_info1`)) or ((not (`education_info1` is null or (`education_info1` <> `education_info1`))) and `education_info1` <= 1e-13)) then
         (case when ((`thirdparty_info_period4_5` is null or (`thirdparty_info_period4_5` <> `thirdparty_info_period4_5`)) or ((not (`thirdparty_info_period4_5` is null or (`thirdparty_info_period4_5` <> `thirdparty_info_period4_5`))) and `thirdparty_info_period4_5` <= 57.500000000000007)) then
             0.0047929446121774766
         else
             -0.002547123489048007
         end)
     else
         -0.018940887179910576
     end) + (case when ((`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`)) or ((not (`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`))) and `thirdparty_info_period1_10` <= 2.5000000000000004)) then
         (case when ((`thirdparty_info_period1_5` is null or (`thirdparty_info_period1_5` <> `thirdparty_info_period1_5`)) or ((not (`thirdparty_info_period1_5` is null or (`thirdparty_info_period1_5` <> `thirdparty_info_period1_5`))) and `thirdparty_info_period1_5` <= 153.50000000000003)) then
             0.0022236564427530739
         else
             -0.016005879026559602
         end)
     else
         -0.01009894873679429
     end) + (case when ((`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`)) or ((not (`userinfo_17` is null or (`userinfo_17` <> `userinfo_17`))) and `userinfo_17` <= 1.5000000000000002)) then
         (case when ((`userinfo_5` is null or (`userinfo_5` <> `userinfo_5`)) or ((not (`userinfo_5` is null or (`userinfo_5` <> `userinfo_5`))) and `userinfo_5` <= 2.5000000000000004)) then
             0.0001487288530464026
         else
             0.015350466719914796
         end)
     else
         -0.010700316126759668
     end) + (case when ((`education_info5` is null or (`education_info5` <> `education_info5`)) or ((not (`education_info5` is null or (`education_info5` <> `education_info5`))) and `education_info5` <= 1e-13)) then
         (case when ((`thirdparty_info_period5_5` is null or (`thirdparty_info_period5_5` <> `thirdparty_info_period5_5`)) or ((not (`thirdparty_info_period5_5` is null or (`thirdparty_info_period5_5` <> `thirdparty_info_period5_5`))) and `thirdparty_info_period5_5` <= 44.500000000000007)) then
             0.0050268468747568266
         else
             -0.0024393164792706323
         end)
     else
         -0.0243661751788165
     end) + (case when ((`thirdparty_info_period4_15` is null or (`thirdparty_info_period4_15` <> `thirdparty_info_period4_15`)) or ((not (`thirdparty_info_period4_15` is null or (`thirdparty_info_period4_15` <> `thirdparty_info_period4_15`))) and `thirdparty_info_period4_15` <= 242.50000000000003)) then
         (case when ((`thirdparty_info_period4_14` is null or (`thirdparty_info_period4_14` <> `thirdparty_info_period4_14`)) or ((not (`thirdparty_info_period4_14` is null or (`thirdparty_info_period4_14` <> `thirdparty_info_period4_14`))) and `thirdparty_info_period4_14` <= 1878.5000000000002)) then
             0.0058975451536968137
         else
             -0.0089261868382999651
         end)
     else
         0.0027856342325260075
     end) + (case when ((`webloginfo_17` is null or (`webloginfo_17` <> `webloginfo_17`)) or ((not (`webloginfo_17` is null or (`webloginfo_17` <> `webloginfo_17`))) and `webloginfo_17` <= 6.5000000000000009)) then
         -0.0022315274715297945
     else
         (case when ((`thirdparty_info_period5_3` is null or (`thirdparty_info_period5_3` <> `thirdparty_info_period5_3`)) or ((not (`thirdparty_info_period5_3` is null or (`thirdparty_info_period5_3` <> `thirdparty_info_period5_3`))) and `thirdparty_info_period5_3` <= 303.50000000000006)) then
             0.001544852771907702
         else
             0.018810813082619095
         end)
     end) + (case when ((`socialnetwork_8` is null or (`socialnetwork_8` <> `socialnetwork_8`)) or ((not (`socialnetwork_8` is null or (`socialnetwork_8` <> `socialnetwork_8`))) and `socialnetwork_8` <= 143.50000000000003)) then
         (case when ((`thirdparty_info_period5_10` is null or (`thirdparty_info_period5_10` <> `thirdparty_info_period5_10`)) or ((not (`thirdparty_info_period5_10` is null or (`thirdparty_info_period5_10` <> `thirdparty_info_period5_10`))) and `thirdparty_info_period5_10` <= 1.5000000000000002)) then
             0.0019536355132049265
         else
             -0.0090851956929146865
         end)
     else
         -0.014649490555221387
     end) + (case when ((`userinfo_15` is null or (`userinfo_15` <> `userinfo_15`)) or ((not (`userinfo_15` is null or (`userinfo_15` <> `userinfo_15`))) and `userinfo_15` <= 2.5000000000000004)) then
         (case when ((`thirdparty_info_period6_8` is null or (`thirdparty_info_period6_8` <> `thirdparty_info_period6_8`)) or ((not (`thirdparty_info_period6_8` is null or (`thirdparty_info_period6_8` <> `thirdparty_info_period6_8`))) and `thirdparty_info_period6_8` <= 516.50000000000011)) then
             -0.0088305669278055682
         else
             0.10890557907362637
         end)
     else
         0.0013906151258223063
     end) + (case when ((`thirdparty_info_period3_5` is null or (`thirdparty_info_period3_5` <> `thirdparty_info_period3_5`)) or ((not (`thirdparty_info_period3_5` is null or (`thirdparty_info_period3_5` <> `thirdparty_info_period3_5`))) and `thirdparty_info_period3_5` <= 188.50000000000003)) then
         (case when ((`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`)) or ((not (`thirdparty_info_period2_3` is null or (`thirdparty_info_period2_3` <> `thirdparty_info_period2_3`))) and `thirdparty_info_period2_3` <= 486.50000000000006)) then
             -0.00077137587800663152
         else
             0.01383714791685936
         end)
     else
         -0.013221699871526339
     end) + (case when ((`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`)) or ((not (`thirdparty_info_period1_10` is null or (`thirdparty_info_period1_10` <> `thirdparty_info_period1_10`))) and `thirdparty_info_period1_10` <= 4.5000000000000009)) then
         (case when ((`thirdparty_info_period1_5` is null or (`thirdparty_info_period1_5` <> `thirdparty_info_period1_5`)) or ((not (`thirdparty_info_period1_5` is null or (`thirdparty_info_period1_5` <> `thirdparty_info_period1_5`))) and `thirdparty_info_period1_5` <= 155.50000000000003)) then
             0.0015103240742641638
         else
             -0.01343080716726062
         end)
     else
         -0.018722019153331115
     end) + (case when ((`thirdparty_info_period3_1` is null or (`thirdparty_info_period3_1` <> `thirdparty_info_period3_1`)) or ((not (`thirdparty_info_period3_1` is null or (`thirdparty_info_period3_1` <> `thirdparty_info_period3_1`))) and `thirdparty_info_period3_1` <= 3.5000000000000004)) then
         (case when ((`thirdparty_info_period1_1` is null or (`thirdparty_info_period1_1` <> `thirdparty_info_period1_1`)) or ((not (`thirdparty_info_period1_1` is null or (`thirdparty_info_period1_1` <> `thirdparty_info_period1_1`))) and `thirdparty_info_period1_1` <= 5.5000000000000009)) then
             0.00022520584136836438
         else
             0.015200506471519638
         end)
     else
         -0.0025855226416094143
     end) + (case when ((`thirdparty_info_period2_13` is null or (`thirdparty_info_period2_13` <> `thirdparty_info_period2_13`)) or ((not (`thirdparty_info_period2_13` is null or (`thirdparty_info_period2_13` <> `thirdparty_info_period2_13`))) and `thirdparty_info_period2_13` <= 32962.500000000007)) then
         (case when ((`thirdparty_info_period2_5` is null or (`thirdparty_info_period2_5` <> `thirdparty_info_period2_5`)) or ((not (`thirdparty_info_period2_5` is null or (`thirdparty_info_period2_5` <> `thirdparty_info_period2_5`))) and `thirdparty_info_period2_5` <= 129.50000000000003)) then
             0.00019881615420357741
         else
             -0.023263491012767881
         end)
     else
         0.0055995933317429941
     end) + (case when ((`thirdparty_info_period5_8` is null or (`thirdparty_info_period5_8` <> `thirdparty_info_period5_8`)) or ((not (`thirdparty_info_period5_8` is null or (`thirdparty_info_period5_8` <> `thirdparty_info_period5_8`))) and `thirdparty_info_period5_8` <= 488.50000000000006)) then
         (case when ((`thirdparty_info_period6_5` is null or (`thirdparty_info_period6_5` <> `thirdparty_info_period6_5`)) or ((not (`thirdparty_info_period6_5` is null or (`thirdparty_info_period6_5` <> `thirdparty_info_period6_5`))) and `thirdparty_info_period6_5` <= 96.500000000000014)) then
             0.0012728717899349973
         else
             -0.0087525443744678796
         end)
     else
         0.024254991303165708
     end))))) as score_p
from input_table