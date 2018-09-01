#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 01:06:00 2018

@author: swapnil
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

youtube_data = pd.read_csv('video_result.csv')

#print(youtube_data)

#print(youtube_data.corr())

plt.figure()
#plt.scatter(youtube_data.viewCount,youtube_data.likeCount)

y = youtube_data.likeCount
X = youtube_data.viewCount
X = sm.add_constant(X)
#print(X)

#Linear Model
lr_model = sm.OLS(y,X).fit()
#print(lr_model.summary())

X_Prime = np.linspace(X.viewCount.min(),X.viewCount.max(),100)
#print(X_Prime)
X_Prime = sm.add_constant(X_Prime)
y_hat = lr_model.predict(X_Prime)

plt.scatter(X.viewCount,y)
plt.xlabel('View Count')
plt.ylabel('Like Count')
plt.plot(X_Prime[:,1],y_hat)

#list = [ 'abcd', 345 , 2.23, 'randy', 70.2 ]
#
#print (X_Prime[:,1])

#print (list[-3])
