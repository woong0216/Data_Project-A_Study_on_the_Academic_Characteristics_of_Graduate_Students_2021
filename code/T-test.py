# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 17:11:37 2021

@author: Han jaewoong
"""

import numpy as np
import pandas as pd
from scipy import stats
import researchpy as rp
df = pd.read_csv("csv 파일", encoding='cp949')


# 데이터 집단 나누기
yes = df.query('석사진학계획 == 1')['현재학년']
no = df.query('석사진학계획  == 0')['현재학년']


# t-test 검정
stats.ttest_ind(yes, no, equal_var=True) 


# 정규성 검정
from scipy.stats import shapiro
data = df['취업_기술직']
shapiro(data)


# 여러 변수 정규성 검정
for a in df[:]:
    data= df[a]
    print(a)
    print(shapiro(data))
    
    