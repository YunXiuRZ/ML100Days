import pandas as pd

#topic
q_df = pd.DataFrame(
    [['male', 'teacher'], 
    ['male', 'engineer'], 
    ['female', None], 
    ['female', 'engineer']],
    columns=['Sex','Profession'])

#1
q_df = q_df.fillna('other')
print(q_df)

#2
q_df_sex = pd.get_dummies(q_df['Sex'])
q_df = pd.concat([q_df, q_df_sex], axis = 1)
q_df_profession = pd.get_dummies(q_df['Profession'])
q_df = pd.concat([q_df, q_df_profession], axis = 1)
print(q_df)