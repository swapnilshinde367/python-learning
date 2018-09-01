#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 17:21:05 2018

@author: swapnil

prediction value = coefficient*your existing value + constant
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

twitter_data = pd.read_csv('twitter_result.csv')

#print(twitter_data)

plt.figure()

#hist1,edges1 = np.histogram(twitter_data.friends)

#plt.bar(edges1[:-1],hist1,width=edges1[1:]-edges1[:-1])

#plt.scatter(twitter_data.followers,twitter_data.retwc)

y = twitter_data.retwc

X = twitter_data.followers
X = sm.add_constant(X)

lr_model = sm.OLS(y,X).fit()

#print(lr_model.summary())

X_Prime = np.linspace(X.followers.min(),X.followers.max(),100)
X_Prime = sm.add_constant(X_Prime)

y_hat = lr_model.predict(X_Prime)

plt.scatter(X.followers,y)
plt.xlabel('Followers')
plt.ylabel('Re-Tweets')
plt.plot(X_Prime[:,1],y_hat)
