# 엑셀 다루기

import pandas as pd

data = {
    "이름": ["홍길동", "김영희", "이철수"],
    "나이": [30, 25, 28],
    "직업": ["개발자", "디자이너", "기획자"]
}

df = pd.DataFrame(data)

df

df.to_excel('데이터.xlsx', index=False)

# 엑셀 파일 읽기
df_excel = pd.read_excel('데이터.xlsx')

df_excel.info()

print(df_excel.head())

# 데이터 베이스_판다스 연동
import pymysql
import pandas as pd
import numpy as np

conn = pymysql.connect(
    host="localhost",
    user="scott",
    password="tiger",
    database="scott",charset="utf8")

sql = "select * from emp"
df_emp = pd.read_sql(sql, conn)
print(df_emp)

df_emp.to_csv("emp.csv")
df_emp.to_excel("emp.xlsx")