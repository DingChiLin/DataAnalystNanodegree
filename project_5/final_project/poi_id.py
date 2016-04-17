#!/usr/bin/pytadd_feature_by_scalar_and_pcahon

import sys
import pickle

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data
from helper import *

### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
#features_list = ['poi','salary','to_messages','deferral_payments','total_payments',\
                 #'exercised_stock_options','bonus','restricted_stock','shared_receipt_with_poi',\
                 #'restricted_stock_deferred','total_stock_value','expenses','loan_advances',\
                 #'from_messages','other','from_this_person_to_poi','director_fees',\
                 #'deferred_income','long_term_incentive','from_poi_to_this_person']


### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### Task 1: Remove outliers : only 122 records remain after doing this

# remove TOTAL : 1
del data_dict['TOTAL']

financial_values = data_dict.values()
names = data_dict.keys()
remove_name_list = []
for idx, financial_value in enumerate(financial_values):
    values = financial_value.values()
    nan_count = 0
    for value in values:
        if(value == 'NaN'):
            nan_count += 1

    if(nan_count >= 18 and not financial_value['poi']):
        remove_name_list.append(names[idx])

#print(len(remove_name_list))
# remove data with too many 'NaN's : 5
for name in remove_name_list:
    del data_dict[name]

### Task 2: Create new feature(s) : Scaler all data and create two new features by PCA
from sklearn.preprocessing import StandardScaler

#Transform by scaler
scaler_data_dict = transform_by_scaler(data_dict, StandardScaler())

#Add New Feature by PCA
scaler_pca_feature_data_dict = add_feature_by_pca(scaler_data_dict)

### Store to my_dataset for easy export below.
my_dataset = scaler_pca_feature_data_dict


### Task 3: Select my feature: Using selectKBest to find the three best features
from sklearn.feature_selection import SelectKBest, f_classif

all_labels, all_features, all_features_list = get_features(my_dataset)

sel = SelectKBest(f_classif, k=3)
sel.fit(all_features, all_labels)
feature_scores = sorted(zip(sel.scores_, all_features_list), key= lambda x:x[0])[-4:]
print(feature_scores)

#Find The Three Best Component: exercised_stock_options, total_stock_value, pca_component1
features_list = ['poi'] + map(lambda x:x[1], feature_scores)
#print(features_list)

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)
#print(len(labels))

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import precision_score, recall_score, make_scorer

def score_function(y_true, y_pred):
    return (2*recall_score(y_true, y_pred) + 1*precision_score(y_true, y_pred))/4

scorer = make_scorer(score_function)

from sklearn.naive_bayes import GaussianNB
param_grid1 = {} # GaussianNB have no parameter
clf1 = GridSearchCV(GaussianNB(), param_grid1, scoring=scorer)

from sklearn.svm import SVC
param_grid2 = {
          'kernel' : ['rbf', 'poly'],
          'C': [1, 10, 1e2, 5e2, 1e3, 5e3, 1e4, 5e4, 1e5],
          'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1],
          'class_weight': [{True: 6, False: 1}, {True: 7, False: 1}, {True: 8, False: 1}, \
                           {True: 9, False: 1}, {True: 10, False: 1}]
          }

clf2 = GridSearchCV(SVC(random_state=42), param_grid2, scoring=scorer)

from sklearn.ensemble import RandomForestClassifier
param_grid3 = {
          'min_samples_split' : [2,5,8,10],
          'max_depth': [1,2,3,None],
          'class_weight': [{True: 6, False: 1}, {True: 7, False: 1}, {True: 8, False: 1}, \
                           {True: 9, False: 1}, {True: 10, False: 1}]
          }

clf3 = GridSearchCV(RandomForestClassifier(random_state=42), param_grid3, scoring=scorer)

from sklearn.ensemble import AdaBoostClassifier
param_grid4 = {
          'n_estimators' : [10, 30, 50, 70, 100],
          'learning_rate': [0.01, 0.05, 0.1, 0.5, 1],
          }

clf4 = GridSearchCV(AdaBoostClassifier(random_state=42), param_grid4, scoring=scorer)


from sklearn.linear_model import LogisticRegression
param_grid5 = {
        'max_iter': [100,200,300],
        'C': [1, 10, 1e2, 5e2, 1e3, 5e3, 1e4, 5e4, 1e5],
        'tol': [1, 1e-1, 1e-4, 1e-16],
        'class_weight': [{True: 6, False: 1}, {True: 7, False: 1}, {True: 8, False: 1}, \
                           {True: 9, False: 1}, {True: 10, False: 1}]
        }

clf5 = GridSearchCV(LogisticRegression(random_state=42), param_grid5, scoring=scorer)


### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

final_clf = None
highest_precesion = 0
highest_recall = 0

from sklearn import cross_validation
for clf in [clf1, clf2, clf3, clf4, clf5]:

    clf.fit(features_train, labels_train)
    score = clf.best_estimator_.score(features_test, labels_test)
    labels_pred = clf.best_estimator_.predict(features_test)

    ######################
    #            Pred    #
    #           0    1   #
    #        0  TN   FP  #
    # ACTUAL             #
    #        1  FN   TP  #
    ######################
    print(confusion_matrix(labels_test, labels_pred))

    ###########################
    # Recall     = TP/(TP+FN) #
    # Precession = TP/(TP+FP) #
    ###########################

    #target_names = ['non-poi(0)', 'poi(1)']
    #print(classification_report(labels_test, labels_pred, target_names=target_names))

    p_score = precision_score(labels_test, labels_pred)
    r_score = recall_score(labels_test, labels_pred)

    print('Algorithm:', type(clf.best_estimator_).__name__)
    print('Best Parameters: ', clf.best_params_)
    print('Recall: ', r_score)
    print('Precision: ', p_score)

    if p_score > 0.2:
        if r_score > highest_recall:
            highest_recall = r_score
            highest_precesion = p_score
            final_clf = clf.best_estimator_
        elif r_score == highest_recall:
            if p_score > highest_precesion:
                highest_precesion = p_score
                final_clf = clf.best_estimator_

    print('---------------------')

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

#final_clf = RandomForestClassifier(min_samples_split = 2, max_depth = 1, class_weight = {False: 1, True: 9})
dump_classifier_and_data(final_clf, my_dataset, features_list)

