import pandas as pd

#topic
score_df = pd.DataFrame([[1,56,66,70], 
                         [2,90,45,34], 
                         [3,45,32,55], 
                         [4,70,77,89], 
                         [5,56,80,70], 
                         [6,60,54,55], 
                         [7,45,70,79], 
                         [8,34,77,76], 
                         [9,25,87,60], 
                         [10,88,40,43]],
                        columns=['student_id',
                                 'math_score',
                                 'english_score',
                                 'chinese_score'])

#a
score_df = score_df.set_index('student_id')
score_avarage = score_df.mean(axis = 1)
print("id6 avarage:%3.1f" % score_avarage[6])

#b
print("avarage median:%3.1f" % score_avarage.median())

#c
score_df = score_df.apply(lambda x : x**(0.5)*10)
print(score_df)


#d
subject_avarage = score_df.mean()
print("class avarage:")
print(subject_avarage)