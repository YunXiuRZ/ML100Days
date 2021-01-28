import pandas as pd

#topic
index = pd.date_range("1/1/2019", periods=20, freq='D')
series = pd.Series(range(20), index=index)

#1
series = series.to_period(freq='W')
print(series)
print("")

#2
print(series.mean())