#!/usr/bin/pytadd_feature_by_scalar_and_pcahon

import sys
import pickle
from pprint import pprint

from feature_format import featureFormat, targetFeatureSplit
from tester import test_classifier, dump_classifier_and_data
from sklearn.preprocessing import StandardScaler, MinMaxScaler
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

print(len(remove_name_list))
# remove data with too many 'NaN's : 5
for name in remove_name_list:
    del data_dict[name]

### Task 2: Create new feature(s) : Scaler all data and create two new features by PCA
my_dataset = add_customer_features(data_dict)

### Task 3: Select my feature: Using selectKBest to find the three best features
from sklearn.feature_selection import SelectKBest, f_classif

all_labels, all_features, all_features_list = get_features(my_dataset)

features_list = ['poi'] + all_features_list #['poi'] + map(lambda x:x[1], feature_scores)

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
from sklearn.cross_validation import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA

def score_function(y_true, y_pred):
    return (8*recall_score(y_true, y_pred) + 1*precision_score(y_true, y_pred))/9.0

scorer = make_scorer(score_function)
scaler = StandardScaler()
k_fold = StratifiedShuffleSplit(labels, n_iter=10, test_size=0.3)


#GaussianNB
from sklearn.naive_bayes import GaussianNB

param_grid1 = {} # GaussianNB have no parameter

pipeline1 = Pipeline(steps=[('minmaxer', scaler),
                            ('selection', SelectKBest(score_func=f_classif)),
                            ('reducer', PCA()),
                            ('classifier', GaussianNB())])

clf1 = GridSearchCV(pipeline1, param_grid=param_grid1, cv=k_fold, scoring=scorer)

#SVC
from sklearn.svm import SVC

param_grid2 = {
          'reducer__n_components': [0.2, 0.5, 0.7, 2, 3, 4],
          'selection__k': [5,6,7,'all'],
          'classifier__C': [1, 10, 1e2, 5e2, 1e3, 5e3, 1e4, 5e4, 1e5],
          'classifier__gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1],
          'classifier__class_weight': [{True: 6, False: 1}, {True: 7, False: 1}, {True: 8, False: 1}, \
                           {True: 9, False: 1}, {True: 10, False: 1}]
          }

pipeline2 = Pipeline(steps=[('minmaxer', scaler),
                            ('selection', SelectKBest(score_func=f_classif)),
                            ('reducer', PCA()),
                            ('classifier', SVC(random_state=42))])

clf2 = GridSearchCV(pipeline2, param_grid=param_grid2, cv=k_fold, scoring=scorer)

#RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier

param_grid3 = {
          'reducer__n_components': [0.2, 0.5, 0.7, 2, 3, 4],
          'selection__k': [5,6,7,'all'],
          'classifier__criterion' : ['gini', 'entropy'],
          'classifier__max_features' : ['auto', 'sqrt', 'log2'],
          'classifier__min_samples_split' : [2,5,8,10],
          'classifier__max_depth': [1,2,3,None],
          'classifier__class_weight': [{True: 6, False: 1}, {True: 7, False: 1}, {True: 8, False: 1}, \
                           {True: 9, False: 1}, {True: 10, False: 1}]
          }

pipeline3 = Pipeline(steps=[('minmaxer', scaler),
                            ('selection', SelectKBest(score_func=f_classif)),
                            ('reducer', PCA()),
                            ('classifier', RandomForestClassifier(random_state=42))])

clf3 = GridSearchCV(pipeline3, param_grid=param_grid3, cv=k_fold, scoring=scorer)

#AdaBoostClassifier
from sklearn.ensemble import AdaBoostClassifier

param_grid4 = {
          'reducer__n_components': [0.2, 0.5, 0.7, 2, 3, 4],
          'selection__k': [5,6,7,'all'],
          'classifier__n_estimators' : [10, 30, 50, 70, 100],
          'classifier__learning_rate': [0.01, 0.05, 0.1, 0.5, 1],
          }

pipeline4 = Pipeline(steps=[('minmaxer', scaler),
                            ('selection', SelectKBest(score_func=f_classif)),
                            ('reducer', PCA()),
                            ('classifier', AdaBoostClassifier(random_state=42))])

clf4 = GridSearchCV(pipeline4, param_grid=param_grid4, cv=k_fold, scoring=scorer)

#LogisticRegression
from sklearn.linear_model import LogisticRegression
param_grid5 = {
        'reducer__n_components': [0.2, 0.5, 0.7, 2, 3, 4],
        'selection__k': [5,6,7,'all'],
        'classifier__C': [1e-4, 1e-3, 1e-2, 1e-1, 1],
        'classifier__tol': [1, 1e-1, 1e-4, 1e-16, 1e-32, 1e-64],
        'classifier__class_weight': [{True: 7, False: 1}, {True: 7.3, False: 1}, \
                           {True: 7.5, False: 1}, {True: 7.8, False: 1}, 'auto']
        }


pipeline5 = Pipeline(steps=[('minmaxer', scaler),
                            ('selection', SelectKBest(score_func=f_classif)),
                            ('reducer', PCA()),
                            ('classifier', LogisticRegression(random_state=42))])

clf5 = GridSearchCV(pipeline5, param_grid=param_grid5, cv=k_fold, scoring=scorer)


### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

#from sklearn.cross_validation import train_test_split
#features_train, features_test, labels_train, labels_test = \
    #train_test_split(features, labels, test_size=0.3, random_state=42)

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

final_clf = None

######################################
# Test Best Algorithm and parameters
######################################

#from sklearn import cross_validation
#for clf in [clf1, clf2, clf3, clf4, clf5]:

    #clf.fit(features, labels)
    #print('Best Parameters: ', clf.best_params_)
    #print('Best Score: ', clf.best_score_)

    #selector = clf.best_estimator_.named_steps['selection'].get_support()
    #print(zip(all_features_list, selector))
    #top_features = [x for (x, boolean) in zip(all_features_list, selector) if boolean]
    #n_pca_components = clf.best_estimator_.named_steps['reducer'].n_components_

    #print('Top Features: ', top_features)
    #print('Number o PCA components: ', n_pca_components)
    #final_clf = clf.best_estimator_
    #test_classifier(clf.best_estimator_, my_dataset, features_list)

    #print('---------------------')

######################################
# Best Algorithm and parameters
######################################

best_params = {
   'classifier__class_weight': [{False: 1, True: 7.8}],
   'selection__k': ['all'],
   'classifier__C': [0.001],
   'reducer__n_components': [4],
   'classifier__tol': [1e-32]}

pipeline = Pipeline(steps=[('minmaxer', scaler),
                            ('selection', SelectKBest(score_func=f_classif)),
                            ('reducer', PCA()),
                            ('classifier', LogisticRegression(random_state=42))])

clf = GridSearchCV(pipeline, param_grid=best_params, cv=k_fold, scoring=scorer)
clf.fit(features, labels)

scores = clf.best_estimator_.named_steps['selection'].scores_
pprint(sorted(zip(all_features_list, scores), key=lambda x:x[1] ))
print(clf.best_estimator_.named_steps['reducer'].explained_variance_ratio_)

final_clf = clf.best_estimator_
test_classifier(final_clf, my_dataset, features_list)

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

#final_clf = RandomForestClassifier(min_samples_split = 2, max_depth = 1, class_weight = {False: 1, True: 9})
dump_classifier_and_data(final_clf, my_dataset, features_list)

