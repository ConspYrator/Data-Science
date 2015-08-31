# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 10:35:12 2015

@author: balazs
"""

# Example code for doing linear regression in sklearn.

from sklearn import linear_model

clf = linear_model.LinearRegression()

# Fit model
clf.fit ([[0, 0], [1, 1], [2, 2]], [0, 1, 2])

# Make prediction
print clf.predict([[45, 4]])

# Print coefficients and intercept
print clf.coef_
print clf.intercept_ 