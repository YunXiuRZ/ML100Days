import pandas as pd

#1
datas = pd.read_csv('STOCK_DAY_0050_202009.csv')
append_datas = pd.read_csv('STOCK_DAY_0050_202010.csv')
datas = datas.append(append_datas)
results = datas[datas.open < datas.close]
results.to_csv('STOCK_DAY_RESULT.csv')