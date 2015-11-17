import pandas as pd
import numpy as np

array1 = [1,3,5,7,9]
array2 = [2,4,2,8,10]
index = [1,2,3,4,5]

d = {'y' : pd.Series(array1, index=index),
     'x1' : pd.Series(array2, index=index)}
df = pd.DataFrame(d)
print(df)

df['x2'] = [2,3,5,7,9]
print(df)

df['x3'] = df['x1'] * 5
print(df)

def multiply(x):
    return x*x

df['x4'] = df['x1'].apply(multiply)
print(df)


df['x5'] = np.log(df['x1']+1)
print(df)



