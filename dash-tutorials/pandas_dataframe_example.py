#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 00:04:55 2018

@author: swapnil
"""

import pandas_datareader.data as web
import datetime

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime.now()

df = web.DataReader('TSLA', 'google', start, end)

print(df.head())