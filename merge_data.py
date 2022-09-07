import pandas as pd
import os
import openpyxl
import sqlite3

df = pd.DataFrame() #모든 data file을 한 data로 합칠 data frame 생성

file_list = os.listdir('./data/2019') #모든 data file의 이름을 불러서 file_list에 저장
file_list1 = os.listdir('./data/2020')
file_list2 = os.listdir('./data/2021')
file_list3 = os.listdir('./data/2022')

num = 0

con = sqlite3.connect("C:/Users/user/Desktop/프로젝트/KOPIS/test_db.db")

for file_name in file_list:
    tmp = "./data/2019/"+file_name
    file_df = pd.read_excel(tmp)[['편의시설_놀이방 여부','장애인시설_주차장 여부','장애인시설_화장실 여부',
                                  '장애인시설_경사로 여부','장애인시설_전용엘리베이터 여부','주차시설_자체 여부',
                                  '주차시설_공영 여부','공연장코드','장애인석','무대시설_오케스트라피트 여부',
                                  '무대시설_무대넓이','공연코드','공연회차','예매/취소구분','할인금액','할인종류코드',
                                  '장당금액','성별','연령','소요시간','장르명','세부장르명','공연지역명','기획제작사명','관람연령',
                                  '아동공연 여부','오픈런 여부']]
    file_df.to_sql("kopis_raw_data_2019",con,if_exists="append",index=False)

for file_name in file_list1:
    tmp = "./data/2020/"+file_name
    file_df = pd.read_excel(tmp)[['편의시설_놀이방 여부','장애인시설_주차장 여부','장애인시설_화장실 여부',
                                  '장애인시설_경사로 여부','장애인시설_전용엘리베이터 여부','주차시설_자체 여부',
                                  '주차시설_공영 여부','공연장코드','장애인석','무대시설_오케스트라피트 여부',
                                  '무대시설_무대넓이','공연코드','공연회차','예매/취소구분','할인금액','할인종류코드',
                                  '장당금액','성별','연령','소요시간','장르명','세부장르명','공연지역명','기획제작사명','관람연령',
                                  '아동공연 여부','오픈런 여부']]
    file_df.to_sql("kopis_raw_data_2020",con,if_exists="append",index=False)

for file_name in file_list2:
    tmp = "./data/2021/"+file_name
    file_df = pd.read_excel(tmp)[['편의시설_놀이방 여부','장애인시설_주차장 여부','장애인시설_화장실 여부',
                                  '장애인시설_경사로 여부','장애인시설_전용엘리베이터 여부','주차시설_자체 여부',
                                  '주차시설_공영 여부','공연장코드','장애인석','무대시설_오케스트라피트 여부',
                                  '무대시설_무대넓이','공연코드','공연회차','예매/취소구분','할인금액','할인종류코드',
                                  '장당금액','성별','연령','소요시간','장르명','세부장르명','공연지역명','기획제작사명','관람연령',
                                  '아동공연 여부','오픈런 여부']]
    file_df.to_sql("kopis_raw_data_2021",con,if_exists="append",index=False)

for file_name in file_list3:
    tmp = "./data/2022/"+file_name
    file_df = pd.read_excel(tmp)[['편의시설_놀이방 여부','장애인시설_주차장 여부','장애인시설_화장실 여부',
                                  '장애인시설_경사로 여부','장애인시설_전용엘리베이터 여부','주차시설_자체 여부',
                                  '주차시설_공영 여부','공연장코드','장애인석','무대시설_오케스트라피트 여부',
                                  '무대시설_무대넓이','공연코드','공연회차','예매/취소구분','할인금액','할인종류코드',
                                  '장당금액','성별','연령','소요시간','장르명','세부장르명','공연지역명','기획제작사명','관람연령',
                                  '아동공연 여부','오픈런 여부']]
    file_df.to_sql("kopis_raw_data_2022",con,if_exists="append",index=False)

