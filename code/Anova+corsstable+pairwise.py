# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 17:02:44 2021

@author: Han jaewoong
"""

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline


# 파일열기
df = pd.read_csv("csv 파일", encoding='cp949')


# 원하는 column만 지정
df2=df[['단과대학','단과대학_2', '분야대학원학위요구']]


# 원하는 column에서의 분류 과정
x1 = np.array(df2[df2.단과대학_2 == 0].분야대학원학위요구)
x2 = np.array(df2[df2.단과대학_2 == 1].분야대학원학위요구)
x3 = np.array(df2[df2.단과대학_2 == 2].분야대학원학위요구)
x4 = np.array(df2[df2.단과대학_2 == 3].분야대학원학위요구)
x5 = np.array(df2[df2.단과대학_2 == 4].분야대학원학위요구)
x6 = np.array(df2[df2.단과대학_2 == 5].분야대학원학위요구)


# 등분산 검정
from scipy import stats
print(stats.bartlett(x1,x2,x3),stats.fligner(x1, x2, x3, x4, x5) ,stats.levene(x1, x2, x3, x4, x5), sep="\n")


# 단과대학별 분야대학원 학위요구
spp = df2.loc[:,['단과대학_2','분야대학원학위요구']]
spp.groupby("단과대학_2").count()
sp= np.array(spp)
group1 = sp[sp[: , 0]==0,1]
group2 = sp[sp[: , 0]==1,1]
group3 = sp[sp[: , 0]==2,1]
group4 = sp[sp[: , 0]==3,1]
group5 = sp[sp[: , 0]==4,1]
group6 = sp[sp[: , 0]==5,1]


# box plot을 통해 검토
plot_sp= [group1,group2, group3, group4, group5, group6]
ax = plt.boxplot(plot_sp, showmeans=True)
plt.show()


# 일원분산분석
F_statistic, pVal = stats.f_oneway(group1, group2, group3,group4, group5, group6)
print('데이터의 일원분산분석 결과 : F={0:.1f}, p={1:.10f}'.format(F_statistic, pVal))

# 각 집단에 대한 평균값
for a in plot_sp:
    print(a.mean())
    
# crosstable
contigency= pd.crosstab(df2['단과대학'], df2['분야대학원학위요구']) 
contigency_pct = pd.crosstab(df2['단과대학'], df2['분야대학원학위요구'], normalize='index')
c, p, dof, expected = chi2_contingency(contigency) 


# pairwise를 이용한 집단간의 분석
from statsmodels.stats.multicomp import pairwise_tukeyhsd

hsd = pairwise_tukeyhsd(df2['분야대학원학위요구'], df2['단과대학'], alpha=0.05)
hsd.summary()




