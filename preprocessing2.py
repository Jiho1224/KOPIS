import sqlite3
import pandas as pd
import numpy as np
from tqdm import tqdm
from sklearn import preprocessing

con = sqlite3.connect("C:/Users/user/Desktop/프로젝트/KOPIS/test_db.db")
pd.set_option('mode.chained_assignment',  None) #SettingWithCopyWarning 끄기

df = pd.read_sql("SELECT * FROM temp_data",con,index_col=None)
df.info()
print("저장완료")
# df["기획제작사명"].fillna("etc")
# df.to_sql("kopis_ver3_2019",con,if_exists = "replace",index=False)
#
# df = pd.read_sql("SELECT * FROM kopis_ver3_2020",con,index_col=None)
# df["기획제작사명"].fillna("etc")
# df.to_sql("kopis_ver3_2020",con,if_exists = "replace",index=False)
#
# df = pd.read_sql("SELECT * FROM kopis_ver3_2021",con,index_col=None)
# df["기획제작사명"].fillna("etc")
# df.to_sql("kopis_ver3_2021",con,if_exists = "replace",index=False)
#
# df = pd.read_sql("SELECT * FROM kopis_ver3_2022",con,index_col=None)
# df["기획제작사명"].fillna("etc")
# df.to_sql("kopis_ver3_2022",con,if_exists = "replace",index=False)

df["장당금액"] = df["장당금액"] - df["할인금액"]

code = preprocessing.LabelEncoder()
code.fit(df["공연코드"])
df["공연코드"] = code.transform(df["공연코드"])

df.to_sql("temp_data_ver2", con, if_exists="replace", index=False)
