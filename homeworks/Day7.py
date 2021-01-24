import numpy as np

#topic
array1 = np.array([[10, 8], [3, 5]])

#1
inserve = np.linalg.inv(array1)
print("inserve:")
print(inserve)
print("multiply:")
print(inserve @ array1)
print("")

#2
value, vector = np.linalg.eig(array1)
print("eigvalue:")
print(value)
print("eigvector:")
print(vector)
print("")

#3
u, s, vh = np.linalg.svd(array1)
print(u)
print(s)
print(vh)