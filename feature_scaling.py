# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 11:04:15 2015

@author: balazs
"""

#Implementation 1:

from __future__ import division

def featureScaling(arr):
    min_arr = min(arr); max_arr = max(arr); new_arr = []
    for i in arr:
        new_arr.append((i - min_arr) / (max_arr - min_arr))
    return new_arr

# test of feature scaler
data = [115, 140, 175]
print featureScaling(data)


#Implementation 2:

from sklearn.preprocessing import MinMaxScaler
import numpy

weights = numpy.array([[115.], [140.], [175.]])
scaler = MinMaxScaler()
rescaled_weights = scaler.fit_transform(weights)

print rescaled_weights