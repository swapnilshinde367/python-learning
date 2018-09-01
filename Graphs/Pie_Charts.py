#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 00:38:40 2018

@author: swapnil
"""


import matplotlib.pyplot as plt

arrintBins = [ 150,20,30,25,25 ]
arrstrLabels = [ 'Logged In','Not Logged In','On Leave','Not in Shift','Not Applicable' ]

plt.pie(
        arrintBins,
        labels = arrstrLabels,
        autopct = '%1.1f%%',
        startangle = 90)

plt.title( 'Pie Chart Example\nThis is New Line' )

plt.show()