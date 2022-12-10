import plotly.express as px
import geojson_rewind
from geojson_rewind import rewind
import dash
from dash import Dash, dcc, html, Input, Output

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from urllib.request import urlopen
import json

import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Output, Input

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
header = html.H2("Himilo Data Solutions & Research", style={'textAlign': 'center'})
title = html.H5("Somaliland Polotical Parties voting pool analysis", style={'textAlign': 'center'})

with open(r'json-sml-regions.txt') as j1:
    geojson1 = json.load(j1)
geojson1 = rewind(geojson1, rfc7946=False)

with open(r'json-sml-districts.txt') as j2:
    geojson2 = json.load(j2)
geojson2 = rewind(geojson2, rfc7946=False)

df1 = pd.read_csv(r'regions-district.csv')

input1 = dbc.Col(dcc.RadioItems(id='drop1', options=[{'label': x, 'value': x} for x in df1['Year'].unique()],
                                value=2021))

output1 = dbc.Col(dcc.Graph(id='myfig1', figure={}))
output2 = dbc.Col(dcc.Graph(id='myfig2', figure={}))
output3 = dbc.Col(dcc.Graph(id='myfig3', figure={}))
output4 = dbc.Col(dcc.Graph(id='myfig4', figure={}))
output5 = dbc.Col(dcc.Graph(id='myfig5', figure={}))
output6 = dbc.Col(dcc.Graph(id='myfig6', figure={}))

# row1 = [input1, style={'textAlign': 'center'}]

row1 = html.H6(["Select The Year", input1], style={'textAlign': 'center'})
row2 = dbc.Row([output1, output2, output3])
row3 = dbc.Row([output4, output5, output6])

app.layout = dbc.Container([title, row1, row2, row3])


@app.callback(
    Output(component_id="myfig1", component_property='figure'),
    Output(component_id="myfig2", component_property='figure'),
    Output(component_id="myfig3", component_property='figure'),
    Output(component_id="myfig4", component_property='figure'),
    Output(component_id="myfig5", component_property='figure'),
    Output(component_id="myfig6", component_property='figure'),
    Input(component_id='drop1', component_property='value'),

)
def himilo(var1):
    dff = df1[(df1["Year"] == var1)]
    fig1 = px.choropleth(dff, geojson=geojson1, locations='name', color='Kulmiye_Vote%', featureidkey="properties.name",
                         title='Kulmiye Votes% Regional Level')
    fig1.update_geos(fitbounds="locations", visible=False)

    dff = df1[(df1["Year"] == var1)]
    fig2 = px.choropleth(dff, geojson=geojson1, locations='name', color='Wadani_Vote%', featureidkey="properties.name",
                         title='Wadani Votes% Regional Level')
    fig2.update_geos(fitbounds="locations", visible=False)

    dff = df1[(df1["Year"] == var1)]
    fig3 = px.choropleth(dff, geojson=geojson1, locations='name', color='Ucid_Vote%', featureidkey="properties.name",
                         title='Ucid Votes% Regional Level')
    fig3.update_geos(fitbounds="locations", visible=False)

    dff = df1[(df1["Year"] == var1)]
    fig4 = px.choropleth(dff, geojson=geojson2, locations='name', color='Kulmiye', featureidkey="properties.name",
                         title='Kulmiye Votes% District Level')
    fig4.update_geos(fitbounds="locations", visible=False)

    dff = df1[(df1["Year"] == var1)]
    fig5 = px.choropleth(dff, geojson=geojson2, locations='name', color='Wadani', featureidkey="properties.name",
                         title='Wadani Votes% District Level')
    fig5.update_geos(fitbounds="locations", visible=False)

    dff = df1[(df1["Year"] == var1)]
    fig6 = px.choropleth(dff, geojson=geojson2, locations='name', color='Ucid', featureidkey="properties.name",
                         title='Ucid Votes% District Level')
    fig6.update_geos(fitbounds="locations", visible=False)

    return fig1, fig2, fig3, fig4, fig5, fig6

app.run(host='0.0.0.0')

server = app.server
