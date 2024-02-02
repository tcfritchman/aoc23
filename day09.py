from itertools import tee

input_text = """5 13 45 115 234 420 731 1329 2591 5314 11131 23388 48974 102035 211293 434077 882526 1771333 3502944 6817585 13056927
12 34 63 97 134 172 209 243 272 294 307 309 298 272 229 167 84 -22 -153 -311 -498
0 8 26 57 105 173 258 346 429 605 1397 4561 14876 43758 116059 282152 638422 1360646 2756524 5345897 9980043
8 29 72 144 248 390 605 1026 2039 4596 10807 25025 55832 119755 248445 502919 1002134 1980015 3897262 7655070 14992036
9 27 56 112 226 457 930 1921 4030 8514 17905 37139 75621 151030 296349 572758 1092879 2061701 3846702 7094666 12920996
-3 -1 14 61 171 389 774 1400 2372 3888 6401 10974 20014 38812 78893 165423 353359 761461 1640856 3507131 7384045
11 29 63 133 274 553 1096 2121 3987 7294 13115 23530 42796 79765 152604 297574 584852 1146848 2229936 4292852 8201987
4 16 45 98 187 334 576 970 1598 2572 4039 6186 9245 13498 19282 26994 37096 50120 66673 87442 113199
4 10 9 -4 -25 -28 51 344 1122 2953 7021 15742 33959 71299 146804 297741 595488 1172324 2263237 4265428 7813247
11 26 63 134 248 417 684 1189 2299 4843 10514 22544 46882 94446 185855 361883 706595 1397224 2807865 5717282 11711740
20 29 41 64 125 279 625 1351 2840 5886 12105 24699 49870 99445 195794 381183 735856 1413383 2709829 5197774 9981223
-7 -2 21 73 165 308 513 791 1153 1610 2173 2853 3661 4608 5705 6963 8393 10006 11813 13825 16053
-6 -11 -24 -41 -38 39 287 875 2119 4670 9965 21263 45911 100042 217804 468587 987712 2028859 4050358 7852599 14790520
5 15 54 142 314 639 1261 2475 4863 9539 18583 35773 67738 125651 227614 402175 694524 1180023 1996985 3425534 6067133
13 28 68 148 283 483 748 1063 1393 1678 1828 1718 1183 13 -2052 -5327 -10187 -17072 -26492 -39032 -55357
15 18 21 24 27 30 33 36 39 42 45 48 51 54 57 60 63 66 69 72 75
5 18 33 53 95 206 501 1235 2929 6587 14070 28747 56662 108740 205218 384937 725081 1382564 2678351 5263233 10431797
11 30 65 116 182 271 422 753 1557 3476 7791 16874 34856 68573 128860 232271 403311 677274 1103789 1751184 2711786
13 25 41 76 159 333 655 1196 2041 3289 5053 7460 10651 14781 20019 26548 34565 44281 55921 69724 85943
20 34 61 124 263 551 1135 2313 4668 9304 18267 35286 67035 125197 229705 413643 730412 1263902 2142561 3558416 5792279
7 15 43 110 258 564 1162 2283 4320 7924 14136 24559 41573 68595 110385 173398 266181 399813 588385 849516 1204900
29 43 66 115 214 394 693 1156 1835 2789 4084 5793 7996 10780 14239 18474 23593 29711 36950 45439 55314
4 17 39 73 120 180 260 391 662 1305 2929 7119 17797 43983 104875 238446 514964 1056877 2066231 3860025 6912426
19 42 78 135 226 382 672 1230 2308 4408 8595 17157 34857 71116 143575 283608 544497 1013134 1826284 3192627 5421996
12 27 50 78 108 137 162 180 188 183 162 122 60 -27 -142 -288 -468 -685 -942 -1242 -1588
19 36 67 115 181 265 367 488 631 802 1011 1273 1609 2047 2623 3382 4379 5680 7363 9519 12253
8 29 68 145 308 662 1413 2926 5796 10931 19659 33928 56836 94142 158318 278529 523344 1048993 2196038 4673419 9893652
6 5 -4 -25 -62 -119 -200 -309 -450 -627 -844 -1105 -1414 -1775 -2192 -2669 -3210 -3819 -4500 -5257 -6094
27 48 71 98 134 197 336 654 1337 2711 5406 10820 22281 47685 105152 234859 523651 1156219 2521255 5429961 11560256
8 21 50 97 166 264 394 547 717 986 1756 4243 11395 29453 70442 155959 322718 630419 1172630 2091509 3597348
21 34 50 77 146 332 792 1842 4108 8797 18144 36109 69459 129579 235985 424195 764706 1409015 2697917 5405540 11264583
7 7 13 42 128 337 788 1680 3325 6187 10927 18454 29982 47093 71806 106652 154755 219919 306721 420610 568012
1 2 11 37 101 248 557 1142 2134 3631 5600 7712 9088 7931 1016 -16993 -54433 -123776 -243047 -437569 -742081
15 30 65 137 271 501 865 1386 2035 2691 3159 3396 4247 9232 28279 84799 228183 554708 1241013 2595795 5137231
9 16 27 41 68 138 309 677 1394 2703 5002 8952 15647 26867 45438 75726 124295 200762 318885 497923 764310
28 39 54 95 208 477 1048 2166 4240 7992 14830 27726 53092 104444 209040 419187 830548 1610557 3040982 5579777 9948648
1 19 52 100 163 241 334 442 565 703 856 1024 1207 1405 1618 1846 2089 2347 2620 2908 3211
7 17 39 100 242 522 1012 1799 2985 4687 7037 10182 14284 19520 26082 34177 44027 55869 69955 86552 105942
14 23 40 63 90 119 148 175 198 215 224 223 210 183 140 79 -2 -105 -232 -385 -566
-1 1 1 -5 -17 -12 94 525 1801 5020 12327 27642 57729 113697 213032 382266 660395 1103163 1788333 2822069 4346555
8 19 38 70 118 183 273 431 792 1679 3748 8192 17014 33379 62055 109953 186776 305787 484706 746746 1121798
4 12 31 58 92 145 262 551 1224 2650 5421 10432 18976 32855 54508 87157 134972 203256 298651 429366 605428
13 21 27 37 66 149 360 837 1820 3726 7306 13946 26174 48406 87925 156171 271051 463195 795077 1415855 2704006
-3 -1 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37
15 18 21 24 27 30 33 36 39 42 45 48 51 54 57 60 63 66 69 72 75
8 13 27 50 82 123 173 232 300 377 463 558 662 775 897 1028 1168 1317 1475 1642 1818
23 34 47 72 144 336 766 1593 2997 5138 8089 11738 15654 18912 19872 15907 3075 -24270 -73933 -156404 -285460
8 18 52 122 244 453 845 1668 3499 7562 16259 33998 68405 131997 244366 434876 745802 1235738 1982966 3088306 4676754
4 15 37 79 154 282 507 952 1943 4246 9491 20919 44713 92440 185736 365780 713350 1392389 2744869 5494063 11168348
18 28 38 48 58 68 78 88 98 108 118 128 138 148 158 168 178 188 198 208 218
14 27 48 85 144 237 395 690 1279 2492 4995 10068 20047 38988 73620 134663 238596 409969 684362 1112103 1762866
22 30 34 34 30 22 10 -6 -26 -50 -78 -110 -146 -186 -230 -278 -330 -386 -446 -510 -578
5 8 12 24 58 137 291 557 1004 1828 3599 7814 18050 42267 97242 216782 466329 967934 1941612 3772550 7120372
15 28 58 106 171 246 308 307 172 -124 -358 447 5134 20744 63225 166563 399685 896204 1904062 3863988 7526669
9 22 51 113 229 428 759 1311 2245 3863 6799 12562 24983 53793 122906 288547 677041 1560252 3500407 7618363 16074497
13 19 31 70 174 416 936 1997 4092 8156 15980 30993 59686 114112 216116 404225 744435 1346413 2386785 4141044 7024946
15 32 55 80 111 176 355 835 2018 4727 10587 22708 46870 93511 180953 340473 624041 1115810 1948759 3328264 5564809
25 45 89 186 393 815 1631 3136 5825 10562 18901 33675 60074 107639 193966 351518 639877 1167143 2126133 3853700 6925051
5 22 50 100 203 420 866 1772 3618 7378 14933 29748 58015 110728 207785 386676 721681 1367140 2655366 5316642 10966081
12 31 68 145 309 658 1379 2793 5392 9849 16995 27798 43459 65870 98870 150998 240788 406091 719454 1312247 2411017
7 15 23 28 27 17 -5 -42 -97 -173 -273 -400 -557 -747 -973 -1238 -1545 -1897 -2297 -2748 -3253
4 4 5 1 -6 7 102 417 1248 3222 7643 17160 37036 77557 158640 318708 631759 1239756 2412515 4654320 8884423
10 24 44 70 108 187 392 932 2281 5461 12592 27935 59827 124186 250690 493355 948108 1781134 3273340 5888300 10373606
21 41 81 146 248 427 779 1492 2900 5576 10490 19245 34357 59444 99010 157225 234679 321491 384343 343940 38022
-5 0 9 30 96 292 810 2049 4778 10391 21328 41852 79609 148819 276627 515173 963421 1804834 3369723 6234674 11376022
16 43 90 177 339 641 1211 2297 4366 8299 15818 30451 59670 119441 243512 501765 1035831 2128042 4336165 8760156 17575100
23 31 37 39 44 77 190 471 1053 2123 3931 6799 11130 17417 26252 38335 54483 75639 102881 137431 180664
3 14 43 103 215 408 719 1193 1883 2850 4163 5899 8143 10988 14535 18893 24179 30518 38043 46895 57223
3 18 45 90 175 361 783 1697 3539 6996 13089 23268 39519 64483 101587 155187 230723 334886 475797 663198 908655
8 16 31 61 120 228 411 701 1136 1760 2623 3781 5296 7236 9675 12693 16376 20816 26111 32365 39688
1 -3 -4 -1 14 80 301 892 2256 5138 10939 22320 44283 85983 163602 304703 554579 985219 1707630 2888381 4771372
5 3 10 44 135 325 668 1230 2089 3335 5070 7408 10475 14409 19360 25490 32973 41995 52754 65460 80335
13 22 37 70 155 367 848 1834 3672 6811 11746 18889 28336 39494 50527 57575 53695 27468 -38789 -171272 -407471
21 28 39 67 140 316 713 1560 3278 6624 12991 25068 48241 93374 181963 355121 688443 1315532 2463855 4507657 8043906
10 19 37 75 166 388 908 2051 4391 8850 16776 29952 50465 80337 120789 170974 225976 273829 291263 237833 48032
1 10 39 106 256 571 1175 2234 3951 6556 10291 15390 22054 30421 40531 52286 65405 79374 93391 106306 116556
12 23 42 84 177 360 681 1195 1962 3045 4508 6414 8823 11790 15363 19581 24472 30051 36318 43256 50829
29 47 77 140 284 607 1297 2709 5510 10934 21200 40157 74231 133760 234814 401608 669627 1089593 1732415 2695274 4109006
5 2 -8 -23 -30 8 186 731 2147 5482 12802 28024 58398 117198 228671 437117 823281 1533218 2827680 5164167 9329458
9 24 44 72 122 232 486 1054 2256 4657 9216 17556 32513 59290 107844 197714 367755 696209 1343618 2647317 5331424
13 20 31 57 122 263 530 986 1707 2782 4313 6415 9216 12857 17492 23288 30425 39096 49507 61877 76438
-5 -11 -18 -23 -11 60 272 764 1768 3701 7402 14716 29866 62549 134687 294694 646727 1408887 3025632 6378637 13171169
20 45 75 107 136 153 144 98 44 162 1070 4506 14838 42192 108543 258931 581116 1238555 2523661 4940989 9333396
4 1 13 49 122 255 485 865 1464 2365 3661 5449 7822 10859 14613 19097 24268 30009 36109 42241 47938
20 33 65 136 272 516 952 1758 3332 6577 13487 28246 59136 121648 243302 470808 880340 1591849 2788509 4742572 7849104
9 35 86 180 343 609 1020 1626 2485 3663 5234 7280 9891 13165 17208 22134 28065 35131 43470 53228 64559
6 18 51 118 236 428 725 1168 1810 2718 3975 5682 7960 10952 14825 19772 26014 33802 43419 55182 69444
19 39 80 164 328 631 1176 2155 3932 7198 13267 24637 46019 86144 160797 297702 544097 978097 1725250 2982050 5048586
2 17 55 131 260 457 737 1115 1606 2225 2987 3907 5000 6281 7765 9467 11402 13585 16031 18755 21772
12 17 23 26 26 31 69 216 654 1787 4473 10506 23681 52271 114903 254366 569202 1283563 2896273 6488056 14334358
21 42 77 128 198 291 412 567 763 1008 1311 1682 2132 2673 3318 4081 4977 6022 7233 8628 10226
-8 -9 8 57 151 309 575 1058 2013 4004 8240 17293 36653 78038 166211 352581 741792 1543371 3172446 6447547 12980373
-6 8 34 81 171 340 638 1139 1997 3622 7107 15133 33766 75952 168332 364618 771805 1600918 3263454 6551270 12967736
5 16 37 85 194 432 931 1930 3831 7268 13189 22951 38428 62132 97347 148276 220201 319656 454613 634681 871318
14 23 36 65 134 274 512 851 1238 1530 1514 1144 1365 6258 27857 96049 277874 714133 1688140 3754775 7983044
-2 -6 -1 37 145 379 835 1709 3447 7084 14946 31994 68224 142699 289972 569854 1081676 1984374 3523873 6069339 10159883
10 25 40 55 70 85 100 115 130 145 160 175 190 205 220 235 250 265 280 295 310
6 8 21 55 120 226 383 601 890 1260 1721 2283 2956 3750 4675 5741 6958 8336 9885 11615 13536
7 11 19 43 102 220 427 778 1417 2725 5603 11953 25432 52566 104323 198256 361339 633631 1072915 1760471 2808154
6 16 37 81 170 336 621 1077 1766 2760 4141 6001 8442 11576 15525 20421 26406 33632 42261 52465 64426
8 4 16 62 168 383 807 1630 3180 5987 10897 19344 34072 61017 113946 225231 469536 1013378 2214254 4810846 10274216
14 34 63 107 176 285 463 777 1387 2671 5500 11806 25675 55316 116410 237534 468588 893432 1648269 2947693 5120762
7 4 9 33 101 267 650 1510 3395 7425 15854 33181 68274 138222 274914 535608 1018907 1887466 3398219 5939673 10073519
2 -3 -8 -13 -18 -23 -28 -33 -38 -43 -48 -53 -58 -63 -68 -73 -78 -83 -88 -93 -98
12 27 53 95 155 228 312 447 798 1797 4359 10187 22181 44966 85554 154155 265152 438255 699849 1084551 1636991
7 10 22 41 58 55 11 -65 -36 591 3119 10463 28429 67568 145610 290299 542141 956104 1600628 2551365 3875820
8 20 57 137 294 600 1198 2360 4606 8946 17345 33579 64776 124157 235847 443145 822344 1505117 2713796 4816071 8409952
28 47 72 103 140 183 232 287 348 415 488 567 652 743 840 943 1052 1167 1288 1415 1548
29 45 66 91 115 144 225 491 1221 2915 6384 12855 24091 42526 71415 114999 178685 269241 395006 566115 794739
16 23 29 32 38 76 228 688 1873 4618 10502 22382 45263 87700 163988 297380 524326 898925 1494799 2397284 3670196
8 16 24 32 40 48 56 64 72 80 88 96 104 112 120 128 136 144 152 160 168
23 42 66 103 174 314 565 962 1526 2310 3608 6558 14596 36629 93516 230686 541899 1213241 2604777 5405295 10935074
16 14 15 21 45 135 413 1149 2905 6795 14909 30937 60998 114624 205765 353563 582486 921212 1399403 2041205 2853947
12 24 53 114 237 482 972 1952 3880 7564 14393 26792 49189 90050 165956 309310 582124 1099504 2067989 3845878 7035173
15 29 65 143 288 530 904 1450 2213 3243 4595 6329 8510 11208 14498 18460 23179 28745 35253 42803 51500
9 11 20 36 59 89 126 170 221 279 344 416 495 581 674 774 881 995 1116 1244 1379
18 37 67 121 231 462 929 1826 3489 6541 12231 23218 45324 91291 188511 394370 825764 1714281 3506627 7042691 13863349
-3 8 36 89 188 378 741 1426 2718 5182 9955 19337 37979 75240 149817 298836 595877 1187316 2367016 4732517 9515664
3 8 21 51 112 215 366 581 929 1627 3251 7205 16717 38838 88321 195195 420185 887767 1859441 3897074 8221156
22 32 48 84 174 382 823 1706 3410 6604 12422 22704 40314 69546 116629 190342 302750 470072 713692 1061324 1548342
15 18 20 17 18 64 249 753 1917 4428 9747 21016 44839 94577 196175 398119 787999 1519458 2855202 5234439 9376860
13 23 37 73 158 328 628 1112 1843 2893 4343 6283 8812 12038 16078 21058 27113 34387 43033 53213 65098
3 10 24 44 71 113 196 376 754 1514 3037 6199 13055 28284 62102 135980 293649 621846 1288474 2610850 5174147
6 20 52 128 300 665 1389 2736 5109 9124 15759 26648 44625 74665 125418 211588 357472 602044 1006046 1661632 2705202
4 21 60 149 346 764 1604 3194 6032 10831 18564 30507 48278 73870 109676 158504 223580 308537 417388 554481 724434
9 16 23 30 37 44 51 58 65 72 79 86 93 100 107 114 121 128 135 142 149
20 46 80 120 165 210 240 242 271 639 2359 8083 23938 62901 150677 335467 703550 1403268 2680810 4932154 8776659
4 17 47 97 168 253 329 363 366 552 1691 5802 17457 46256 111674 252807 548117 1155067 2388362 4872041 9832555
15 33 68 117 170 212 229 218 201 243 474 1115 2508 5150 9731 17176 28691 45813 70464 105009 152318
13 20 41 83 161 311 600 1137 2100 3814 6953 13006 25260 50742 103891 213356 434615 873932 1735261 3414389 6689787
1 12 40 101 226 465 893 1618 2791 4618 7374 11419 17216 25351 36555 51728 71965 98584 133156 177537 233902
9 14 37 102 245 515 974 1697 2773 4308 6431 9304 13137 18209 24896 33707 45329 60682 80985 107834 143293
2 1 1 15 66 187 421 821 1450 2381 3697 5491 7866 10935 14821 19657 25586 32761 41345 51511 63442
8 23 42 61 89 161 351 780 1614 3052 5314 8654 13443 20392 31015 48467 78932 133781 232770 408603 713245
1 21 64 134 227 327 411 473 578 958 2163 5281 12242 26222 52164 97434 172631 292571 477466 754320 1158565
9 1 -1 27 132 392 931 1955 3841 7346 14067 27404 54523 110325 225458 462396 947246 1931349 3907858 7828085 15498491
15 28 58 125 275 598 1254 2509 4783 8712 15226 25645 41795 66146 101974 153549 226351 327316 465114 650461 896467
18 31 53 96 175 308 516 823 1256 1845 2623 3626 4893 6466 8390 10713 13486 16763 20601 25060 30203
1 21 65 144 275 497 903 1690 3234 6213 11839 22339 41972 79119 150379 288197 554399 1063181 2018669 3774218 6923241
10 29 65 133 254 453 770 1297 2254 4117 7811 14981 28354 52205 92940 159809 265762 428461 671461 1025573 1530422
-5 7 41 110 226 399 639 959 1386 2019 3251 6427 15482 40553 105300 260935 612242 1365256 2915090 6010569 12069795
21 38 62 107 197 366 658 1127 1837 2862 4286 6203 8717 11942 16002 21031 27173 34582 43422 53867 66101
-3 -4 -8 -15 -25 -38 -54 -73 -95 -120 -148 -179 -213 -250 -290 -333 -379 -428 -480 -535 -593
13 34 73 140 244 396 611 919 1420 2456 5026 11651 28046 66274 150749 329908 699259 1446934 2942547 5906638 11724972
1 -1 -3 -5 -7 -9 -11 -13 -15 -17 -19 -21 -23 -25 -27 -29 -31 -33 -35 -37 -39
8 23 48 81 130 239 530 1268 2971 6613 14005 28483 56078 107395 200511 365366 650422 1132803 1933518 3239109 5328782
6 12 22 47 100 189 320 528 960 2040 4752 11083 24674 51733 102270 191720 343026 589260 976866 1569615 2453368
18 30 49 77 112 141 140 96 84 472 2400 8799 26401 69465 166340 370550 778882 1560074 2999255 5565441 10012346
20 43 90 174 322 593 1113 2140 4188 8266 16327 32080 62412 119839 226769 423215 781652 1437489 2654100 4962934 9461150
6 13 39 100 221 433 770 1266 1945 2784 3609 3855 2077 -4972 -23995 -68011 -161132 -346233 -696681 -1333186 -2446047
0 -1 8 42 133 340 760 1540 2898 5189 9112 16258 30359 59826 122472 253716 520068 1040315 2017576 3786282 6879177
12 29 53 94 184 398 896 2011 4420 9448 19565 39148 75618 141176 255631 451343 782220 1340139 2284217 3891098 6637812
24 48 83 135 216 344 543 843 1280 1896 2739 3863 5328 7200 9551 12459 16008 20288 25395 31431 38504
11 25 58 120 223 400 746 1491 3115 6515 13234 25762 47919 85330 146002 241013 385323 598717 906890 1342684 1947487
5 9 22 66 175 390 750 1279 1969 2759 3510 3976 3771 2332 -1122 -7635 -18563 -35627 -60970 -97218 -147545
14 32 58 100 172 294 492 798 1250 1892 2774 3952 5488 7450 9912 12954 16662 21128 26450 32732 40084
13 19 38 95 236 554 1236 2640 5416 10692 20355 37468 66877 116077 196423 324791 525815 834849 1301828 1996229 3013362
-2 -4 -7 -15 -26 -14 98 476 1426 3460 7379 14375 26154 45082 74356 118202 182102 273052 399853 573437 807230
20 47 96 174 296 510 937 1829 3659 7276 14200 27233 51785 98755 190601 373560 741070 1476589 2928552 5736576 11036710
9 21 51 126 298 663 1389 2759 5238 9571 16911 28979 48321 78954 128282 212465 370023 693269 1395551 2946168 6326812
9 32 73 140 255 462 831 1458 2461 3972 6125 9040 12803 17442 22899 28998 35409 41608 46833 50036 49831
12 25 54 104 193 375 766 1573 3137 6018 11173 20307 36512 65350 116583 206806 363298 629471 1072368 1792738 2938299
2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12 -13 -14 -15 -16 -17 -18
3 11 27 56 102 169 276 501 1088 2680 6776 16548 38202 83175 171793 339979 653037 1236005 2341217 4494776 8801058
1 -4 -6 2 31 112 320 816 1930 4321 9263 19119 38078 73243 136171 244979 427143 723130 1191016 1912256 2998785
3 6 9 13 25 58 131 269 503 870 1413 2181 3229 4618 6415 8693 11531 15014 19233 24285 30273
3 -1 -4 -6 -7 -7 -6 -4 -1 3 8 14 21 29 38 48 59 71 84 98 113
13 16 31 72 171 391 853 1788 3635 7233 14219 27894 55158 110850 227371 475612 1009429 2157809 4610859 9784975 20520225
7 15 36 85 185 373 727 1429 2894 6035 12813 27353 58106 121817 250434 502577 981793 1864567 3441954 6179757 10803415
14 17 16 6 -5 25 196 689 1783 3860 7391 12895 20862 31630 45205 61012 77564 92035 99722 93380 62413
8 16 31 72 169 377 804 1653 3275 6229 11362 19990 34433 59509 106226 199958 397014 815906 1693029 3477160 6983485
28 54 91 140 207 307 481 851 1758 4065 9780 23287 53699 119230 255167 528317 1063312 2090960 4037741 7691418 14504863
19 45 100 213 442 884 1689 3084 5420 9274 15686 26716 46714 85088 162074 320300 647181 1316975 2667532 5336587 10497526
-1 18 55 126 265 544 1114 2273 4563 8892 16666 29892 51159 83289 128234 184474 241917 273782 227938 29639 -368563
17 20 19 14 5 -8 -25 -46 -71 -100 -133 -170 -211 -256 -305 -358 -415 -476 -541 -610 -683
14 23 49 106 222 458 946 1962 4054 8246 16337 31309 57850 102987 176810 293251 470862 733513 1110905 1638764 2358550
1 7 24 64 143 280 491 785 1180 1771 2899 5490 11656 25676 55504 114983 226979 427687 772402 1343092 2258157
13 12 11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7
-3 1 7 23 69 179 404 820 1548 2804 5018 9104 17078 33535 69261 149904 335831 765031 1740529 3899025 8520627
5 17 56 150 345 714 1380 2559 4624 8187 14210 24230 41010 70489 127120 247110 518703 1147378 2590486 5828141 12900371
21 27 31 41 81 213 565 1373 3067 6462 13155 26278 51815 100758 192453 359572 655241 1162957 2010039 3385479 5563189
20 30 33 32 43 106 306 821 2041 4849 11238 25589 57207 125184 267440 557031 1130694 2237356 4318251 8135706 14974975
14 19 33 63 124 253 526 1077 2118 3959 7027 11883 19236 29953 45064 65761 93390 129435 175493 233239 304380
9 20 38 72 149 324 702 1488 3087 6283 12544 24551 47174 89388 168168 316490 599761 1149520 2232700 4394690 8756683
21 22 30 65 169 434 1050 2378 5062 10217 19767 37054 67895 122355 217731 383864 673485 1184069 2106184 3831998 7197659
6 18 42 84 157 288 527 963 1757 3207 5863 10721 19596 36044 67958 134711 285280 640396 1483200 3441590 7834687
6 15 31 54 87 136 210 321 484 717 1041 1480 2061 2814 3772 4971 6450 8251 10419 13002 16051
20 30 48 72 94 105 118 234 784 2585 7352 18316 41128 85228 166122 309608 560200 998261 1774406 3176839 5759690
12 30 52 87 170 373 811 1654 3169 5829 10539 19042 34581 62906 113728 202735 354298 605008 1008198 1639617 2604436
-6 -13 -22 -33 -46 -61 -78 -97 -118 -141 -166 -193 -222 -253 -286 -321 -358 -397 -438 -481 -526
11 24 45 77 121 184 312 677 1766 4749 12148 28996 64770 136511 273713 525778 973101 1743174 3033487 5143463 8518199
21 41 79 142 231 338 438 482 404 160 -166 -99 1868 9771 33451 95239 242735 571867 1266473 2663384 5355533
11 23 35 47 68 121 242 469 810 1174 1267 538 -1522 -3962 -175 32404 155160 516078 1445918 3646814 8554127
12 31 55 84 119 162 217 289 378 465 487 298 -387 -2068 -5559 -12113 -23576 -42573 -72729 -118928 -187613
5 10 24 63 149 301 523 805 1182 1940 4122 10588 28057 70868 167736 373683 790775 1603530 3138176 5959697 11027249
13 27 47 88 180 375 760 1476 2743 4891 8397 13928 22390 34983 53262 79204 115281 164539 230683 318168 432296
15 23 38 79 183 415 878 1723 3159 5463 8990 14183 21583 31839 45718 64115 88063 118743 157494 205823 265415
19 33 49 63 72 74 68 54 33 7 -21 -47 -66 -72 -58 -16 63 189 373 627 964
28 56 106 191 341 631 1237 2540 5311 11025 22378 44141 84612 158160 289740 522859 933398 1653142 2909198 5089311 8849439
26 44 68 100 144 201 263 305 273 72 -421 -1233 -1812 450 14158 63440 209216 593632 1527766 3656462 8255164"""


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def extrapolate_forward(l):
    if all([n == 0 for n in l]):
        return 0
    else:
        l2 = [b - a for a, b in pairwise(l)]
        return extrapolate_forward(l2) + l[-1]


def extrapolate_backward(l):
    if all([n == 0 for n in l]):
        return 0
    else:
        l2 = [b - a for a, b in pairwise(l)]
        return l[0] - extrapolate_backward(l2)


def part_1(text):
    total = 0
    for line in text.splitlines():
        nums = [int(n) for n in line.split(" ")]
        total += extrapolate_forward(nums)
    return total


def part_2(text):
    total = 0
    for line in text.splitlines():
        nums = [int(n) for n in line.split(" ")]
        total += extrapolate_backward(nums)
    return total


if __name__ == '__main__':
    print("Part 1: %d" % (part_1(input_text)))
    print("Part 2: %d" % (part_2(input_text)))
