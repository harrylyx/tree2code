
        select idx,1 / (1 + exp(-((tree_0_score + tree_1_score + tree_2_score + tree_3_score + tree_4_score + tree_5_score + tree_6_score + tree_7_score + tree_8_score + tree_9_score + tree_10_score + tree_11_score + tree_12_score + tree_13_score + tree_14_score + tree_15_score + tree_16_score + tree_17_score + tree_18_score + tree_19_score + tree_20_score + tree_21_score + tree_22_score + tree_23_score + tree_24_score + tree_25_score + tree_26_score + tree_27_score + tree_28_score + tree_29_score + tree_30_score + tree_31_score + tree_32_score + tree_33_score + tree_34_score + tree_35_score + tree_36_score + tree_37_score + tree_38_score + tree_39_score + tree_40_score + tree_41_score + tree_42_score + tree_43_score + tree_44_score + tree_45_score + tree_46_score + tree_47_score + tree_48_score + tree_49_score + tree_50_score + tree_51_score + tree_52_score + tree_53_score + tree_54_score + tree_55_score + tree_56_score + tree_57_score + tree_58_score + tree_59_score + tree_60_score + tree_61_score + tree_62_score + tree_63_score + tree_64_score + tree_65_score + tree_66_score + tree_67_score + tree_68_score + tree_69_score + tree_70_score + tree_71_score + tree_72_score + tree_73_score + tree_74_score + tree_75_score + tree_76_score + tree_77_score + tree_78_score + tree_79_score + tree_80_score + tree_81_score + tree_82_score + tree_83_score + tree_84_score + tree_85_score + tree_86_score + tree_87_score + tree_88_score + tree_89_score + tree_90_score + tree_91_score + tree_92_score + tree_93_score + tree_94_score + tree_95_score + tree_96_score + tree_97_score + tree_98_score + tree_99_score + tree_100_score + tree_101_score + tree_102_score + tree_103_score + tree_104_score + tree_105_score + tree_106_score + tree_107_score + tree_108_score + tree_109_score + tree_110_score + tree_111_score + tree_112_score + tree_113_score + tree_114_score + tree_115_score + tree_116_score + tree_117_score + tree_118_score + tree_119_score + tree_120_score + tree_121_score + tree_122_score + tree_123_score + tree_124_score + tree_125_score + tree_126_score + tree_127_score + tree_128_score + tree_129_score + tree_130_score + tree_131_score + tree_132_score + tree_133_score + tree_134_score + tree_135_score + tree_136_score + tree_137_score + tree_138_score + tree_139_score + tree_140_score + tree_141_score + tree_142_score + tree_143_score + tree_144_score + tree_145_score + tree_146_score + tree_147_score + tree_148_score + tree_149_score + tree_150_score + tree_151_score + tree_152_score + tree_153_score + tree_154_score + tree_155_score + tree_156_score + tree_157_score + tree_158_score + tree_159_score + tree_160_score + tree_161_score + tree_162_score + tree_163_score + tree_164_score + tree_165_score + tree_166_score + tree_167_score + tree_168_score + tree_169_score + tree_170_score + tree_171_score + tree_172_score + tree_173_score + tree_174_score + tree_175_score + tree_176_score + tree_177_score + tree_178_score + tree_179_score + tree_180_score + tree_181_score + tree_182_score + tree_183_score + tree_184_score + tree_185_score + tree_186_score + tree_187_score + tree_188_score + tree_189_score + tree_190_score + tree_191_score + tree_192_score + tree_193_score + tree_194_score + tree_195_score + tree_196_score + tree_197_score + tree_198_score + tree_199_score)+(-0.0)))) as score
        from (
        select idx,
        --tree0
		case when (thirdparty_info_period1_6 is null and true==true or thirdparty_info_period1_6<=14.500000000000002) then
			case when (thirdparty_info_period5_1 is null and true==true or thirdparty_info_period5_1<=0.000000) then
				-2.462882248184236
			else
				-2.489020191444419
			end
		else
			-2.4295699792503966
		end
		as tree_0_score,
--tree1
		case when (thirdparty_info_period2_6 is null and true==true or thirdparty_info_period2_6<=23.500000000000004) then
			case when (userinfo_14 is null and true==true or userinfo_14<=3.5000000000000004) then
				-0.019324384994685515
			else
				0.007310915183384899
			end
		else
			0.039935963366007805
		end
		as tree_1_score,
--tree2
		case when (thirdparty_info_period2_6 is null and true==true or thirdparty_info_period2_6<=25.500000000000004) then
			case when (userinfo_14 is null and true==true or userinfo_14<=3.5000000000000004) then
				-0.018291967585472187
			else
				0.007151912716598369
			end
		else
			0.0384994050549064
		end
		as tree_2_score,
--tree3
		case when (thirdparty_info_period1_6 is null and true==true or thirdparty_info_period1_6<=14.500000000000002) then
			case when (thirdparty_info_period5_1 is null and true==true or thirdparty_info_period5_1<=0.000000) then
				0.008418998885988448
			else
				-0.016905859572355516
			end
		else
			0.03441595983289839
		end
		as tree_3_score,
--tree4
		case when (thirdparty_info_period2_6 is null and true==true or thirdparty_info_period2_6<=14.500000000000002) then
			-0.010683633147590037
		else
			case when (thirdparty_info_period4_2 is null and true==true or thirdparty_info_period4_2<=0.000000) then
				0.05470690536938229
			else
				0.013624238570792344
			end
		end
		as tree_4_score,
--tree5
		case when (thirdparty_info_period2_6 is null and true==true or thirdparty_info_period2_6<=14.500000000000002) then
			case when (thirdparty_info_period6_1 is null and true==true or thirdparty_info_period6_1<=0.000000) then
				0.0012477348096436517
			else
				-0.022718978698989683
			end
		else
			0.0236663428451935
		end
		as tree_5_score,
--tree6
		case when (thirdparty_info_period2_6 is null and true==true or thirdparty_info_period2_6<=14.500000000000002) then
			case when (thirdparty_info_period5_1 is null and true==true or thirdparty_info_period5_1<=0.000000) then
				0.005629561133830724
			else
				-0.018552836412776698
			end
		else
			0.022204118845676926
		end
		as tree_6_score,
--tree7
		case when (thirdparty_info_period1_6 is null and true==true or thirdparty_info_period1_6<=13.500000000000002) then
			case when (thirdparty_info_period6_1 is null and true==true or thirdparty_info_period6_1<=0.000000) then
				0.0037908520179377268
			else
				-0.019257761567318916
			end
		else
			0.026948557782490747
		end
		as tree_7_score,
--tree8
		case when (thirdparty_info_period1_6 is null and true==true or thirdparty_info_period1_6<=13.500000000000002) then
			case when (userinfo_14 is null and true==true or userinfo_14<=3.5000000000000004) then
				-0.01626341335098435
			else
				0.0065303346185426854
			end
		else
			0.025221039258161257
		end
		as tree_8_score,
--tree9
		case when (thirdparty_info_period5_2 is null and true==true or thirdparty_info_period5_2<=0.000000) then
			case when (thirdparty_info_period1_6 is null and true==true or thirdparty_info_period1_6<=15.500000000000002) then
				0.0072000281642714955
			else
				0.051511265642508165
			end
		else
			-0.010121182351034506
		end
		as tree_9_score,
--tree10
		case when (thirdparty_info_period2_6 is null and true==true or thirdparty_info_period2_6<=34.50000000000001) then
			case when (userinfo_14 is null and true==true or userinfo_14<=3.5000000000000004) then
				-0.015402415703284945
			else
				0.008750165561791166
			end
		else
			0.030937223459711307
		end
		as tree_10_score,
--tree11
		case when (thirdparty_info_period2_6 is null and true==true or thirdparty_info_period2_6<=11.500000000000002) then
			-0.00957996781860526
		else
			case when (thirdparty_info_period5_2 is null and true==true or thirdparty_info_period5_2<=0.000000) then
				0.03705803690943699
			else
				0.0036217913133995347
			end
		end
		as tree_11_score,
--tree12
		case when (thirdparty_info_period6_2 is null and true==true or thirdparty_info_period6_2<=0.000000) then
			case when (thirdparty_info_period2_6 is null and true==true or thirdparty_info_period2_6<=9.500000000000002) then
				-0.0004879012122769414
			else
				0.02726708218153076
			end
		else
			-0.013139533509006202
		end
		as tree_12_score,
--tree13
		case when (thirdparty_info_period2_6 is null and true==true or thirdparty_info_period2_6<=45.50000000000001) then
			case when (thirdparty_info_period6_1 is null and true==true or thirdparty_info_period6_1<=0.000000) then
				0.006277627283354176
			else
				-0.015815941335823716
			end
		else
			0.031572520509753746
		end
		as tree_13_score,
--tree14
		case when (thirdparty_info_period5_2 is null and true==true or thirdparty_info_period5_2<=0.000000) then
			0.014091203142360759
		else
			case when (thirdparty_info_period4_6 is null and true==true or thirdparty_info_period4_6<=10.500000000000002) then
				-0.0189317656590868
			else
				0.006073173124317457
			end
		end
		as tree_14_score,
--tree15
		case when (thirdparty_info_period1_15 is null and true==true or thirdparty_info_period1_15<=450.50000000000006) then
			-0.008869746565430329
		else
			case when (thirdparty_info_period4_2 is null and true==true or thirdparty_info_period4_2<=0.000000) then
				0.03359442629633164
			else
				0.004694753074927208
			end
		end
		as tree_15_score,
--tree16
		case when (thirdparty_info_period5_1 is null and true==true or thirdparty_info_period5_1<=0.000000) then
			0.014387711368448537
		else
			case when (thirdparty_info_period4_6 is null and true==true or thirdparty_info_period4_6<=16.500000000000004) then
				-0.01609619214910342
			else
				0.010432901487853299
			end
		end
		as tree_16_score,
--tree17
		case when (userinfo_14 is null and true==true or userinfo_14<=3.5000000000000004) then
			-0.00955581081601381
		else
			case when (userinfo_16 is null and true==true or userinfo_16<=1.5000000000000002) then
				0.024293950772789355
			else
				-0.002806400276973639
			end
		end
		as tree_17_score,
--tree18
		case when (thirdparty_info_period2_6 is null and true==true or thirdparty_info_period2_6<=14.500000000000002) then
			-0.007575908647040825
		else
			case when (webloginfo_7 is null and true==true or webloginfo_7<=20.500000000000004) then
				0.008256178527560155
			else
				0.05174947718374341
			end
		end
		as tree_18_score,
--tree19
		case when (thirdparty_info_period6_2 is null and true==true or thirdparty_info_period6_2<=0.000000) then
			case when (userinfo_15 is null and true==true or userinfo_15<=2.5000000000000004) then
				-0.016246768738504832
			else
				0.015154459715390471
			end
		else
			-0.011949488806590363
		end
		as tree_19_score,
--tree20
		case when (thirdparty_info_period1_15 is null and true==true or thirdparty_info_period1_15<=382.50000000000006) then
			-0.008788926519099067
		else
			case when (thirdparty_info_period5_2 is null and true==true or thirdparty_info_period5_2<=0.000000) then
				0.02722818618081929
			else
				0.0014836064675661585
			end
		end
		as tree_20_score,
--tree21
		case when (userinfo_14 is null and true==true or userinfo_14<=3.5000000000000004) then
			-0.009014001860138897
		else
			case when (userinfo_16 is null and true==true or userinfo_16<=1.5000000000000002) then
				0.022255045802607024
			else
				-0.002495763821752101
			end
		end
		as tree_21_score,
--tree22
		case when (thirdparty_info_period6_1 is null and true==true or thirdparty_info_period6_1<=0.000000) then
			case when (thirdparty_info_period2_15 is null and true==true or thirdparty_info_period2_15<=383.50000000000006) then
				-0.0025060494957937357
			else
				0.020443513665912016
			end
		else
			-0.01088763102175091
		end
		as tree_22_score,
--tree23
		case when (userinfo_14 is null and true==true or userinfo_14<=2.5000000000000004) then
			-0.020246066290781746
		else
			case when (userinfo_16 is null and true==true or userinfo_16<=1.5000000000000002) then
				0.01374878540670513
			else
				-0.008664674883385041
			end
		end
		as tree_23_score,
--tree24
		case when (thirdparty_info_period5_1 is null and true==true or thirdparty_info_period5_1<=0.000000) then
			0.012601744982983533
		else
			case when (thirdparty_info_period3_15 is null and true==true or thirdparty_info_period3_15<=1257.5000000000002) then
				-0.015591097020586808
			else
				0.0072036304684054645
			end
		end
		as tree_24_score,
--tree25
		case when (thirdparty_info_period6_9 is null and true==true or thirdparty_info_period6_9<=0.000000) then
			case when (thirdparty_info_period2_6 is null and true==true or thirdparty_info_period2_6<=7.500000000000001) then
				-0.005171301890751478
			else
				0.01589410156495166
			end
		else
			-0.017925537140112465
		end
		as tree_25_score,
--tree26
		case when (thirdparty_info_period5_2 is null and true==true or thirdparty_info_period5_2<=0.000000) then
			0.011236907487583507
		else
			case when (thirdparty_info_period4_6 is null and true==true or thirdparty_info_period4_6<=10.500000000000002) then
				-0.017015605591210063
			else
				0.005075350474818911
			end
		end
		as tree_26_score,
--tree27
		case when (userinfo_15 is null and true==true or userinfo_15<=2.5000000000000004) then
			-0.019425325129218733
		else
			case when (thirdparty_info_period6_2 is null and true==true or thirdparty_info_period6_2<=0.000000) then
				0.012796262236659698
			else
				-0.0072458353188200935
			end
		end
		as tree_27_score,
--tree28
		case when (thirdparty_info_period5_10 is null and true==true or thirdparty_info_period5_10<=0.000000) then
			case when (thirdparty_info_period2_6 is null and true==true or thirdparty_info_period2_6<=6.500000000000001) then
				-0.004855727189647016
			else
				0.016334556726702375
			end
		else
			-0.01401497604432722
		end
		as tree_28_score,
--tree29
		case when (userinfo_14 is null and true==true or userinfo_14<=3.5000000000000004) then
			case when (thirdparty_info_period2_6 is null and true==true or thirdparty_info_period2_6<=32.50000000000001) then
				-0.012721151159235364
			else
				0.015891100555479133
			end
		else
			0.00995573446187177
		end
		as tree_29_score,
--tree30
		case when (userinfo_16 is null and true==true or userinfo_16<=1.5000000000000002) then
			case when (thirdparty_info_period4_9 is null and true==true or thirdparty_info_period4_9<=0.000000) then
				0.01501460032582756
			else
				-0.007172452406308182
			end
		else
			-0.0118317768371918
		end
		as tree_30_score,
--tree31
		case when (thirdparty_info_period5_1 is null and true==true or thirdparty_info_period5_1<=0.000000) then
			0.011137470051898614
		else
			case when (thirdparty_info_period4_6 is null and true==true or thirdparty_info_period4_6<=15.500000000000002) then
				-0.014024697090446632
			else
				0.007643592946987485
			end
		end
		as tree_31_score,
--tree32
		case when (userinfo_16 is null and true==true or userinfo_16<=1.5000000000000002) then
			case when (education_info1 is null and true==true or education_info1<=0.000000) then
				0.009659338579497379
			else
				-0.032070886085127315
			end
		else
			-0.011360006399658607
		end
		as tree_32_score,
--tree33
		case when (userinfo_14 is null and true==true or userinfo_14<=2.5000000000000004) then
			-0.018358923163148067
		else
			case when (thirdparty_info_period6_9 is null and true==true or thirdparty_info_period6_9<=0.000000) then
				0.008847511461839526
			else
				-0.013888622379827334
			end
		end
		as tree_33_score,
--tree34
		case when (userinfo_16 is null and true==true or userinfo_16<=1.5000000000000002) then
			case when (thirdparty_info_period1_10 is null and true==true or thirdparty_info_period1_10<=1.5000000000000002) then
				0.012398402994436855
			else
				-0.010754492053989439
			end
		else
			-0.010885713468001587
		end
		as tree_34_score,
--tree35
		case when (thirdparty_info_period1_15 is null and true==true or thirdparty_info_period1_15<=382.50000000000006) then
			-0.007428860774840989
		else
			case when (webloginfo_15 is null and true==true or webloginfo_15<=5.500000000000001) then
				0.0064310053351155265
			else
				0.050067488340102564
			end
		end
		as tree_35_score,
--tree36
		case when (thirdparty_info_period6_1 is null and true==true or thirdparty_info_period6_1<=0.000000) then
			case when (thirdparty_info_period2_15 is null and true==true or thirdparty_info_period2_15<=215.50000000000003) then
				-0.004229939815536563
			else
				0.014721783421377064
			end
		else
			-0.009356793807961726
		end
		as tree_36_score,
--tree37
		case when (thirdparty_info_period5_9 is null and true==true or thirdparty_info_period5_9<=0.000000) then
			case when (userinfo_16 is null and true==true or userinfo_16<=1.5000000000000002) then
				0.012486621214733028
			else
				-0.006770340052071367
			end
		else
			-0.012771682664543323
		end
		as tree_37_score,
--tree38
		case when (thirdparty_info_period5_2 is null and true==true or thirdparty_info_period5_2<=0.000000) then
			0.009528166810729731
		else
			case when (thirdparty_info_period4_6 is null and true==true or thirdparty_info_period4_6<=7.500000000000001) then
				-0.01667640080753506
			else
				0.00270278317044778
			end
		end
		as tree_38_score,
--tree39
		case when (userinfo_15 is null and true==true or userinfo_15<=3.5000000000000004) then
			case when (thirdparty_info_period2_8 is null and true==true or thirdparty_info_period2_8<=257.50000000000006) then
				-0.011156596811970149
			else
				0.020533302396988584
			end
		else
			0.008837276480222919
		end
		as tree_39_score,
--tree40
		case when (thirdparty_info_period4_1 is null and true==true or thirdparty_info_period4_1<=0.000000) then
			0.011915491630970228
		else
			case when (thirdparty_info_period3_6 is null and true==true or thirdparty_info_period3_6<=3.5000000000000004) then
				-0.01907080109747252
			else
				0.0008246258016754364
			end
		end
		as tree_40_score,
--tree41
		case when (userinfo_14 is null and true==true or userinfo_14<=2.5000000000000004) then
			-0.017181000498122143
		else
			case when (thirdparty_info_period6_9 is null and true==true or thirdparty_info_period6_9<=0.000000) then
				0.00795158735635529
			else
				-0.012914947040829718
			end
		end
		as tree_41_score,
--tree42
		case when (userinfo_16 is null and true==true or userinfo_16<=1.5000000000000002) then
			case when (education_info1 is null and true==true or education_info1<=0.000000) then
				0.008385460925550984
			else
				-0.03025635888664315
			end
		else
			-0.010028170161081228
		end
		as tree_42_score,
--tree43
		case when (webloginfo_15 is null and true==true or webloginfo_15<=5.500000000000001) then
			case when (thirdparty_info_period6_2 is null and true==true or thirdparty_info_period6_2<=0.000000) then
				0.004495690081213519
			else
				-0.010987936483549364
			end
		else
			0.03155088060667317
		end
		as tree_43_score,
--tree44
		case when (thirdparty_info_period1_10 is null and true==true or thirdparty_info_period1_10<=2.5000000000000004) then
			case when (thirdparty_info_period1_15 is null and true==true or thirdparty_info_period1_15<=382.50000000000006) then
				-0.004390682141468343
			else
				0.012908884367225582
			end
		else
			-0.02023010996598836
		end
		as tree_44_score,
--tree45
		case when (thirdparty_info_period2_6 is null and true==true or thirdparty_info_period2_6<=45.50000000000001) then
			case when (userinfo_15 is null and true==true or userinfo_15<=3.5000000000000004) then
				-0.010229494598236077
			else
				0.005554192974373623
			end
		else
			0.019161119347118984
		end
		as tree_45_score,
--tree46
		case when (userinfo_17 is null and true==true or userinfo_17<=1.5000000000000002) then
			case when (userinfo_16 is null and true==true or userinfo_16<=1.5000000000000002) then
				0.009130166212177729
			else
				-0.007824954316839055
			end
		else
			-0.020805957187076528
		end
		as tree_46_score,
--tree47
		case when (thirdparty_info_period1_10 is null and true==true or thirdparty_info_period1_10<=2.5000000000000004) then
			case when (thirdparty_info_period4_1 is null and true==true or thirdparty_info_period4_1<=0.000000) then
				0.01506503976366802
			else
				-0.0027406792147852375
			end
		else
			-0.01953900544034152
		end
		as tree_47_score,
--tree48
		case when (thirdparty_info_period2_8 is null and true==true or thirdparty_info_period2_8<=192.50000000000003) then
			case when (userinfo_14 is null and true==true or userinfo_14<=2.5000000000000004) then
				-0.02146977556812779
			else
				-0.0002578968168940316
			end
		else
			0.013683091667625283
		end
		as tree_48_score,
--tree49
		case when (thirdparty_info_period4_2 is null and true==true or thirdparty_info_period4_2<=0.000000) then
			0.009841630539026626
		else
			case when (thirdparty_info_period4_15 is null and true==true or thirdparty_info_period4_15<=196.50000000000003) then
				-0.017260313368175594
			else
				0.0006620870978199111
			end
		end
		as tree_49_score,
--tree50
		case when (webloginfo_15 is null and true==true or webloginfo_15<=1.5000000000000002) then
			case when (thirdparty_info_period3_10 is null and true==true or thirdparty_info_period3_10<=2.5000000000000004) then
				-0.0015462678286328776
			else
				-0.026115874297408987
			end
		else
			0.013545175978227695
		end
		as tree_50_score,
--tree51
		case when (userinfo_17 is null and true==true or userinfo_17<=1.5000000000000002) then
			case when (userinfo_16 is null and true==true or userinfo_16<=1.5000000000000002) then
				0.008563726121788134
			else
				-0.00744222190232243
			end
		else
			-0.019897611364543287
		end
		as tree_51_score,
--tree52
		case when (thirdparty_info_period6_14 is null and true==true or thirdparty_info_period6_14<=2351.5000000000005) then
			0.00873333445326068
		else
			case when (thirdparty_info_period6_6 is null and true==true or thirdparty_info_period6_6<=21.500000000000004) then
				-0.011107391452027852
			else
				0.01040965779959591
			end
		end
		as tree_52_score,
--tree53
		case when (thirdparty_info_period6_9 is null and true==true or thirdparty_info_period6_9<=0.000000) then
			case when (thirdparty_info_period2_6 is null and true==true or thirdparty_info_period2_6<=2.5000000000000004) then
				-0.008837338668881421
			else
				0.008472773491415444
			end
		else
			-0.014164217351115296
		end
		as tree_53_score,
--tree54
		case when (thirdparty_info_period1_10 is null and true==true or thirdparty_info_period1_10<=2.5000000000000004) then
			case when (thirdparty_info_period4_1 is null and true==true or thirdparty_info_period4_1<=0.000000) then
				0.013611600342336456
			else
				-0.002656378806841144
			end
		else
			-0.01874423881387864
		end
		as tree_54_score,
--tree55
		case when (webloginfo_15 is null and true==true or webloginfo_15<=1.5000000000000002) then
			case when (thirdparty_info_period6_5 is null and true==true or thirdparty_info_period6_5<=65.50000000000001) then
				0.0010920108188996497
			else
				-0.013808417836625947
			end
		else
			0.01261025205947377
		end
		as tree_55_score,
--tree56
		case when (thirdparty_info_period5_9 is null and true==true or thirdparty_info_period5_9<=0.000000) then
			case when (thirdparty_info_period4_6 is null and true==true or thirdparty_info_period4_6<=21.500000000000004) then
				0.00027218776528114836
			else
				0.0186350641201713
			end
		else
			-0.010933309636034554
		end
		as tree_56_score,
--tree57
		case when (userinfo_17 is null and true==true or userinfo_17<=1.5000000000000002) then
			case when (userinfo_16 is null and true==true or userinfo_16<=1.5000000000000002) then
				0.00795577294151664
			else
				-0.00700396516864996
			end
		else
			-0.019287194114605055
		end
		as tree_57_score,
--tree58
		case when (userinfo_14 is null and true==true or userinfo_14<=2.5000000000000004) then
			-0.015212955996736489
		else
			case when (thirdparty_info_period3_10 is null and true==true or thirdparty_info_period3_10<=0.000000) then
				0.008353662485055167
			else
				-0.006457375988983523
			end
		end
		as tree_58_score,
--tree59
		case when (thirdparty_info_period2_8 is null and true==true or thirdparty_info_period2_8<=192.50000000000003) then
			case when (userinfo_14 is null and true==true or userinfo_14<=2.5000000000000004) then
				-0.01997565215113392
			else
				-0.00033249013025029683
			end
		else
			0.012363079588216853
		end
		as tree_59_score,
--tree60
		case when (thirdparty_info_period5_2 is null and true==true or thirdparty_info_period5_2<=0.000000) then
			0.007677406581825141
		else
			case when (thirdparty_info_period4_6 is null and true==true or thirdparty_info_period4_6<=3.5000000000000004) then
				-0.018326181465486063
			else
				-0.00018494926654721812
			end
		end
		as tree_60_score,
--tree61
		case when (thirdparty_info_period4_2 is null and true==true or thirdparty_info_period4_2<=0.000000) then
			0.008815939154119616
		else
			case when (thirdparty_info_period4_6 is null and true==true or thirdparty_info_period4_6<=7.500000000000001) then
				-0.012976733093149596
			else
				0.0025306481928173657
			end
		end
		as tree_61_score,
--tree62
		case when (userinfo_17 is null and true==true or userinfo_17<=1.5000000000000002) then
			case when (userinfo_16 is null and true==true or userinfo_16<=1.5000000000000002) then
				0.007675506452600052
			else
				-0.00689977205109017
			end
		else
			-0.018767171645464997
		end
		as tree_62_score,
--tree63
		case when (education_info1 is null and true==true or education_info1<=0.000000) then
			case when (userinfo_16 is null and true==true or userinfo_16<=1.5000000000000002) then
				0.006765818077038534
			else
				-0.007642684752085508
			end
		else
			-0.029558967931558155
		end
		as tree_63_score,
--tree64
		case when (thirdparty_info_period2_10 is null and true==true or thirdparty_info_period2_10<=1.5000000000000002) then
			case when (thirdparty_info_period2_8 is null and true==true or thirdparty_info_period2_8<=192.50000000000003) then
				-0.00015717972869373013
			else
				0.01668441710550694
			end
		else
			-0.012330942682136435
		end
		as tree_64_score,
--tree65
		case when (thirdparty_info_period1_10 is null and true==true or thirdparty_info_period1_10<=2.5000000000000004) then
			case when (webloginfo_15 is null and true==true or webloginfo_15<=1.5000000000000002) then
				-0.0014009737080725995
			else
				0.015123479834218086
			end
		else
			-0.01746382090545535
		end
		as tree_65_score,
--tree66
		case when (webloginfo_15 is null and true==true or webloginfo_15<=5.500000000000001) then
			case when (thirdparty_info_period3_9 is null and true==true or thirdparty_info_period3_9<=0.000000) then
				0.0030043946131804336
			else
				-0.010216863131916068
			end
		else
			0.025400842748621335
		end
		as tree_66_score,
--tree67
		case when (thirdparty_info_period2_6 is null and true==true or thirdparty_info_period2_6<=2.5000000000000004) then
			-0.010886945274254139
		else
			case when (thirdparty_info_period6_14 is null and true==true or thirdparty_info_period6_14<=3438.5000000000005) then
				0.012741032478889025
			else
				-0.002441007265094642
			end
		end
		as tree_67_score,
--tree68
		case when (education_info1 is null and true==true or education_info1<=0.000000) then
			case when (userinfo_16 is null and true==true or userinfo_16<=1.5000000000000002) then
				0.006446243468373776
			else
				-0.007095572463712663
			end
		else
			-0.02924916672721388
		end
		as tree_68_score,
--tree69
		case when (thirdparty_info_period2_3 is null and true==true or thirdparty_info_period2_3<=426.50000000000006) then
			-0.0027606772976732762
		else
			case when (thirdparty_info_period3_5 is null and true==true or thirdparty_info_period3_5<=161.50000000000003) then
				0.02569228176615103
			else
				-0.007251550862327343
			end
		end
		as tree_69_score,
--tree70
		case when (thirdparty_info_period4_1 is null and true==true or thirdparty_info_period4_1<=0.000000) then
			0.008939562476459103
		else
			case when (thirdparty_info_period3_6 is null and true==true or thirdparty_info_period3_6<=3.5000000000000004) then
				-0.016319869063886473
			else
				0.0006292380404688924
			end
		end
		as tree_70_score,
--tree71
		case when (thirdparty_info_period1_10 is null and true==true or thirdparty_info_period1_10<=2.5000000000000004) then
			case when (thirdparty_info_period1_15 is null and true==true or thirdparty_info_period1_15<=115.50000000000001) then
				-0.005830135823211603
			else
				0.007601277061614266
			end
		else
			-0.01701084614994559
		end
		as tree_71_score,
--tree72
		case when (userinfo_17 is null and true==true or userinfo_17<=1.5000000000000002) then
			case when (userinfo_15 is null and true==true or userinfo_15<=3.5000000000000004) then
				-0.004151605635730759
			else
				0.009036980290806696
			end
		else
			-0.01771493576396369
		end
		as tree_72_score,
--tree73
		case when (thirdparty_info_period6_14 is null and true==true or thirdparty_info_period6_14<=2351.5000000000005) then
			0.00714157759108364
		else
			case when (thirdparty_info_period6_15 is null and true==true or thirdparty_info_period6_15<=414.50000000000006) then
				-0.014324439914961988
			else
				0.0030502561739427607
			end
		end
		as tree_73_score,
--tree74
		case when (userinfo_14 is null and true==true or userinfo_14<=2.5000000000000004) then
			-0.013612685527976148
		else
			case when (thirdparty_info_period2_10 is null and true==true or thirdparty_info_period2_10<=1.5000000000000002) then
				0.005844657206625596
			else
				-0.009302253169854906
			end
		end
		as tree_74_score,
--tree75
		case when (thirdparty_info_period5_1 is null and true==true or thirdparty_info_period5_1<=0.000000) then
			0.007273243187996688
		else
			case when (thirdparty_info_period3_6 is null and true==true or thirdparty_info_period3_6<=3.5000000000000004) then
				-0.016891604508238622
			else
				2.3332093540659132e-05
			end
		end
		as tree_75_score,
--tree76
		case when (userinfo_17 is null and true==true or userinfo_17<=1.5000000000000002) then
			case when (userinfo_15 is null and true==true or userinfo_15<=3.5000000000000004) then
				-0.0037592885301220035
			else
				0.008111243126746331
			end
		else
			-0.017055467911961667
		end
		as tree_76_score,
--tree77
		case when (webloginfo_15 is null and true==true or webloginfo_15<=5.500000000000001) then
			case when (thirdparty_info_period1_10 is null and true==true or thirdparty_info_period1_10<=1.5000000000000002) then
				0.001548865712752118
			else
				-0.012825332280571464
			end
		else
			0.022626507744164224
		end
		as tree_77_score,
--tree78
		case when (thirdparty_info_period3_8 is null and true==true or thirdparty_info_period3_8<=484.50000000000006) then
			case when (thirdparty_info_period5_1 is null and true==true or thirdparty_info_period5_1<=0.000000) then
				0.006540053786256077
			else
				-0.005900929335920428
			end
		else
			0.04209925779325388
		end
		as tree_78_score,
--tree79
		case when (education_info1 is null and true==true or education_info1<=0.000000) then
			case when (thirdparty_info_period4_2 is null and true==true or thirdparty_info_period4_2<=0.000000) then
				0.00917916843460422
			else
				-0.003221399387606333
			end
		else
			-0.027588518259356876
		end
		as tree_79_score,
--tree80
		case when (thirdparty_info_period2_3 is null and true==true or thirdparty_info_period2_3<=426.50000000000006) then
			-0.002641975124236983
		else
			case when (thirdparty_info_period3_5 is null and true==true or thirdparty_info_period3_5<=161.50000000000003) then
				0.02361130668471446
			else
				-0.007105332328962855
			end
		end
		as tree_80_score,
--tree81
		case when (education_info1 is null and true==true or education_info1<=0.000000) then
			case when (userinfo_17 is null and true==true or userinfo_17<=1.5000000000000002) then
				0.003219235453477012
			else
				-0.015596246667372724
			end
		else
			-0.026823179942248556
		end
		as tree_81_score,
--tree82
		case when (webloginfo_15 is null and true==true or webloginfo_15<=0.000000) then
			case when (thirdparty_info_period3_10 is null and true==true or thirdparty_info_period3_10<=2.5000000000000004) then
				-0.001851621678424626
			else
				-0.024665293076471546
			end
		else
			0.008100993881698765
		end
		as tree_82_score,
--tree83
		case when (userinfo_16 is null and true==true or userinfo_16<=1.5000000000000002) then
			case when (thirdparty_info_period1_10 is null and true==true or thirdparty_info_period1_10<=1.5000000000000002) then
				0.007787688017902423
			else
				-0.008125365991979957
			end
		else
			-0.0075811856875240115
		end
		as tree_83_score,
--tree84
		case when (thirdparty_info_period2_3 is null and true==true or thirdparty_info_period2_3<=184.50000000000003) then
			-0.005984216659107547
		else
			case when (thirdparty_info_period5_5 is null and true==true or thirdparty_info_period5_5<=82.50000000000001) then
				0.015572136552182808
			else
				-0.0042044865213428425
			end
		end
		as tree_84_score,
--tree85
		case when (thirdparty_info_period2_8 is null and true==true or thirdparty_info_period2_8<=257.50000000000006) then
			case when (thirdparty_info_period5_5 is null and true==true or thirdparty_info_period5_5<=46.50000000000001) then
				0.005221825269365752
			else
				-0.00789225590357683
			end
		else
			0.013679232594430152
		end
		as tree_85_score,
--tree86
		case when (thirdparty_info_period4_2 is null and true==true or thirdparty_info_period4_2<=0.000000) then
			0.007193544271403504
		else
			case when (thirdparty_info_period4_6 is null and true==true or thirdparty_info_period4_6<=39.50000000000001) then
				-0.0072061108213528485
			else
				0.010813038962429147
			end
		end
		as tree_86_score,
--tree87
		case when (thirdparty_info_period6_14 is null and true==true or thirdparty_info_period6_14<=2351.5000000000005) then
			0.0062371306005366625
		else
			case when (thirdparty_info_period6_15 is null and true==true or thirdparty_info_period6_15<=192.50000000000003) then
				-0.015539636508257348
			else
				0.0011534479172392853
			end
		end
		as tree_87_score,
--tree88
		case when (thirdparty_info_period1_10 is null and true==true or thirdparty_info_period1_10<=2.5000000000000004) then
			case when (education_info5 is null and true==true or education_info5<=0.000000) then
				0.0029508992352049097
			else
				-0.03299199824284623
			end
		else
			-0.015253439047782057
		end
		as tree_88_score,
--tree89
		case when (education_info1 is null and true==true or education_info1<=0.000000) then
			case when (webloginfo_15 is null and true==true or webloginfo_15<=5.500000000000001) then
				-0.0003691953931875669
			else
				0.022601694690081976
			end
		else
			-0.026044298605751526
		end
		as tree_89_score,
--tree90
		case when (thirdparty_info_period6_9 is null and true==true or thirdparty_info_period6_9<=0.000000) then
			case when (education_info5 is null and true==true or education_info5<=0.000000) then
				0.003598712075826341
			else
				-0.03126715973348245
			end
		else
			-0.010945952029616736
		end
		as tree_90_score,
--tree91
		case when (userinfo_17 is null and true==true or userinfo_17<=1.5000000000000002) then
			case when (userinfo_5 is null and true==true or userinfo_5<=2.5000000000000004) then
				0.00032121848099252675
			else
				0.026230004075447417
			end
		else
			-0.015590680278621769
		end
		as tree_91_score,
--tree92
		case when (thirdparty_info_period2_6 is null and true==true or thirdparty_info_period2_6<=2.5000000000000004) then
			-0.009137829183696017
		else
			case when (thirdparty_info_period4_9 is null and true==true or thirdparty_info_period4_9<=1.5000000000000002) then
				0.00686941015088155
			else
				-0.008007675313277207
			end
		end
		as tree_92_score,
--tree93
		case when (userinfo_16 is null and true==true or userinfo_16<=1.5000000000000002) then
			case when (thirdparty_info_period2_3 is null and true==true or thirdparty_info_period2_3<=426.50000000000006) then
				0.0013209306266953923
			else
				0.018822657579687093
			end
		else
			-0.007192885675275026
		end
		as tree_93_score,
--tree94
		case when (thirdparty_info_period3_8 is null and true==true or thirdparty_info_period3_8<=484.50000000000006) then
			case when (thirdparty_info_period6_5 is null and true==true or thirdparty_info_period6_5<=96.50000000000001) then
				0.0017967832344479352
			else
				-0.012758908728914742
			end
		else
			0.03536834946627913
		end
		as tree_94_score,
--tree95
		case when (thirdparty_info_period2_3 is null and true==true or thirdparty_info_period2_3<=184.50000000000003) then
			-0.005581206070132514
		else
			case when (thirdparty_info_period5_5 is null and true==true or thirdparty_info_period5_5<=87.50000000000001) then
				0.01349071763532073
			else
				-0.004564855547675858
			end
		end
		as tree_95_score,
--tree96
		case when (education_info1 is null and true==true or education_info1<=0.000000) then
			case when (userinfo_16 is null and true==true or userinfo_16<=1.5000000000000002) then
				0.0052145623409894796
			else
				-0.00623612098621236
			end
		else
			-0.025364697841014652
		end
		as tree_96_score,
--tree97
		case when (thirdparty_info_period1_10 is null and true==true or thirdparty_info_period1_10<=2.5000000000000004) then
			case when (thirdparty_info_period4_1 is null and true==true or thirdparty_info_period4_1<=0.000000) then
				0.009776463929361384
			else
				-0.0020767734687120896
			end
		else
			-0.01430610630061133
		end
		as tree_97_score,
--tree98
		case when (userinfo_17 is null and true==true or userinfo_17<=1.5000000000000002) then
			case when (userinfo_5 is null and true==true or userinfo_5<=2.5000000000000004) then
				0.0003607377291303415
			else
				0.023781197033135647
			end
		else
			-0.015123316594501949
		end
		as tree_98_score,
--tree99
		case when (thirdparty_info_period4_2 is null and true==true or thirdparty_info_period4_2<=0.000000) then
			0.006581725638343858
		else
			case when (thirdparty_info_period4_15 is null and true==true or thirdparty_info_period4_15<=196.50000000000003) then
				-0.013358450548808791
			else
				0.0006221562676999541
			end
		end
		as tree_99_score,
--tree100
		case when (userinfo_15 is null and true==true or userinfo_15<=2.5000000000000004) then
			-0.01192110320462307
		else
			case when (thirdparty_info_period2_10 is null and true==true or thirdparty_info_period2_10<=1.5000000000000002) then
				0.005086361284500518
			else
				-0.008226888880949289
			end
		end
		as tree_100_score,
--tree101
		case when (webloginfo_15 is null and true==true or webloginfo_15<=1.5000000000000002) then
			case when (thirdparty_info_period6_5 is null and true==true or thirdparty_info_period6_5<=65.50000000000001) then
				0.0013701793370216998
			else
				-0.011242556446327946
			end
		else
			0.009040820171582134
		end
		as tree_101_score,
--tree102
		case when (thirdparty_info_period2_3 is null and true==true or thirdparty_info_period2_3<=304.50000000000006) then
			-0.0033818091052459525
		else
			case when (thirdparty_info_period3_5 is null and true==true or thirdparty_info_period3_5<=121.50000000000001) then
				0.01786511959504158
			else
				-0.0037134755196687624
			end
		end
		as tree_102_score,
--tree103
		case when (thirdparty_info_period3_8 is null and true==true or thirdparty_info_period3_8<=484.50000000000006) then
			case when (thirdparty_info_period6_1 is null and true==true or thirdparty_info_period6_1<=2.5000000000000004) then
				0.003274176742517237
			else
				-0.007698237268224526
			end
		else
			0.03318416368463473
		end
		as tree_103_score,
--tree104
		case when (userinfo_17 is null and true==true or userinfo_17<=1.5000000000000002) then
			case when (userinfo_14 is null and true==true or userinfo_14<=3.5000000000000004) then
				-0.0032886604375268144
			else
				0.006784593058717064
			end
		else
			-0.014759200942206955
		end
		as tree_104_score,
--tree105
		case when (thirdparty_info_period1_10 is null and true==true or thirdparty_info_period1_10<=2.5000000000000004) then
			case when (education_info5 is null and true==true or education_info5<=0.000000) then
				0.002601092265492492
			else
				-0.030545665225466513
			end
		else
			-0.013839412520292471
		end
		as tree_105_score,
--tree106
		case when (education_info1 is null and true==true or education_info1<=0.000000) then
			case when (education_info5 is null and true==true or education_info5<=0.000000) then
				0.0017358261688452871
			else
				-0.0322387858938053
			end
		else
			-0.024293950514334122
		end
		as tree_106_score,
--tree107
		case when (thirdparty_info_period3_10 is null and true==true or thirdparty_info_period3_10<=2.5000000000000004) then
			case when (thirdparty_info_period2_6 is null and true==true or thirdparty_info_period2_6<=3.5000000000000004) then
				-0.006324119696279
			else
				0.004975030657432193
			end
		else
			-0.01578983089815457
		end
		as tree_107_score,
--tree108
		case when (thirdparty_info_period4_2 is null and true==true or thirdparty_info_period4_2<=0.000000) then
			0.006291744432552072
		else
			case when (thirdparty_info_period4_15 is null and true==true or thirdparty_info_period4_15<=196.50000000000003) then
				-0.012525685796968375
			else
				0.0005104608880362628
			end
		end
		as tree_108_score,
--tree109
		case when (userinfo_16 is null and true==true or userinfo_16<=1.5000000000000002) then
			case when (education_info1 is null and true==true or education_info1<=0.000000) then
				0.004748545897666025
			else
				-0.022960039421755216
			end
		else
			-0.006338093051805949
		end
		as tree_109_score,
--tree110
		case when (thirdparty_info_period2_3 is null and true==true or thirdparty_info_period2_3<=426.50000000000006) then
			case when (thirdparty_info_period2_5 is null and true==true or thirdparty_info_period2_5<=125.50000000000001) then
				-9.432610441198807e-05
			else
				-0.019281304070506395
			end
		else
			0.010376441105425425
		end
		as tree_110_score,
--tree111
		case when (thirdparty_info_period3_9 is null and true==true or thirdparty_info_period3_9<=0.000000) then
			case when (thirdparty_info_period1_15 is null and true==true or thirdparty_info_period1_15<=34.50000000000001) then
				-0.006451711527002828
			else
				0.007349003591493483
			end
		else
			-0.0065910043948412475
		end
		as tree_111_score,
--tree112
		case when (webloginfo_15 is null and true==true or webloginfo_15<=5.500000000000001) then
			case when (socialnetwork_13 is null and true==true or socialnetwork_13<=0.000000) then
				0.0015134587728129103
			else
				-0.012245059715310935
			end
		else
			0.018206204331140438
		end
		as tree_112_score,
--tree113
		case when (userinfo_17 is null and true==true or userinfo_17<=1.5000000000000002) then
			case when (thirdparty_info_period6_5 is null and true==true or thirdparty_info_period6_5<=75.50000000000001) then
				0.004594251138549717
			else
				-0.006144407200133942
			end
		else
			-0.013958599489509402
		end
		as tree_113_score,
--tree114
		case when (thirdparty_info_period2_3 is null and true==true or thirdparty_info_period2_3<=184.50000000000003) then
			case when (thirdparty_info_period3_3 is null and true==true or thirdparty_info_period3_3<=264.50000000000006) then
				-0.006808154846782402
			else
				0.043445245900617324
			end
		else
			0.004572395032734741
		end
		as tree_114_score,
--tree115
		case when (thirdparty_info_period1_10 is null and true==true or thirdparty_info_period1_10<=4.500000000000001) then
			case when (thirdparty_info_period4_6 is null and true==true or thirdparty_info_period4_6<=40.50000000000001) then
				-0.0010523135578731594
			else
				0.012784086538521625
			end
		else
			-0.02385855092570821
		end
		as tree_115_score,
--tree116
		case when (webloginfo_15 is null and true==true or webloginfo_15<=0.000000) then
			case when (socialnetwork_13 is null and true==true or socialnetwork_13<=0.000000) then
				-0.0005071357341381999
			else
				-0.016999382076130717
			end
		else
			0.006806568742028795
		end
		as tree_116_score,
--tree117
		case when (thirdparty_info_period5_5 is null and true==true or thirdparty_info_period5_5<=44.50000000000001) then
			0.005957703448522217
		else
			case when (thirdparty_info_period4_3 is null and true==true or thirdparty_info_period4_3<=242.50000000000003) then
				-0.011587625650905306
			else
				0.0038885358563291728
			end
		end
		as tree_117_score,
--tree118
		case when (thirdparty_info_period3_1 is null and true==true or thirdparty_info_period3_1<=0.000000) then
			case when (thirdparty_info_period1_1 is null and true==true or thirdparty_info_period1_1<=4.500000000000001) then
				0.0007145611850437681
			else
				0.026886139004318868
			end
		else
			-0.0027676520587518578
		end
		as tree_118_score,
--tree119
		case when (thirdparty_info_period1_10 is null and true==true or thirdparty_info_period1_10<=4.500000000000001) then
			case when (education_info5 is null and true==true or education_info5<=0.000000) then
				0.001596031176573182
			else
				-0.02963619427115155
			end
		else
			-0.02375791825638472
		end
		as tree_119_score,
--tree120
		case when (thirdparty_info_period3_2 is null and true==true or thirdparty_info_period3_2<=0.000000) then
			case when (thirdparty_info_period1_2 is null and true==true or thirdparty_info_period1_2<=8.500000000000002) then
				0.002025891690484256
			else
				0.025330021211679012
			end
		else
			-0.0030547203244139986
		end
		as tree_120_score,
--tree121
		case when (thirdparty_info_period2_9 is null and true==true or thirdparty_info_period2_9<=0.000000) then
			case when (education_info5 is null and true==true or education_info5<=0.000000) then
				0.00464645082743161
			else
				-0.028143875868354887
			end
		else
			-0.005537776511629186
		end
		as tree_121_score,
--tree122
		case when (userinfo_17 is null and true==true or userinfo_17<=1.5000000000000002) then
			case when (userinfo_5 is null and true==true or userinfo_5<=2.5000000000000004) then
				0.0002261899918761835
			else
				0.02110622083755668
			end
		else
			-0.0134665626257595
		end
		as tree_122_score,
--tree123
		case when (education_info1 is null and true==true or education_info1<=0.000000) then
			case when (userinfo_16 is null and true==true or userinfo_16<=1.5000000000000002) then
				0.004273705340407611
			else
				-0.005413688171477153
			end
		else
			-0.02258981534429439
		end
		as tree_123_score,
--tree124
		case when (thirdparty_info_period2_3 is null and true==true or thirdparty_info_period2_3<=437.50000000000006) then
			case when (thirdparty_info_period2_5 is null and true==true or thirdparty_info_period2_5<=125.50000000000001) then
				0.00020677745090532849
			else
				-0.018628437447235125
			end
		else
			0.009903281996376294
		end
		as tree_124_score,
--tree125
		case when (thirdparty_info_period2_3 is null and true==true or thirdparty_info_period2_3<=184.50000000000003) then
			case when (thirdparty_info_period5_3 is null and true==true or thirdparty_info_period5_3<=312.50000000000006) then
				-0.006294804969750264
			else
				0.04455578714456568
			end
		else
			0.004149385557243195
		end
		as tree_125_score,
--tree126
		case when (thirdparty_info_period5_5 is null and true==true or thirdparty_info_period5_5<=44.50000000000001) then
			0.005791450072223086
		else
			case when (thirdparty_info_period5_3 is null and true==true or thirdparty_info_period5_3<=248.50000000000003) then
				-0.010922441459638603
			else
				0.0038872923725846715
			end
		end
		as tree_126_score,
--tree127
		case when (thirdparty_info_period2_10 is null and true==true or thirdparty_info_period2_10<=1.5000000000000002) then
			case when (thirdparty_info_period6_5 is null and true==true or thirdparty_info_period6_5<=83.50000000000001) then
				0.004774970215925026
			else
				-0.007101651425396947
			end
		else
			-0.008745893161040337
		end
		as tree_127_score,
--tree128
		case when (webloginfo_15 is null and true==true or webloginfo_15<=0.000000) then
			case when (socialnetwork_13 is null and true==true or socialnetwork_13<=0.000000) then
				-0.00044977003720687815
			else
				-0.01592861531069865
			end
		else
			0.006217146568619023
		end
		as tree_128_score,
--tree129
		case when (userinfo_14 is null and true==true or userinfo_14<=2.5000000000000004) then
			-0.010187419697623329
		else
			case when (thirdparty_info_period3_5 is null and true==true or thirdparty_info_period3_5<=133.50000000000003) then
				0.0038386196750917773
			else
				-0.008691589879221898
			end
		end
		as tree_129_score,
--tree130
		case when (thirdparty_info_period3_8 is null and true==true or thirdparty_info_period3_8<=484.50000000000006) then
			case when (thirdparty_info_period5_5 is null and true==true or thirdparty_info_period5_5<=46.50000000000001) then
				0.005162578737893871
			else
				-0.004638497917185175
			end
		else
			0.02838025133734683
		end
		as tree_130_score,
--tree131
		case when (thirdparty_info_period4_15 is null and true==true or thirdparty_info_period4_15<=528.5000000000001) then
			case when (thirdparty_info_period5_5 is null and true==true or thirdparty_info_period5_5<=53.50000000000001) then
				0.002419226020504579
			else
				-0.013241066615066197
			end
		else
			0.004519193451495968
		end
		as tree_131_score,
--tree132
		case when (thirdparty_info_period2_3 is null and true==true or thirdparty_info_period2_3<=184.50000000000003) then
			case when (thirdparty_info_period5_3 is null and true==true or thirdparty_info_period5_3<=312.50000000000006) then
				-0.0061856668984385755
			else
				0.04061796600417978
			end
		else
			0.0040008716709551894
		end
		as tree_132_score,
--tree133
		case when (thirdparty_info_period2_10 is null and true==true or thirdparty_info_period2_10<=4.500000000000001) then
			case when (thirdparty_info_period3_15 is null and true==true or thirdparty_info_period3_15<=361.50000000000006) then
				-0.004249202197699571
			else
				0.004594191700907493
			end
		else
			-0.022126345318072317
		end
		as tree_133_score,
--tree134
		case when (thirdparty_info_period3_1 is null and true==true or thirdparty_info_period3_1<=0.000000) then
			case when (thirdparty_info_period1_1 is null and true==true or thirdparty_info_period1_1<=4.500000000000001) then
				0.0008293104857805488
			else
				0.024269030091077053
			end
		else
			-0.0026179653779725785
		end
		as tree_134_score,
--tree135
		case when (education_info1 is null and true==true or education_info1<=0.000000) then
			case when (education_info5 is null and true==true or education_info5<=0.000000) then
				0.0014971048995832065
			else
				-0.029416370543376827
			end
		else
			-0.02192846194816209
		end
		as tree_135_score,
--tree136
		case when (thirdparty_info_period3_2 is null and true==true or thirdparty_info_period3_2<=0.000000) then
			case when (thirdparty_info_period1_2 is null and true==true or thirdparty_info_period1_2<=8.500000000000002) then
				0.002054334472116626
			else
				0.02298887814514541
			end
		else
			-0.002843273570268743
		end
		as tree_136_score,
--tree137
		case when (thirdparty_info_period3_10 is null and true==true or thirdparty_info_period3_10<=2.5000000000000004) then
			case when (userinfo_18 is null and true==true or userinfo_18<=21.500000000000004) then
				-0.018057153372347364
			else
				0.002163049133242866
			end
		else
			-0.013897776392685555
		end
		as tree_137_score,
--tree138
		case when (thirdparty_info_period1_10 is null and true==true or thirdparty_info_period1_10<=4.500000000000001) then
			case when (userinfo_5 is null and true==true or userinfo_5<=2.5000000000000004) then
				-0.00028880876171279455
			else
				0.017340894250731233
			end
		else
			-0.0224517078495462
		end
		as tree_138_score,
--tree139
		case when (userinfo_17 is null and true==true or userinfo_17<=1.5000000000000002) then
			case when (thirdparty_info_period3_5 is null and true==true or thirdparty_info_period3_5<=162.50000000000003) then
				0.0028677291263015745
			else
				-0.011355558932915835
			end
		else
			-0.012717706235491592
		end
		as tree_139_score,
--tree140
		case when (webloginfo_15 is null and true==true or webloginfo_15<=0.000000) then
			case when (socialnetwork_13 is null and true==true or socialnetwork_13<=0.000000) then
				-0.0006364984423399647
			else
				-0.015260610286578694
			end
		else
			0.0057162122803048
		end
		as tree_140_score,
--tree141
		case when (thirdparty_info_period2_3 is null and true==true or thirdparty_info_period2_3<=184.50000000000003) then
			case when (thirdparty_info_period3_3 is null and true==true or thirdparty_info_period3_3<=264.50000000000006) then
				-0.006239947631651269
			else
				0.03811857867757209
			end
		else
			0.0036786625780627843
		end
		as tree_141_score,
--tree142
		case when (thirdparty_info_period5_8 is null and true==true or thirdparty_info_period5_8<=488.50000000000006) then
			case when (thirdparty_info_period5_1 is null and true==true or thirdparty_info_period5_1<=5.500000000000001) then
				0.0031977975092339055
			else
				-0.005629796577086623
			end
		else
			0.03152377716661223
		end
		as tree_142_score,
--tree143
		case when (webloginfo_15 is null and true==true or webloginfo_15<=5.500000000000001) then
			-0.001276649757189952
		else
			case when (thirdparty_info_period2_6 is null and true==true or thirdparty_info_period2_6<=33.50000000000001) then
				0.0029246613047291844
			else
				0.03947781581478798
			end
		end
		as tree_143_score,
--tree144
		case when (thirdparty_info_period4_14 is null and true==true or thirdparty_info_period4_14<=4409.500000000001) then
			0.007735904112907458
		else
			case when (thirdparty_info_period4_15 is null and true==true or thirdparty_info_period4_15<=196.50000000000003) then
				-0.0121273089882806
			else
				0.0016754237155456955
			end
		end
		as tree_144_score,
--tree145
		case when (thirdparty_info_period6_14 is null and true==true or thirdparty_info_period6_14<=2351.5000000000005) then
			0.0045918098066176204
		else
			case when (thirdparty_info_period6_15 is null and true==true or thirdparty_info_period6_15<=192.50000000000003) then
				-0.012836163911457319
			else
				0.001283648047991749
			end
		end
		as tree_145_score,
--tree146
		case when (userinfo_18 is null and true==true or userinfo_18<=21.500000000000004) then
			-0.018811305250413336
		else
			case when (thirdparty_info_period4_5 is null and true==true or thirdparty_info_period4_5<=57.50000000000001) then
				0.006186530180908761
			else
				-0.0030349127487054703
			end
		end
		as tree_146_score,
--tree147
		case when (thirdparty_info_period1_10 is null and true==true or thirdparty_info_period1_10<=2.5000000000000004) then
			case when (thirdparty_info_period1_5 is null and true==true or thirdparty_info_period1_5<=153.50000000000003) then
				0.002573480266191893
			else
				-0.017289807874116117
			end
		else
			-0.011564406125410763
		end
		as tree_147_score,
--tree148
		case when (thirdparty_info_period2_3 is null and true==true or thirdparty_info_period2_3<=184.50000000000003) then
			-0.004378222508647421
		else
			case when (thirdparty_info_period3_4 is null and true==true or thirdparty_info_period3_4<=190.50000000000003) then
				0.015253938610060629
			else
				-0.0011233838707160567
			end
		end
		as tree_148_score,
--tree149
		case when (thirdparty_info_period1_9 is null and true==true or thirdparty_info_period1_9<=0.000000) then
			case when (userinfo_5 is null and true==true or userinfo_5<=2.5000000000000004) then
				0.0018169219694871596
			else
				0.024916985962203098
			end
		else
			-0.004790784464243962
		end
		as tree_149_score,
--tree150
		case when (userinfo_17 is null and true==true or userinfo_17<=1.5000000000000002) then
			case when (education_info1 is null and true==true or education_info1<=0.000000) then
				0.0020851416657608024
			else
				-0.02060290397881831
			end
		else
			-0.012585579851274337
		end
		as tree_150_score,
--tree151
		case when (thirdparty_info_period4_3 is null and true==true or thirdparty_info_period4_3<=339.50000000000006) then
			-0.0023052724836301504
		else
			case when (thirdparty_info_period2_7 is null and true==true or thirdparty_info_period2_7<=159.50000000000003) then
				0.08039615713572303
			else
				0.005339549857086289
			end
		end
		as tree_151_score,
--tree152
		case when (thirdparty_info_period2_10 is null and true==true or thirdparty_info_period2_10<=4.500000000000001) then
			case when (userinfo_16 is null and true==true or userinfo_16<=1.5000000000000002) then
				0.0036984343151158366
			else
				-0.004962315319536628
			end
		else
			-0.020870659255877902
		end
		as tree_152_score,
--tree153
		case when (thirdparty_info_period6_1 is null and true==true or thirdparty_info_period6_1<=2.5000000000000004) then
			0.0028742701089020865
		else
			case when (thirdparty_info_period3_8 is null and true==true or thirdparty_info_period3_8<=484.50000000000006) then
				-0.006311067563163797
			else
				0.0323095900542631
			end
		end
		as tree_153_score,
--tree154
		case when (thirdparty_info_period3_2 is null and true==true or thirdparty_info_period3_2<=0.000000) then
			case when (thirdparty_info_period6_14 is null and true==true or thirdparty_info_period6_14<=1005.5000000000001) then
				0.013269688037714356
			else
				-0.0012956177135207518
			end
		else
			-0.002583251316282308
		end
		as tree_154_score,
--tree155
		case when (thirdparty_info_period4_3 is null and true==true or thirdparty_info_period4_3<=339.50000000000006) then
			case when (thirdparty_info_period4_5 is null and true==true or thirdparty_info_period4_5<=57.50000000000001) then
				0.0035853920150453107
			else
				-0.009165033027953746
			end
		else
			0.007203699779225828
		end
		as tree_155_score,
--tree156
		case when (userinfo_14 is null and true==true or userinfo_14<=2.5000000000000004) then
			-0.00934382633943344
		else
			case when (thirdparty_info_period3_5 is null and true==true or thirdparty_info_period3_5<=133.50000000000003) then
				0.0033458638684606256
			else
				-0.008258698738223276
			end
		end
		as tree_156_score,
--tree157
		case when (thirdparty_info_period2_6 is null and true==true or thirdparty_info_period2_6<=2.5000000000000004) then
			case when (thirdparty_info_period3_6 is null and true==true or thirdparty_info_period3_6<=4.500000000000001) then
				-0.011774122251315258
			else
				0.01147273651151509
			end
		else
			0.0020981184267027677
		end
		as tree_157_score,
--tree158
		case when (thirdparty_info_period3_8 is null and true==true or thirdparty_info_period3_8<=484.50000000000006) then
			case when (thirdparty_info_period3_5 is null and true==true or thirdparty_info_period3_5<=121.50000000000001) then
				0.0015520738811285514
			else
				-0.009613448266622589
			end
		else
			0.024950135277146963
		end
		as tree_158_score,
--tree159
		case when (education_info5 is null and true==true or education_info5<=0.000000) then
			case when (webloginfo_17 is null and true==true or webloginfo_17<=6.500000000000001) then
				-0.0019679186714506047
			else
				0.007241057064036691
			end
		else
			-0.026145728209452226
		end
		as tree_159_score,
--tree160
		case when (thirdparty_info_period2_3 is null and true==true or thirdparty_info_period2_3<=304.50000000000006) then
			-0.00261728735239707
		else
			case when (thirdparty_info_period3_4 is null and true==true or thirdparty_info_period3_4<=296.50000000000006) then
				0.01688142659907307
			else
				-0.001527911689617284
			end
		end
		as tree_160_score,
--tree161
		case when (thirdparty_info_period1_10 is null and true==true or thirdparty_info_period1_10<=4.500000000000001) then
			case when (webloginfo_15 is null and true==true or webloginfo_15<=0.000000) then
				-0.0021321870982036846
			else
				0.006157721799802639
			end
		else
			-0.020855506765355903
		end
		as tree_161_score,
--tree162
		case when (userinfo_18 is null and true==true or userinfo_18<=21.500000000000004) then
			-0.017813217758165564
		else
			case when (education_info1 is null and true==true or education_info1<=0.000000) then
				0.0016060684024233247
			else
				-0.02032793362544656
			end
		end
		as tree_162_score,
--tree163
		case when (userinfo_17 is null and true==true or userinfo_17<=1.5000000000000002) then
			case when (thirdparty_info_period2_5 is null and true==true or thirdparty_info_period2_5<=170.50000000000003) then
				0.0025270567968915564
			else
				-0.01081154615131423
			end
		else
			-0.011494456358807597
		end
		as tree_163_score,
--tree164
		case when (thirdparty_info_period2_3 is null and true==true or thirdparty_info_period2_3<=486.50000000000006) then
			case when (thirdparty_info_period2_5 is null and true==true or thirdparty_info_period2_5<=138.50000000000003) then
				0.00016139941785549188
			else
				-0.01739340848118447
			end
		else
			0.009482869888891327
		end
		as tree_164_score,
--tree165
		case when (thirdparty_info_period2_3 is null and true==true or thirdparty_info_period2_3<=145.50000000000003) then
			case when (thirdparty_info_period4_3 is null and true==true or thirdparty_info_period4_3<=246.50000000000003) then
				-0.006797542939514726
			else
				0.0369226037678437
			end
		else
			0.0028884031437670064
		end
		as tree_165_score,
--tree166
		case when (thirdparty_info_period3_2 is null and true==true or thirdparty_info_period3_2<=0.000000) then
			case when (thirdparty_info_period1_2 is null and true==true or thirdparty_info_period1_2<=5.500000000000001) then
				0.0012140540782377566
			else
				0.01841232701490597
			end
		else
			-0.002381203554070422
		end
		as tree_166_score,
--tree167
		case when (socialnetwork_8 is null and true==true or socialnetwork_8<=133.50000000000003) then
			case when (thirdparty_info_period4_9 is null and true==true or thirdparty_info_period4_9<=1.5000000000000002) then
				0.00317203394476073
			else
				-0.00634472079565608
			end
		else
			-0.01480470950187861
		end
		as tree_167_score,
--tree168
		case when (userinfo_18 is null and true==true or userinfo_18<=21.500000000000004) then
			-0.0173884500988368
		else
			case when (thirdparty_info_period6_5 is null and true==true or thirdparty_info_period6_5<=81.50000000000001) then
				0.003087500459123734
			else
				-0.006480546563773263
			end
		end
		as tree_168_score,
--tree169
		case when (thirdparty_info_period2_3 is null and true==true or thirdparty_info_period2_3<=145.50000000000003) then
			case when (thirdparty_info_period3_3 is null and true==true or thirdparty_info_period3_3<=264.50000000000006) then
				-0.0061525068742399654
			else
				0.05086645933878641
			end
		else
			0.002732122376881495
		end
		as tree_169_score,
--tree170
		case when (thirdparty_info_period2_9 is null and true==true or thirdparty_info_period2_9<=0.000000) then
			0.0029179793625941993
		else
			case when (thirdparty_info_period2_13 is null and true==true or thirdparty_info_period2_13<=37733.50000000001) then
				-0.008501863223852702
			else
				0.005586764482508113
			end
		end
		as tree_170_score,
--tree171
		case when (userinfo_16 is null and true==true or userinfo_16<=1.5000000000000002) then
			case when (thirdparty_info_period4_8 is null and true==true or thirdparty_info_period4_8<=372.50000000000006) then
				0.0015755624915684216
			else
				0.023759768055732503
			end
		else
			-0.005278868126284921
		end
		as tree_171_score,
--tree172
		case when (thirdparty_info_period2_10 is null and true==true or thirdparty_info_period2_10<=4.500000000000001) then
			0.0007531594581651263
		else
			case when (thirdparty_info_period2_3 is null and true==true or thirdparty_info_period2_3<=942.5000000000001) then
				-0.024377691819540435
			else
				0.07266011715229809
			end
		end
		as tree_172_score,
--tree173
		case when (thirdparty_info_period1_9 is null and true==true or thirdparty_info_period1_9<=0.000000) then
			case when (userinfo_5 is null and true==true or userinfo_5<=2.5000000000000004) then
				0.0016279377665722496
			else
				0.02332406561265284
			end
		else
			-0.004217001401656834
		end
		as tree_173_score,
--tree174
		case when (webloginfo_15 is null and true==true or webloginfo_15<=5.500000000000001) then
			case when (socialnetwork_13 is null and true==true or socialnetwork_13<=0.000000) then
				0.0012585302930994318
			else
				-0.010369513116113196
			end
		else
			0.013502240814590172
		end
		as tree_174_score,
--tree175
		case when (webloginfo_17 is null and true==true or webloginfo_17<=6.500000000000001) then
			-0.0023110107993791337
		else
			case when (thirdparty_info_period5_3 is null and true==true or thirdparty_info_period5_3<=307.50000000000006) then
				0.0019449285609586299
			else
				0.02117540794413686
			end
		end
		as tree_175_score,
--tree176
		case when (thirdparty_info_period3_1 is null and true==true or thirdparty_info_period3_1<=0.000000) then
			case when (thirdparty_info_period1_1 is null and true==true or thirdparty_info_period1_1<=4.500000000000001) then
				0.0002056275424193977
			else
				0.021029396538876154
			end
		else
			-0.002198673045346081
		end
		as tree_176_score,
--tree177
		case when (userinfo_17 is null and true==true or userinfo_17<=1.5000000000000002) then
			case when (education_info1 is null and true==true or education_info1<=0.000000) then
				0.0019081857734437617
			else
				-0.019066061212641497
			end
		else
			-0.011198836124336394
		end
		as tree_177_score,
--tree178
		case when (thirdparty_info_period1_10 is null and true==true or thirdparty_info_period1_10<=4.500000000000001) then
			case when (thirdparty_info_period1_5 is null and true==true or thirdparty_info_period1_5<=155.50000000000003) then
				0.001555942608622676
			else
				-0.01464331783299624
			end
		else
			-0.02010745790939009
		end
		as tree_178_score,
--tree179
		case when (education_info5 is null and true==true or education_info5<=0.000000) then
			case when (thirdparty_info_period3_2 is null and true==true or thirdparty_info_period3_2<=0.000000) then
				0.006276303221648853
			else
				-0.0020642852814903695
			end
		else
			-0.025236047096318538
		end
		as tree_179_score,
--tree180
		case when (thirdparty_info_period3_6 is null and true==true or thirdparty_info_period3_6<=3.5000000000000004) then
			case when (thirdparty_info_period4_5 is null and true==true or thirdparty_info_period4_5<=12.500000000000002) then
				0.010618932087362793
			else
				-0.00911169155979207
			end
		else
			0.0024758215391816386
		end
		as tree_180_score,
--tree181
		case when (userinfo_16 is null and true==true or userinfo_16<=1.5000000000000002) then
			case when (thirdparty_info_period5_8 is null and true==true or thirdparty_info_period5_8<=488.50000000000006) then
				0.001985338026724089
			else
				0.04168778652343462
			end
		else
			-0.00489097052326526
		end
		as tree_181_score,
--tree182
		case when (thirdparty_info_period3_1 is null and true==true or thirdparty_info_period3_1<=0.000000) then
			0.005752493693056464
		else
			case when (thirdparty_info_period3_15 is null and true==true or thirdparty_info_period3_15<=368.50000000000006) then
				-0.007572776946048902
			else
				0.0013593327254439367
			end
		end
		as tree_182_score,
--tree183
		case when (socialnetwork_8 is null and true==true or socialnetwork_8<=143.50000000000003) then
			case when (thirdparty_info_period2_3 is null and true==true or thirdparty_info_period2_3<=145.50000000000003) then
				-0.004113142005621548
			else
				0.0036908627336395476
			end
		else
			-0.015366300118251158
		end
		as tree_183_score,
--tree184
		case when (userinfo_18 is null and true==true or userinfo_18<=21.500000000000004) then
			-0.016726705873237446
		else
			case when (webloginfo_17 is null and true==true or webloginfo_17<=6.500000000000001) then
				-0.0017926663264109365
			else
				0.00689300561720132
			end
		end
		as tree_184_score,
--tree185
		case when (thirdparty_info_period6_5 is null and true==true or thirdparty_info_period6_5<=96.50000000000001) then
			case when (thirdparty_info_period4_3 is null and true==true or thirdparty_info_period4_3<=316.50000000000006) then
				-0.0007830509477711441
			else
				0.012400629224038392
			end
		else
			-0.007363873389264257
		end
		as tree_185_score,
--tree186
		case when (thirdparty_info_period1_9 is null and true==true or thirdparty_info_period1_9<=0.000000) then
			0.0028448099950754476
		else
			case when (thirdparty_info_period1_3 is null and true==true or thirdparty_info_period1_3<=325.50000000000006) then
				-0.0071465340144421284
			else
				0.008342487514300258
			end
		end
		as tree_186_score,
--tree187
		case when (education_info1 is null and true==true or education_info1<=0.000000) then
			case when (thirdparty_info_period4_5 is null and true==true or thirdparty_info_period4_5<=57.50000000000001) then
				0.004792944612177477
			else
				-0.002547123489048007
			end
		else
			-0.018940887179910576
		end
		as tree_187_score,
--tree188
		case when (thirdparty_info_period1_10 is null and true==true or thirdparty_info_period1_10<=2.5000000000000004) then
			case when (thirdparty_info_period1_5 is null and true==true or thirdparty_info_period1_5<=153.50000000000003) then
				0.002223656442753074
			else
				-0.016005879026559602
			end
		else
			-0.01009894873679429
		end
		as tree_188_score,
--tree189
		case when (userinfo_17 is null and true==true or userinfo_17<=1.5000000000000002) then
			case when (userinfo_5 is null and true==true or userinfo_5<=2.5000000000000004) then
				0.0001487288530464026
			else
				0.015350466719914796
			end
		else
			-0.010700316126759668
		end
		as tree_189_score,
--tree190
		case when (education_info5 is null and true==true or education_info5<=0.000000) then
			case when (thirdparty_info_period5_5 is null and true==true or thirdparty_info_period5_5<=44.50000000000001) then
				0.005026846874756827
			else
				-0.0024393164792706323
			end
		else
			-0.0243661751788165
		end
		as tree_190_score,
--tree191
		case when (thirdparty_info_period4_15 is null and true==true or thirdparty_info_period4_15<=242.50000000000003) then
			case when (thirdparty_info_period4_14 is null and true==true or thirdparty_info_period4_14<=1878.5000000000002) then
				0.005897545153696814
			else
				-0.008926186838299965
			end
		else
			0.0027856342325260075
		end
		as tree_191_score,
--tree192
		case when (webloginfo_17 is null and true==true or webloginfo_17<=6.500000000000001) then
			-0.0022315274715297945
		else
			case when (thirdparty_info_period5_3 is null and true==true or thirdparty_info_period5_3<=303.50000000000006) then
				0.001544852771907702
			else
				0.018810813082619095
			end
		end
		as tree_192_score,
--tree193
		case when (socialnetwork_8 is null and true==true or socialnetwork_8<=143.50000000000003) then
			case when (thirdparty_info_period5_10 is null and true==true or thirdparty_info_period5_10<=1.5000000000000002) then
				0.0019536355132049265
			else
				-0.009085195692914686
			end
		else
			-0.014649490555221387
		end
		as tree_193_score,
--tree194
		case when (userinfo_15 is null and true==true or userinfo_15<=2.5000000000000004) then
			case when (thirdparty_info_period6_8 is null and true==true or thirdparty_info_period6_8<=516.5000000000001) then
				-0.008830566927805568
			else
				0.10890557907362637
			end
		else
			0.0013906151258223063
		end
		as tree_194_score,
--tree195
		case when (thirdparty_info_period3_5 is null and true==true or thirdparty_info_period3_5<=188.50000000000003) then
			case when (thirdparty_info_period2_3 is null and true==true or thirdparty_info_period2_3<=486.50000000000006) then
				-0.0007713758780066315
			else
				0.01383714791685936
			end
		else
			-0.013221699871526339
		end
		as tree_195_score,
--tree196
		case when (thirdparty_info_period1_10 is null and true==true or thirdparty_info_period1_10<=4.500000000000001) then
			case when (thirdparty_info_period1_5 is null and true==true or thirdparty_info_period1_5<=155.50000000000003) then
				0.0015103240742641638
			else
				-0.01343080716726062
			end
		else
			-0.018722019153331115
		end
		as tree_196_score,
--tree197
		case when (thirdparty_info_period3_1 is null and true==true or thirdparty_info_period3_1<=3.5000000000000004) then
			case when (thirdparty_info_period1_1 is null and true==true or thirdparty_info_period1_1<=5.500000000000001) then
				0.00022520584136836438
			else
				0.015200506471519638
			end
		else
			-0.0025855226416094143
		end
		as tree_197_score,
--tree198
		case when (thirdparty_info_period2_13 is null and true==true or thirdparty_info_period2_13<=32962.50000000001) then
			case when (thirdparty_info_period2_5 is null and true==true or thirdparty_info_period2_5<=129.50000000000003) then
				0.0001988161542035774
			else
				-0.02326349101276788
			end
		else
			0.005599593331742994
		end
		as tree_198_score,
--tree199
		case when (thirdparty_info_period5_8 is null and true==true or thirdparty_info_period5_8<=488.50000000000006) then
			case when (thirdparty_info_period6_5 is null and true==true or thirdparty_info_period6_5<=96.50000000000001) then
				0.0012728717899349973
			else
				-0.00875254437446788
			end
		else
			0.024254991303165708
		end
		as tree_199_score
        from input_table)
        