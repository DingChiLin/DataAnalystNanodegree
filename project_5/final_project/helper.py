from feature_format import featureFormat, targetFeatureSplit
import numpy
from math import log

def get_features(data_dict):
    all_features_list = data_dict.values()[0].keys()
    all_features_list.remove('poi') #poi will be label, not feature
    all_features_list.remove('email_address') #email is not a numerical feature

    all_data = featureFormat(data_dict, ['poi']+all_features_list, remove_all_zeroes=False)
    all_labels, all_features = targetFeatureSplit(all_data)

    return all_labels, all_features, all_features_list


def transform_by_scaler(data_dict, scaler):

    _, all_features, all_features_list = get_features(data_dict)
    scaler_features = scaler.fit_transform(all_features)

    keys = data_dict.keys()
    transformed_dict = {}

    for idx, key in enumerate(keys):
        transformed_dict[key] = {}
        transformed_dict[key]['poi'] = data_dict[key]['poi']
        transformed_dict[key]['email_address'] = data_dict[key]['email_address']

        for f_idx, feature in enumerate(all_features_list):
            transformed_dict[key][feature] = round(scaler_features[idx][f_idx], 4)

    return transformed_dict

def remove_nan(number):
    return 0 if number == 'NaN' else float(number)

def add_customer_features(data_dict):
    _, all_features, all_features_list = get_features(data_dict)
    keys = data_dict.keys()
    new_dict = {}
    for idx, key in enumerate(keys):
        new_dict[key] = dict(data_dict[key])

        new_dict[key]['financial_info'] = \
               (remove_nan(data_dict[key]['salary']) + \
                remove_nan(data_dict[key]['deferral_payments']) + \
                remove_nan(data_dict[key]['total_payments']) + \
                remove_nan(data_dict[key]['exercised_stock_options']) + \
                remove_nan(data_dict[key]['bonus']) + \
                remove_nan(data_dict[key]['restricted_stock']) + \
                remove_nan(data_dict[key]['restricted_stock_deferred']) + \
                remove_nan(data_dict[key]['total_stock_value']) + \
                remove_nan(data_dict[key]['expenses']) + \
                remove_nan(data_dict[key]['loan_advances']) + \
                remove_nan(data_dict[key]['other']) + \
                remove_nan(data_dict[key]['director_fees']) + \
                remove_nan(data_dict[key]['deferred_income']) + \
                remove_nan(data_dict[key]['long_term_incentive']))

        new_dict[key]['communicating_info'] = \
               (remove_nan(data_dict[key]['shared_receipt_with_poi']) + \
                remove_nan(data_dict[key]['to_messages']) + \
                remove_nan(data_dict[key]['from_messages']) + \
                remove_nan(data_dict[key]['from_this_person_to_poi']) + \
                remove_nan(data_dict[key]['from_poi_to_this_person']))

        new_dict[key]['log_financial_info'] = log(new_dict[key]['financial_info']+1)
        new_dict[key]['log_communicating_info'] = log(new_dict[key]['communicating_info']+1)

    return new_dict

