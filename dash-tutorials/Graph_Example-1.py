#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 17:55:50 2018

@author: swapnil
"""

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
import datetime

app = dash.Dash()

app.layout = html.Div(
                children = [
                        dcc.Input( id='input', placeholder='Enter Stock Name', type='text'),
                        html.Div(id='output-graph')
                ]
            )

@app.callback(
    Output( component_id = 'output-graph', component_property = 'children' ),
    [ Input( component_id= 'input', component_property = 'value' ) ]  
)

def update_graph( stock ) :

    if( '' == stock )  :
        stock = 'TSLA'

    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime.now()
    df = web.DataReader( stock, 'google', start, end )
    
    return dcc.Graph(
                    id = 'graph',
                    figure = {
                        'data' : [
                                    { 'x': df.index, 'y': df.Close, 'type': 'line', 'name' : stock }
                                ],
                        'layout' : {
                            'title' : stock
                        }
                    }
                )

if __name__ == '__main__' :
    app.run_server( debug = True )