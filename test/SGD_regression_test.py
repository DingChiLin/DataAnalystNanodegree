import numpy as np
import pandas
from sklearn.linear_model import SGDRegressor
import random

"""
In this question, you need to:
1) Implement the linear_regression() procedure using gradient descent.
   You can use the SGDRegressor class from sklearn, since this class uses gradient descent.
2) Select features (in the predictions procedure) and make predictions.

"""

def normalize_features(features):
    ''' 
    Returns the means and standard deviations of the given features, along with a normalized feature
    matrix.
    ''' 
    means = np.mean(features, axis=0)
    std_devs = np.std(features, axis=0)
    normalized_features = (features - means) / std_devs
    return means, std_devs, normalized_features

def recover_params(means, std_devs, norm_intercept, norm_params):
    ''' 
    Recovers the weights for a linear model given parameters that were fitted using
    normalized features. Takes the means and standard deviations of the original
    features, along with the intercept and parameters computed using the normalized
    features, and returns the intercept and parameters that correspond to the original
    features.
    ''' 
    intercept = norm_intercept - np.sum(means * norm_params / std_devs)
    params = norm_params / std_devs
    return intercept, params

def linear_regression(features, values):
    """
    Perform linear regression given a data set with an arbitrary number of features.
    """
    clf = SGDRegressor(n_iter=100)
    clf.fit(features,values)
    print(clf.score(features,values))
    intercept = clf.intercept_ 
    params = clf.coef_
    
    return intercept, params

def predictions(dataframe):
    '''
    The NYC turnstile data is stored in a pandas dataframe called weather_turnstile.
    Using the information stored in the dataframe, let's predict the ridership of
    the NYC subway using linear regression with gradient descent.
    
    You can download the complete turnstile weather dataframe here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv    
    
    Your prediction should have a R^2 value of 0.40 or better.
    You need to experiment using various input features contained in the dataframe. 
    We recommend that you don't use the EXITSn_hourly feature as an input to the 
    linear model because we cannot use it as a predictor: we cannot use exits 
    counts as a way to predict entry counts. 
    
    Note: Due to the memory and CPU limitation of our Amazon EC2 instance, we will
    give you a random subset (~50%) of the data contained in 
    turnstile_data_master_with_weather.csv. You are encouraged to experiment with 
    this exercise on your own computer, locally.
    
    If you receive a "server has encountered an error" message, that means you are 
    hitting the 30-second limit that's placed on running your program. Try using a
    smaller number of features or fewer iterations.
    '''
    ################################ MODIFY THIS SECTION #####################################
    # Select features. You should modify this section to try different features!             #
    # We've selected rain, precipi, Hour, meantempi, and UNIT (as a dummy) to start you off. #
    # See this page for more info about dummy variables:                                     #
    # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.get_dummies.html          #
    ##########################################################################################

    # Add improved useful data
    dataframe['day_week'] = pandas.to_datetime(dataframe['DATEn']).dt.weekday

    features = dataframe[['rain', 'precipi', 'meantempi', 'hour', 'day_week']]
    dummy_units = pandas.get_dummies(dataframe['UNIT'], prefix='unit')
    features = features.join(dummy_units)

    # Values
    values = dataframe['ENTRIESn_hourly']

    # Get numpy arrays
    features_array = features.values
    values_array = values.values
    means, std_devs, normalized_features_array = normalize_features(features_array)

    # Perform gradient descent
    norm_intercept, norm_params = linear_regression(normalized_features_array, values_array)

    intercept, params = recover_params(means, std_devs, norm_intercept, norm_params)
    predictions = intercept + np.dot(features_array, params)
    # The following line would be equivalent:
    # predictions = norm_intercept + np.dot(normalized_features_array, norm_params)

    print(getRsquare(predictions, values))

    return intercept, params, predictions

def predictions_by_test(dataframe):

    dataframe['day_week'] = pandas.to_datetime(dataframe['DATEn']).dt.weekday

    #Separate Data
    rows = random.sample( list(dataframe.index), round(len(dataframe.index)/10) )
    df_test = dataframe.ix[rows]
    df_train = dataframe.drop(rows)

    #Choose features
    features_test = df_test[['rain', 'precipi', 'meantempi', 'hour', 'day_week']]
    dummy_units = pandas.get_dummies(df_test['UNIT'], prefix='unit')
    features_test = features_test.join(dummy_units)

    features_train = df_train[['rain', 'precipi', 'meantempi', 'hour', 'day_week']]
    dummy_units = pandas.get_dummies(df_train['UNIT'], prefix='unit')
    features_train = features_train.join(dummy_units)

    # Values
    values_test = df_test['ENTRIESn_hourly']
    values_train = df_train['ENTRIESn_hourly']

    # Get numpy arrays
    features_array = features_train.values
    values_array = values_train.values
    means, std_devs, normalized_features_array = normalize_features(features_array)

    # Perform gradient descent
    norm_intercept, norm_params = linear_regression(normalized_features_array, values_array)
    intercept, params = recover_params(means, std_devs, norm_intercept, norm_params)

    predictions = intercept + np.dot(features_test.values, params)
    print(getRsquare(predictions, values_test))


def getRsquare(predictions, data):

    numerator = 0
    denominator = 0
    data_mean = data.mean()

    print(data_mean)

    for idx, val in enumerate(data):
        numerator += np.square(val - predictions[idx])
        denominator += np.square(val - data_mean)

    r_squared = 1 - numerator/denominator
    return r_squared



