#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 00:48:58 2018

@author: swapnil
"""

import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter
    

def graph_data():

    strUrl = 'https://pythonprogramming.net/yahoo_finance_replacement'
    arrstrSourceCode = urllib.request.urlopen( strUrl ).read().decode()
    arrstrStockData = []
    arrstrStockSplitData = arrstrSourceCode.split( '\n' )
#    
    for strStockData in arrstrStockSplitData[1:] :
        strTempStockData = strStockData.split( ',' )
        if( 7 == len( strStockData ) ) :
            if 'values' not in strStockData and 'labels' not in strStockData:
                arrstrStockData.append(strTempStockData)
            
    strDate, fltClosePrice, fltHighPrice,fltLowPrice, fltOpenPrice, fltVolume = np.loadtxt( arrstrStockData,
                                                      delimiter = ',',
                                                      unpack = True,
                                                      converters = 
                                                      { 0: bytespdate2num( '%Y-%m-%d' ) }
                                                    )

#    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
#    source_code = urllib.request.urlopen(stock_price_url).read().decode()
#    stock_data = []
#    split_source = source_code.split('\n')
#    for line in split_source[1:]:
#        split_line = line.split(',')
#        if len(split_line) == 7:
#            if 'values' not in line and 'labels' not in line:
#                stock_data.append(line)
#
#    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
#                                                          delimiter=',',
#                                                          unpack=True,
#                                                          # %Y = full year. 2015
#                                                          # %y = partial year 15
#                                                          # %m = number month
#                                                          # %d = number day
#                                                          # %H = hours
#                                                          # %M = minutes
#                                                          # %S = seconds
#                                                          # 12-06-2014
#                                                          # %m-%d-%Y
#                                                          converters={0: bytespdate2num('%Y-%m-%d')})

    
#            print(strStockData)

#    split_source = source_code.split('\n')
#    for line in split_source[1:]:
#        split_line = line.split(',')
#        if len(split_line) == 7:
#            if 'values' not in line and 'labels' not in line:
#                stock_data.append(line)
                


graph_data()