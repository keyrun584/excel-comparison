import pandas as pd
import numpy as np

s1=pd.read_excel('s1.xlsx')
s2=pd.read_excel('s2.xlsx')

s1.equals(s2)

comparison_values = s1.values == s2.values


rows,cols=np.where(comparison_values==False)

for item in zip(rows,cols):
    s1.iloc[item[0], item[1]] = '{} --> {}'.format(s1.iloc[item[0], 
    item[1]],s2.iloc[item[0], item[1]])
    if np.where(comparison_values=="False"):
        print("Exist")
        break
    else :
        print("non_exist")
        break