import pandas as pd

df = pd.read_csv('test.csv')
df['full_name'] = df.fname+" "+df.lname
df.to_csv('test_fullname.csv')


