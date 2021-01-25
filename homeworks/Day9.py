import pandas as pd

#1
datas = pd.read_csv('boston.csv', 
                    usecols=['CHAS', 'NOX', 'RM'])
datas.to_excel('boston.xlsx', sheet_name = 'boston')