import numpy as np

#1
v = 20000
result = 20 * np.log10(v/20)
print(result)

#2
v30 = np.power(10, 1.5) * 20
v50 = np.power(10, 2.5) * 20
print(v30/v50)