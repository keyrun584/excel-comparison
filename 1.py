import pandas as pd
import numpy as np

s1=pd.read_excel('s1.xlsx')
s2=pd.read_excel('s2.xlsx')

s1.equals(s2)
exist=0
non_exist=0
comparison_values = s1.values == s2.values
comparison_values.tolist()
for i in range(0,len(comparison_values)):
    for j in range(0,len(comparison_values)-1):
        if comparison_values[i][j]==False:
            exist=exist+1
if exist>0:
    print("exist")
else:
    print("NOn_Exist")
