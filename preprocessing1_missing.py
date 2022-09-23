
# '공연장코드',
# ,'공연코드','예매/취소구분',,'할인종류코드',
# ,'성별','연령',,'세부장르명','공연지역명','기획제작사명','관람연령',
# '아동공연 여부','오픈런 여부'

## numerical : '무대시설_무대넓이','공연회차','할인금액','장당금액','소요시간'
## categorical : '편의시설_놀이방 여부','장애인시설_주차장 여부','장애인시설_화장실 여부'
##           '장애인시설_경사로 여부','장애인시설_전용엘리베이터 여부','주차시설_자체 여부'
##           '주차시설_공영 여부','장애인석','무대시설_오케스트라피트 여부',
## one-hot encoding :
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from sklearn import preprocessing
from tqdm import tqdm
import time
import random
import os

con = sqlite3.connect("C:/Users/user/Desktop/프로젝트/KOPIS/test_db.db")
pd.set_option('mode.chained_assignment',  None) #SettingWithCopyWarning 끄기
# (데이터)'19년 하반기~ '22년 상반기 공모전 raw데이터_2019_07_01_10_389,999.xlsx
file_list = os.listdir('./data/2020')

for file_name in file_list:
    tmp = "./data/2020/" + file_name

    # df = pd.read_excel("./data/test_data.xlsx")[['편의시설_놀이방 여부', '장애인시설_주차장 여부', '장애인시설_화장실 여부',
    #                                              '장애인시설_경사로 여부', '장애인시설_전용엘리베이터 여부', '주차시설_자체 여부',
    #                                              '주차시설_공영 여부', '공연장코드', '장애인석', '무대시설_오케스트라피트 여부',
    #                                              '공연코드', '공연회차', '예매/취소구분', '할인금액',
    #                                              '장당금액', '성별', '연령', '소요시간', '장르명', '세부장르명', '공연지역명', '기획제작사명', '관람연령',
    #                                              '아동공연 여부', '오픈런 여부']]

    df = pd.read_excel(tmp)[['편의시설_놀이방 여부','장애인시설_주차장 여부','장애인시설_화장실 여부',
                                      '장애인시설_경사로 여부','장애인시설_전용엘리베이터 여부','주차시설_자체 여부',
                                      '주차시설_공영 여부','공연장코드','장애인석','무대시설_오케스트라피트 여부',
                                      '공연코드','공연회차','예매/취소구분','할인금액','할인종류코드',
                                      '장당금액','성별','연령','소요시간','장르명','세부장르명','공연지역명','기획제작사명','관람연령',
                                      '아동공연 여부','오픈런 여부']]

    # df = pd.read_sql("SELECT * FROM kopis_ver2_2020", con, index_col=None)

    print("저장 완료")
    # df["편의시설_놀이방 여부"].plot(kind="box")

    ## categorical => Y/N

    df.info()

    # 0   편의시설_놀이방 여부       389999 non-null  object
    #  1   장애인시설_주차장 여부      389999 non-null  object
    #  2   장애인시설_화장실 여부      389999 non-null  object
    #  3   장애인시설_경사로 여부      389999 non-null  object
    #  4   장애인시설_전용엘리베이터 여부  389999 non-null  object
    #  5   주차시설_자체 여부        389999 non-null  object
    #  6   주차시설_공영 여부        389999 non-null  object
    #  7   공연장코드             389999 non-null  object
    #  8   장애인석              389999 non-null  object
    #  9   무대시설_오케스트라피트 여부   389999 non-null  object
    #  10  공연코드              389999 non-null  object
    #  11  공연회차              389999 non-null  int64
    #  12  예매/취소구분           389999 non-null  int64
    #  13  할인금액              389999 non-null  int64
    #  14  할인종류코드            389999 non-null  int64
    #  15  장당금액              389999 non-null  int64
    #  16  성별                389999 non-null  int64
    #  17  연령                389999 non-null  int64
    #  18  소요시간              385262 non-null  object
    #  19  장르명               389999 non-null  object
    #  20  세부장르명             389999 non-null  object
    #  21  공연지역명             389999 non-null  object
    #  22  기획제작사명            387996 non-null  object
    #  23  관람연령              389994 non-null  object
    #  24  아동공연 여부           389999 non-null  object
    #  25  오픈런 여부            389999 non-null  object

    #  18  소요시간              385262 non-null  object
    #  22  기획제작사명            387996 non-null  object
    #  23  관람연령              389994 non-null  object

    # 결측값 존재 (소요시간, 기획제작사명, 관람연령)

    # 소요시간 => 결측값에 평균 소요시간 입력
    # 기획제작사명 => etc 넣기
    # 관람연령 => 평균 관람연령

    # print(df["소요시간"].value_counts(dropna=False))
    # 1. 소요시간
    sex = [1, 2]

    df["장당금액"] = df["장당금액"] - df["할인금액"]
    print("금액책정 완")

    for i in tqdm(range(len(df))):
        df["소요시간"][i] = str(df["소요시간"][i])
        if "시간" in df["소요시간"][i]:

            sp = df["소요시간"][i].split(" ")
            df["소요시간"][i] = 0
            df["소요시간"][i] += (int(float(sp[0][0:-2])) * 60)
            if len(sp) != 1: df["소요시간"][i] += int(float(sp[1][0:-1]))
        elif "분" in df["소요시간"][i]:
            df["소요시간"][i] = int(float(df["소요시간"][i][0:-1]))

        else:
            df["소요시간"][i] = np.NaN

        if "전체" in str(df["관람연령"][i]):
            df["관람연령"][i] = 0
        elif "개월" in str(df["관람연령"][i]):
            df["관람연령"][i] = int(int(re.sub(r'[^0-9]', '', str(df["관람연령"][i]))) / 12)
        elif re.sub(r'[^0-9]', '', str(df["관람연령"][i])) == '':
            df["관람연령"][i] = 0
        else:
            df["관람연령"][i] = int(re.sub(r'[^0-9]', '', str(df["관람연령"][i])))

        # 2020
        if df["성별"][i] == 0:
            df["성별"][i] = random.choices(sex, weights=[0.2, 0.8])[0]

    print("시간 변환 완")
    mean = df["소요시간"].mean()
    df["소요시간"] = df["소요시간"].fillna(mean)  # 결측값에는 평균을 넣는다.

    print("소요시간 결측 보정 완")

    # 2. 기획제작사명 =>결측값에는 etc를 넣어준다.
    df["기획제작사명"] = df["기획제작사명"].fillna("etc")
    print("기획제작사명 결측 보정 완")
    # 3. 관람 연령 => 가장 빈도수가 높은 만 7세 이상 (Figure.py)
    df["관람연령"] = df["관람연령"].fillna(7)

    ## 2020 1: 859942(남) 2: 3683698 합: 4543640 (0.2 vs 0.8)

    print("관람연령 결측 보정 완")

    # Y/N 데이터 바꾸기

    ox = {"Y": 0, "N": 1}

    df['편의시설_놀이방 여부'] = df['편의시설_놀이방 여부'].replace(ox)
    df['장애인시설_주차장 여부'] = df['장애인시설_주차장 여부'].replace(ox)
    df['장애인시설_화장실 여부'] = df['장애인시설_화장실'].replace(ox)
    df['장애인시설_경사로 여부'] = df['장애인시설_경사로 여부'].replace(ox)
    df['장애인시설_전용엘리베이터 여부'] = df['장애인시설_전용엘리베이터 여부'].replace(ox)
    df['주차시설_자체 여부'] = df['주차시설_자체 여부'].replace(ox)
    df['주차시설_공영 여부'] = df['주차시설_공영 여부'].replace(ox)
    df['무대시설_오케스트라피트 여부'] = df['무대시설_오케스트라피트 여부'].replace(ox)
    df['아동공연 여부'] = df['아동공연 여부'].replace(ox)
    df['오픈런 여부'] = df['오픈런 여부'].replace(ox)

    print("y/n 전처리 완")

    # 여러 항목 categorical data => sklearn을 통해 labeling

    # 1. 공연지역명

    list_region = preprocessing.LabelEncoder()
    list_region.fit(df["공연지역명"])  # 공연지역명 list 만들기

    df["공연지역명"] = list_region.transform(df["공연지역명"])  # 숫자 코드로 변환

    # 2. 장르명

    genre = preprocessing.LabelEncoder()
    genre.fit(df["장르명"])
    df["장르명"] = genre.transform(df["장르명"])

    # 3. 세부 장르명
    detail = preprocessing.LabelEncoder()
    detail.fit(df["세부장르명"])
    df["세부장르명"] = detail.transform(df["세부장르명"])

    # 각 labeling 정보 저장
    df2 = pd.DataFrame({
        '공연지역명': [''.join(s + " " for s in list(list_region.classes_))],
        '장르명': [''.join(s + " " for s in list(genre.classes_))],
        '세부장르명': [''.join(s + " " for s in list(detail.classes_))]
    })

    df2.to_sql("categorical_data_list_2020", con, if_exists="append", index=False)

    df.to_sql("kopis_ver3_2020", con, if_exists="append", index=False)

    df.info()