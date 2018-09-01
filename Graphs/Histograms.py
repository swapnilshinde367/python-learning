#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 22:25:44 2018

@author: swapnil
"""

import matplotlib.pyplot as plt

arrintPopulationAges = [12,10,130,4,31,6,54,76,120,115,98,85,67,33,35,80,99,110,19,103,50,51,52,53,54,55]

#segment or span in whoch histogram will show
arrintBins = [0,20,40,60,80,100,120,140]

plt.hist(
        [arrintPopulationAges, arrintBins], 
        arrintBins, 
        histtype='bar', 
        rwidth = 0.7, 
        stacked = True, 
        label=['No of People', 'Bin Numbers'] )

plt.title( 'Histogram Example\nThis is New Line' )
plt.xlabel( 'Age Groups' )
plt.ylabel( 'No of People' )
plt.legend()
plt.show()