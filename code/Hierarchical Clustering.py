# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 17:14:16 2021

@author: Han jaewoong
"""

import pandas as pd
df=pd.read_excel('엑셀 파일')


# 정규화
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
df[:]=scaler.fit_transform(df[:])


# ward clustering 시각화
data = df.iloc[:, 3:24].values

import scipy.cluster.hierarchy as shc
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 7))
plt.title("Dendograms")
clustering = shc.dendrogram(shc.linkage(data, method='ward'))

# 클러스터링 결과에 따른 분류
from sklearn.cluster import AgglomerativeClustering
cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
cluster_data=cluster.fit_predict(data)

df['clustering']=cluster_data