#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 00:42:48 2018

@author: swapnil
"""

import dash
import time
import random
from collections import deque
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from pandas_datareader.data import DataReader

app = dash.Dash( 'vehicle-data' )

max_length = 50
times = deque( maxlen = max_length )
oil_temps = deque( maxlen = max_length )
intake_temps = deque( maxlen = max_length )
coolant_temps = deque( maxlen = max_length )
rpms = deque( maxlen = max_length )
speeds = deque( maxlen = max_length )
throttle_pos = deque( maxlen = max_length )


data_dict = {
    'Oil Temp' : oil_temps,
    'Intake Temp' : intake_temps,
    'Coolant Temp' : coolant_temps,    
    'RPM' : rpms,
    'Speed' : speeds,
    'Throttle Pos' : throttle_pos
}

def update_obd_values( times, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos ) :
    
    times.append(time.time())
    
    if len(times) == 1 :
        # starting relative values
        oil_temps.append( random.randomrange( 180, 230 ) )
        intake_temps.append( random.randomrange( 180, 230 ) )
        coolant_temps.append( random.randomrange( 180, 230 ) )
        rpms.append( random.randomrange( 180, 230 ) )
        speeds.append( random.randomrange( 180, 230 ) )
        throttle_pos.append( random.randomrange( 180, 230 ) )
    else :
        for data_of_interest in [ times, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos ] :
            data_of_interest.append( data_of_interest[-1] + data_of_interest[-1] * random.uniform( -0.0001,0.0001 ) )
    
    return times, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos

app.layout = html.Div([
    html.Div([
        html.H2('Vehicle Data',
                style={'float': 'left',
                       }),
        ]),
    dcc.Dropdown(id='vehicle-data-name',
                 options=[{'label': s, 'value': s}
                          for s in data_dict.keys()],
                 value=['Coolant Temperature','Oil Temperature','Intake Temperature'],
                 multi=True
                 ),
    html.Div(children=html.Div(id='graphs'), className='row'),
    dcc.Interval(
        id='graph-update',
        interval=100),
    ], className="container",style={'width':'98%','margin-left':10,'margin-right':10,'max-width':50000})

