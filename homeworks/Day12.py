import pandas as pd

#topic
datas = pd.read_csv('boston.csv')

#1
datas.boxplot()

#2
datas.plot.scatter(x = 'NOX', y = 'DIS')