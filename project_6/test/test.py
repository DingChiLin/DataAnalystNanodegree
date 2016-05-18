import pandas as pd
import numpy as np

df1 = pd.DataFrame([[0,1],[2,3],[4,5]])
df1.columns = ['Col', None]
print(df1)

df2 = pd.DataFrame([[0,7],[2,8],[4,9]])
df2.columns = ['Col', None]
print(df2)

df1['D'] = df2
print(df1)

