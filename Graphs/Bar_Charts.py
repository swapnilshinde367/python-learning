#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 20:27:36 2018

@author: swapnil
"""

import matplotlib.pyplot as plt

arrintXArray = [1,3,5,7,9]
arrintYArray = [1,3,5,7,9]

plt.bar(arrintXArray, arrintYArray, label='Odd Values', color='black')

arrintXArray = [2,4,6,8]
arrintYArray = [2,4,6,8]

plt.bar(
        arrintXArray, 
        arrintYArray, 
        label='Even Values', 
        color='yellow')

plt.title( 'Bar Graph Example\nThis is New Line' )
plt.xlabel( 'X Values' )
plt.ylabel( 'Y Values' )
plt.legend()
plt.show()