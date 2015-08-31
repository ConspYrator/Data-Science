# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 09:17:36 2015

@author: balazs
"""

from sklearn import datasets
from sklearn.svm import SVC
from sklearn import cross_validation

# Load Iris dataset from sklearn

iris = datasets.load_iris()
features = iris.data
labels = iris.target

# Splitting data into training and test sets

features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.4, random_state=0)

# Train Support Vector Machine

clf = SVC(kernel="linear", C=1.)
clf.fit(features_train, labels_train)

# Print out result on test data

print clf.score(features_test, labels_test)