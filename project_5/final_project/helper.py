from feature_format import featureFormat, targetFeatureSplit
import numpy

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


def add_feature_by_pca(data_dict):

    _, all_features, all_features_list = get_features(data_dict)

    from sklearn.decomposition import RandomizedPCA
    n_components = 2
    pca = RandomizedPCA(n_components=n_components, whiten=True)
    pca_features = pca.fit_transform(all_features)

    keys = ['poi']+all_features_list
    values = all_features

    keys = data_dict.keys()
    new_dict = {}
    print(pca.explained_variance_ratio_)

    for idx, key in enumerate(keys):
        new_dict[key] = dict(data_dict[key])

        new_dict[key]['pca_component1'] = round(pca_features[idx][0],4 )
        new_dict[key]['pca_component2'] = round(pca_features[idx][1],4 )

    return new_dict

