import numpy as np

#topic
array1 = np.array(range(30))

#1
array1.resize((5, 6))

arg_array = np.where(array1 % 6 == 1)
print(arg_array)