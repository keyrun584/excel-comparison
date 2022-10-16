
import pandas as pd

s1=pd.read_excel('s1.xlsx')
s2=pd.read_excel('s2.xlsx')
exist=0
comparison_values = s1.values == s2.values
comparison_values.tolist()
for i in range(0,len(comparison_values)):
    exist=0
    for j in range(0,len(comparison_values)-1):
        if comparison_values[i][j]==True:
            exist=exist+1
    if j==exist-1:
        print("Exist")
    else:
        print("non_exist")
