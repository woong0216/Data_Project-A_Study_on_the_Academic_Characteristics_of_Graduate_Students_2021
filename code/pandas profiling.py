# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 17:10:39 2021

@author: Han jaewoong
"""

# pip install -U pandas-profiling

import pandas as pd
import pandas_profiling
data = pd.read_excel("xlsx 파일")

pr=data.profile_report() # 프로파일링 결과 리포트를 pr에 저장
data.profile_report() # 바로 결과 보기