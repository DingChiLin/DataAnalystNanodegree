import pandas as pd

filename = '../data/pisa2012.csv'

f_in = open(filename,'r')
df = pd.read_csv(f_in, delimiter=",")
clean_data = df[['CNT','LMINS','MMINS','SMINS','ST69Q01','ST69Q02','ST69Q03','ICTRES','W_FSTUWT']]
clean_data.rename(
  columns={'CNT': 'Country',
           'LMINS': 'LanguageLearningTime', # response time in each class * class number
           'MMINS': 'MathLearningTime',
           'SMINS': 'ScienceLearningTime',
           'ST69Q01': 'LanguageClassTime',
           'ST69Q02': 'MathClassTime',
           'ST69Q03': 'ScienceClassTime',
           'ICTRES': 'ICTResources',
           'W_FSTUWT': 'Weight'},
  inplace=True)

clean_data['LanguageScore'] = (df['PV1READ'] + df['PV2READ'] + df['PV3READ'] + df['PV4READ'] + df['PV5READ'])/5
clean_data['MathScore'] = (df['PV1MATH'] + df['PV2MATH'] + df['PV3MATH'] + df['PV4MATH'] + df['PV5MATH'])/5
clean_data['ScienceScore'] = (df['PV1SCIE'] + df['PV2SCIE'] + df['PV3SCIE'] + df['PV4SCIE'] + df['PV5SCIE'])/5

clean_data=clean_data.dropna()

print(clean_data)
clean_data.to_csv('../data/pisa2012_clean.csv', sep=',', index_label='index')
