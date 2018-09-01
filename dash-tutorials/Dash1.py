#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 18:30:29 2018

@author: swapnil
"""

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
                dcc.Input(id='input', placeholder='Enter Something Here', type='text'),
                html.Div(id='output')
            ])

@app.callback(
        Output( component_id = 'output', component_property = 'children'),
        [Input( component_id = 'input', component_property='value' ) ]
        )

def update_value( input_data ) :
    
    if( '' != input_data ) :
        try :
            return str( float( input_data ) ** 2 )
        except :
            return "Enter number"

if __name__ == '__main__':
    app.run_server(debug=True)