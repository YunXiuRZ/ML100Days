import numpy as np

#topic
english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,55,60])
chinese_score = np.array([65,90,82,72,66,77])

#1
result = 0
for i in range(0, 6):
    if(english_score[i] > math_score[i]):
        result+=1
print(result)

#2
flag = True
for i in range(0, 6):
    if(english_score[i] > chinese_score[i] | 
       math_score[i] > chinese_score[i]):
        flag = False
        break
print(flag)