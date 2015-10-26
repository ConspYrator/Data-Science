# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 16:17:19 2015

@author: balazs
"""
import csv
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

data = pd.read_csv('kshdata.csv', index_col=False, header=0)
x = data.date.values
y = data.wage.values

x = x.reshape(len(x), 1)
y = y.reshape(len(y), 1)

#clf = linear_model.LinearRegression()
clf = make_pipeline(PolynomialFeatures(4), Ridge())
clf.fit (x, y)


# Predicting in which year wages exceed a given threshold
number = 0
year = 2015
threshold = 500000 # set threshold here

while number < threshold:
    year = year + 1
    number = clf.predict(year)
        
print "Wages will exceed %s HUF in year %s; predicted wages for year %s is %d HUF." % (threshold, year, year, clf.predict(year))

# plotting
font = {'family' : 'serif',
        'color'  : 'darkred',
        'weight' : 'normal',
        'size'   : 16,
        }
        
plt.scatter(x, y, color='black', label="wage")
plt.plot(x, clf.predict(x), color='blue', linewidth=3)
plt.title('change in wages', fontdict=font)
plt.xlabel('date', fontdict=font)
plt.ylabel('wage (HUF)', fontdict=font)
plt.show()