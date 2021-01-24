import numpy as np

#topic
name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank_list = [8,1,5,4,7,6,2,3]
myopia_list = [True,True,False,False,True,True,False,False]

#1
datatype = np.dtype({'names':('name', 'sex', 'weight', 'rank', 'myopia',),
                     'formats':('U5', 'U5', 'f', 'i', '?')})
array = np.zeros(8, dtype = datatype)
array['name'] = name_list
array['sex'] = sex_list
array['weight'] = weight_list
array['rank'] = rank_list
array['myopia'] = myopia_list
print(array)
print("")

#2
print("weight_avarage:%3.1f" % np.mean(array['weight']))
print("")

#3
print("weight avarage of boys:%3.1f" % np.mean(array[array['sex'] == 'boy']['weight']))
print("weight avarage 0f girls:%3.1f" % np.mean(array[array['sex'] == 'girl']['weight']))