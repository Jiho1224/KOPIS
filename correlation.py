# -*- coding: utf-8 -*-
import sqlite3
import pandas as pd
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm
from matplotlib import rcParams
from scipy.stats import chi2_contingency
con = sqlite3.connect("C:/Users/user/Desktop/프로젝트/KOPIS/test_db.db")
pd.set_option('mode.chained_assignment',  None)

df = pd.read_sql("SELECT * FROM tmp3",con,index_col=None)
#
# re = df[['편의시설_놀이방','장애인시설_주차장','장애인시설_화장실','장애인시설_경사로','장애인시설_전용엘리베이터',
#          '주차시설_자체','주차시설_공영','공연장코드','장애인석','무대시설_오케스트라피트','공연코드',
#          '공연회차','예매_취소구분','할인금액','장당금액','성별','연령','소요시간','장르명','세부장르명',
#          '공연지역명','관람연령','아동공연','오픈런']].corr(method='kendall')




# print(re['공연코드'])

# font_lc = './Font/NanumFontSetup_TTF_GOTHIC/NanumGothic.ttf'
# font_name = fm.FontProperties(fname = font_lc).get_name()
rcParams['font.family'] = 'Malgun Gothic'
rcParams['axes.unicode_minus'] = False
# sns.heatmap(re,cmap='viridis')
# print(re['공연코드'])
#
# temp = dict(re['공연코드'])
# temp = sorted(temp.items(),key = lambda x:x[1],reverse=True)
# print(temp)
# plt.show()

# [('공연코드', 1.0), ('오픈런', 0.4512288039753247), ('장당금액', 0.1647698168189328), ('소요시간', 0.07342603794262804), ('예매_취소구분', 0.045013708023348), ('성별', 0.040128255875525085), ('관람연령', 0.013470611433475806), ('세부장르명', -0.019067331305604493), ('주차시설_공영', -0.033603141879029484), ('연령', -0.04153783535490032), ('공연지역명', -0.050499985769615195), ('장르명', -0.06311270992426037), ('아동공연', -0.1407947460388885), ('장애인시설_경사로', -0.14269247685036732), ('장애인시설_전용엘리베이터', -0.1537934285381658), ('편의시설_놀이방', -0.1810820790978807), ('공연회차', -0.18443280061066006), ('할인금액', -0.1856850023661343), ('장애인시설_주차장', -0.25537248835993964), ('장애인시설_화장실', -0.2604356221330388), ('무대시설_오케스트라피트', -0.26473631457155544), ('주차시설_자체', -0.2942031676739756)]

# categorical data의 상관계수를 분석해야하기 때문에 일반 상관계수 분석으로는 정확한 값이 도출되지 않을 것이라고 판단


#dython 사용 - 자동으로 어떤 기능이 범주형이고 어떤기능이 수치인지 찾고 각 기능과 모든 기능간의 관련 측정값을 계산
from dython.nominal import associations
from dython.nominal import identify_nominal_columns
categorical_features=identify_nominal_columns(df)

# 연속-연속 : pearson, 범주-연속 : 상관 비율, 범주-범주 : cramer V or Theil U
#associations(df, nominal_columns=categorical_features, numerical_columns=numerical_features, mark_columns=False, nom_nom_assoc='cramer', num_num_assoc='pearson')

associations(df, nominal_columns='auto', numerical_columns=None, mark_columns=False, nom_nom_assoc='cramer', num_num_assoc='pearson', ax=None, figsize=(15,15), annot=True, fmt='.2f', cmap=None, sv_color='silver', cbar=True, vmax=1.0, vmin=None, plot=True, compute_only=False, clustering=False, title=None, filename=None)
plt.savefig('cor.png')
