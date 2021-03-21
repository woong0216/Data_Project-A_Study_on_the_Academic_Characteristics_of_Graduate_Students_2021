# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 17:09:10 2021

@author: Han jaewoong
"""

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

# 파일 열기
df = pd.read_csv("csv 파일", encoding='cp949')


# 전처리
df2=df[['석사진학계획','RA프로젝트참여여부']]
contigency= pd.crosstab(df2['석사진학계획'], df2['RA프로젝트참여여부']) 
contigency

contigency_pct = pd.crosstab(df2['석사진학계획'], df2['RA프로젝트참여여부'], normalize='index')
contigency_pct

c, p, dof, expected = chi2_contingency(contigency) 
print(p)
