import numpy as np
import seaborn as sns

#1
#設定圖形樣式 - whitegrid
sns.set(style='whitegrid')

# 利用 NUMPY 去建立資料集
# np.random.RandomState 設定數學式
rs = np.random.RandomState()
x = rs.normal(2, 1, 75)
y = 2 + 1.5 * x + rs.normal(0, 2, 75)
'''
x = rs.normal(2, 1, 75)
y = 2 + 1.5 * x + rs.normal(0, 2, 75)
'''

# 畫圖
sns.residplot("x", "y", {"x":x, "y":y})

#2
sns.distplot(x, bins=10, kde=True)