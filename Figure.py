#데이터 조감
import sqlite3
import pandas as pd
con = sqlite3.connect("C:/Users/user/Desktop/프로젝트/KOPIS/test_db.db")

#2019
print("2019")
print()
df = pd.read_sql("SELECT * FROM kopis_raw_data_2019",con,index_col=None)

print("저장완료")

print(df["공연장코드"].value_counts())
# FC222234-01    525993
# FC222233-01    439105
# FC222028-01    347149
# FC222253-01    332849
# FC222220-01    316733
#                 ...
# FC224542-01         1
# FC223508-02         1
# FC224414-01         1
# FC223356-02         1
# FC222436-01         1
# Name: 공연장코드, Length: 1001, dtype: int64

print(df["세부장르명"].value_counts())
# 뮤지컬         7202489
# 연극          3329041
# 기악          1299378
# 넌버벌 퍼포먼스     766364
# 발레           398335
# 성악           311192
# 복합           259095
# 오페라          235264
# 한국무용         118255
# 연희혼합          99405
# 현대무용          90264
# 인형극           35166
# 악극            34331
# 창극            31379
# 마당극           23606
# 마임             3904
# Name: 세부장르명, dtype: int64
print(df["공연지역명"].value_counts())
# 서울     10205558
# 경기도     1398062
# 경상도     1315809
# 전라도      539701
# 충청도      430596
# 제주도      231150
# 강원도      116588
# 해외            4
# Name: 공연지역명, dtype: int64
print(df["기획제작사명"].value_counts())
# (주)레드앤블루(구. 악어컴퍼니)(주관), (주)레드앤블루(구. 악어컴퍼니)(주최)                                                           541931
# (주)피엠씨프러덕션(PMC Production)(제작사)                                                                          510859
# (주)오디컴퍼니(ODCOMPANY)(제작사), 롯데엔터테인먼트(제작사), TBC(제작사), TJB 대전방송(제작사), 오픈리뷰(주)(주관), SBS(주최), (주)창작컴퍼니다(주관)    434530
# (주)CJ ENM(제작사)                                                                                           349014
# (주)신시컴퍼니(주최), SBS(주최)                                                                                    265624
#                                                                                                           ...
# JJ예술기획(주최)                                                                                                    1
# 리더라이히 예술기획(주관)                                                                                                1
# 진예술기획(주최)                                                                                                     1
# 앙상블트라움(주관), 앙상블트라움(주최)                                                                                        1
# (사)한국연극협회 광주시지회(주관), 광주시청(주최)                                                                                 1
# Name: 기획제작사명, Length: 3838, dtype: int64
print(df["관람연령"].value_counts())
# 만 7세 이상     5344621
# 만 13세 이상    3415349
# 24개월 이상     1309112
# 12개월 이상      674564
# 36개월 이상      661897
# 전체 관람가       620229
# 만 15세 이상     386908
# 만 5세 이상      264788
# 만 16세 이상     202906
# 48개월 이상      183217
# 만 12세 이상     170584
# 만 10세 이상     166980
# 만 8세 이상      163670
# 20개월 이상      154358
# 만 18세 이상     151197
# 만 6세 이상       93652
# 만 19세 이상      75958
# 만 14세 이상      56794
# 만 11세 이상      56087
# 만 9세 이상       52031
# 만 17세 이상      28183
# 만 23세 이상        691
# 만 20세 이상         20
# Name: 관람연령, dtype: int64
print()

#2020
print("2020")
print()
df = pd.read_sql("SELECT * FROM kopis_raw_data_2020",con,index_col=None)

print("저장완료")

print(df["공연장코드"].value_counts())
# FC222234-01    1177074
# FC222253-01    1054018
# FC222242-01     489333
# FC222236-02     475736
# FC222224-01     430493
#                 ...
# FC224534-01          1
# FC224964-01          1
# FC224757-01          1
# FC222950-01          1
# FC224959-01          1
# Name: 공연장코드, Length: 826, dtype: int64

print(df["세부장르명"].value_counts())
# 뮤지컬         8666695
# 연극          2817682
# 기악           813818
# 넌버벌 퍼포먼스     180136
# 성악           169106
# 오페라          101575
# 발레            81889
# 복합            67518
# 현대무용          44111
# 악극            25857
# 한국무용          25027
# 마당극           21815
# 연희혼합          21119
# 창극            13990
# 인형극            9963
# 마임              626
# Name: 세부장르명, dtype: int64
print(df["공연지역명"].value_counts())
# 서울     11591805
# 경상도      775600
# 경기도      311502
# 전라도      188039
# 충청도      115498
# 강원도       42657
# 제주도       35826
# Name: 공연지역명, dtype: int64

print(df["기획제작사명"].value_counts())
# (주)오디컴퍼니(ODCOMPANY)(제작사), 롯데엔터테인먼트(제작사), 씨제스컬처 ((주)씨제스엔터테인먼트)(제작사), TBC(제작사), SBS(주최), 오픈리뷰(주)(주관)    619826
# 롯데엔터테인먼트(제작사), MBC(주최), 에스앤코(S&CO)(제작사), 클립서비스(주관)                                                    357596
# (주)EMK뮤지컬컴퍼니(제작사), (재)세종문화회관(주최), (주)카카오(주최), SBS(주최)                                                 341458
# (주)신시컴퍼니(주최), SBS(주최)                                                                                 337452
# (주)CJ ENM(제작사), (주)CJ ENM(기획사)                                                                        311492
#                                                                                                        ...
# (재)부산문화회관(주최), 대전예술의전당(주최)                                                                                 1
# 대구음악협회(주최), 대구음악협회(주관)                                                                                     1
# 이화브릴란테앙상블(주최), 시티필하모니오케스트라(주관)                                                                             1
# 스트라디움(주최), 유나이티드프로듀서스(UPD)(주관)                                                                             1
# 공연예술창작집단 극단 기차(주최), 공연예술창작집단 극단 기차(기획사)                                                                    1
# Name: 기획제작사명, Length: 2860, dtype: int64
print(df["관람연령"].value_counts())
# 만 7세 이상     6094989
# 만 13세 이상    3872422
# 만 15세 이상     411261
# 24개월 이상      410529
# 만 16세 이상     327484
# 만 12세 이상     307794
# 12개월 이상      247504
# 만 10세 이상     198941
# 만 11세 이상     165469
# 전체 관람가       164024
# 48개월 이상      146967
# 36개월 이상      138384
# 만 18세 이상     125724
# 만 8세 이상       95682
# 만 14세 이상      85830
# 만 5세 이상       72532
# 만 19세 이상      61749
# 20개월 이상       52126
# 만 9세 이상       43530
# 만 6세 이상       16224
# 만 17세 이상      13920
# Name: 관람연령, dtype: int64
print()

#2021
print("2021")
print()
df = pd.read_sql("SELECT * FROM kopis_raw_data_2021",con,index_col=None)

print("저장완료")

print(df["공연장코드"].value_counts())
# FC222253-01    1117503
# FC222234-01    1020761
# FC222242-01     810863
# FC222236-02     717452
# FC222223-06     521721
#                 ...
# FC224670-01          1
# FC224531-01          1
# FC224701-01          1
# FC223597-01          1
# FC224060-01          1
# Name: 공연장코드, Length: 870, dtype: int64
print(df["세부장르명"].value_counts())
# 뮤지컬         10920234
# 연극           2805400
# 기악           1571839
# 성악            809059
# 발레            380555
# 오페라           232957
# 현대무용          135215
# 연희혼합          107937
# 복합            106234
# 넌버벌 퍼포먼스       85153
# 한국무용           46685
# 악극             44368
# 창극             28529
# 인형극            25094
# 마당극             3962
# 마임              2552
# Name: 세부장르명, dtype: int64
print(df["공연지역명"].value_counts())
# 서울     13509540
# 경상도     1635825
# 경기도     1178775
# 전라도      440005
# 충청도      368026
# 강원도      102548
# 제주도       71054
# Name: 공연지역명, dtype: int64
print(df["기획제작사명"].value_counts())
# SBS(주최), (주)오디컴퍼니(ODCOMPANY)(주최), TJB(주최), TBC(주최)                                                      452638
# (주)오디컴퍼니(ODCOMPANY)(제작사), 씨제스컬처 ((주)씨제스엔터테인먼트)(제작사), TBC(제작사), TJB 대전방송(제작사), SBS(주최), 롯데엔터테인먼트(제작사)    420716
# (재)세종문화회관(주최), (주)CJ ENM(주최), (주)CJ ENM(주관), (주)CJ ENM(제작사)                                             405402
# (주)EMK뮤지컬컴퍼니(제작사)                                                                                       305804
# (주)나인스토리(제작사)                                                                                           302115
#                                                                                                          ...
# 앙상블리안(주관), 피아노듀오 새벽별(주최)                                                                                     1
# 극단 동인재(제작사), 명일극장(제작사), 성동예인(제작사)                                                                            1
# 우리노래펼침이(주최), 현대문화기획(주관)                                                                                      1
# 서초아트센터(서초아트홀)(주최), 서초아트센터(서초아트홀)(기획사), 서초국제예술단(주관)                                                           1
# 보이스앙상블 베르떼(주최), 보이스앙상블 베르떼(주관)                                                                               1
# Name: 기획제작사명, Length: 5459, dtype: int64
print(df["관람연령"].value_counts())
# 만 7세 이상           7587237
# 만 13세 이상          4804183
# 24개월 이상            891439
# 만 15세 이상           762072
# 전체 관람가             482588
# 만 14세 이상           362159
# 12개월 이상            350663
# 만 12세 이상           334901
# 만 16세 이상           272487
# 48개월 이상            262110
# 36개월 이상            163546
# 만 8세 이상            149727
# 만 11세 이상           149405
# 만 5세 이상            108991
# 만 17세 이상           103254
# 만 18세 이상            85590
# 만 6세 이상             68949
# 만 19세 이상            68553
# 만 10세 이상            65147
# 20개월 이상             49975
# 만 4세 이상             48840
# 만 12세 드림아트센터이상      31371
# 만 9세 이상             22660
# 만 2세 이상             14473
# 만 13세 이상예술의전당        8687
# 만 3세 이상              6961
# 만  7세 이상             6944
# 만 5세이상               3859
# 8세                   1843
# 전체                   1106
# 만 7세이상               1013
# 60개월 이상               883
# 8세이상                  616
# 전체관람가                 578
# 전 체관람가                512
# 8세 이상 관람가             502
# 8세 이상                 486
# 만 7세 이상예술의전당          377
# 40개월 이상               236
# 48개월 이상 관가능           201
# 8세이상 관람가능             187
# 만 8 세이상               108
# 8세 이상 관람              101
# 초등학생이상 입장가능            97
# 0세 이상                  61
# 미취학아동입장불가              26
# 만 8세이상                 16
# 10개월 이상                10
# Name: 관람연령, dtype: int64
print()

#2022
print("2022")
print()
df = pd.read_sql("SELECT * FROM kopis_raw_data_2022",con,index_col=None)

print("저장완료")

print(df["공연장코드"].value_counts())

print(df["세부장르명"].value_counts())

print(df["공연지역명"].value_counts())
print(df["기획제작사명"].value_counts())
print(df["관람연령"].value_counts())

print()