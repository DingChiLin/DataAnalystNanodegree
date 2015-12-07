import pandas

f_in = open('test_dummy.csv','r')
df = pandas.read_csv(f_in, delimiter=",")
print df

dummy_units = pandas.get_dummies(df['c'], prefix='unit')
print dummy_units

features = df[['a','b']]
features = features.join(dummy_units)
print features
