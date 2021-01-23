import numpy as np


def calculate(List):
    scores = np.array(List)
    print("avarage:%3.1f" % np.nanmean(scores))
    print("maximum:%3.1f" % np.nanmax(scores))
    print("minimum:%3.1f" % np.nanmin(scores))
    print("standard diviation:%3.1f" % np.nanstd(scores))
    print("")

#topic
english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,np.nan,60])
chinese_score = np.array([65,90,82,72,66,77])

#1
print("english scores data:")
calculate(english_score)
print("")
print("math scores data:")
calculate(math_score)
print("")
print("chinese scores data:")
calculate(chinese_score)
print("")

#2
math_score[4] = 55
print("math scores after makeup")
calculate(math_score)
print("")

#3
print("correlation coefficient of english and chinese:")
print(np.corrcoef(english_score, chinese_score))
print("")
print("correlation coefficient of math and chinese:")
print(np.corrcoef(math_score, chinese_score))