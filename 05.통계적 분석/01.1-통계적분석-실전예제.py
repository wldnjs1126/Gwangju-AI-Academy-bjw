import pandas as pd
import numpy as np

df_emp = pd.read_csv("C:\Gwangju-AI-Academy-bjw\emp.csv")

df_emp.info()
print(df_emp.describe())
print(df_emp.head())



# 플로리다 일평균 기온이다.
# 일평균 기온이 25도씨 라고 할수 있는지 검정해 보시오.
data = [35, 40, 12, 15, 21, 14, 46, 10, 28, 48, 16, 30, 32, 48, 31, 22, 12, 39, 19, 25]
mean = 25

import scipy.stats as stats

# 데이터가 정규성을 만족하는지 조사
shapiro_test = stats.shapiro(data)
print(shapiro_test)