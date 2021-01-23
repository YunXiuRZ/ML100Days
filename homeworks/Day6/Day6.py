import numpy as np

#topic
array1 = np.array(range(30))
array2 = np.array([2,3,5])

array3 = np.array([[4,5,6],[1,2,3]])

#1
with open('homework_output1.npz', 'wb') as f:
    np.savez(f, array1, array2)

#2
array4 = np.load('homework_output1.npz')
with open('homework_output2.npz', 'wb') as f:
    np.savez(f, array4, array3)
