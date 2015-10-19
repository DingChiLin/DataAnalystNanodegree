import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import SGD_regression_test as SGD

path = r'~/Documents/GitHub/DataAnalystNanodegree/test/improved-dataset/turnstile_weather_v2.csv'
#path = r'~/Documents/GitHub/DataAnalystNanodegree/turnstile_data_master_with_weather.csv'

turnstile_weather = pd.read_csv(path)
#enter_rain = turnstile_weather[turnstile_weather.rain == 1]['ENTRIESn_hourly']
#enter_not_rain = turnstile_weather[turnstile_weather.rain == 0]['ENTRIESn_hourly']

#w1,p1 = scipy.stats.shapiro(enter_rain)
#w2,p2 = scipy.stats.shapiro(enter_not_rain)

#enter_rain_mean = enter_rain.mean()
#enter_not_rain_mean = enter_not_rain.mean()
#U ,p = scipy.stats.mannwhitneyu(enter_rain, enter_not_rain,  use_continuity=True)

#print(enter_rain_mean)
#print(enter_not_rain_mean)
#print(p)

inter, param, prediction = SGD.predictions(turnstile_weather)
#SGD.predictions_by_test(turnstile_weather)
print(param)


