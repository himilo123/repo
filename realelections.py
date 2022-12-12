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

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP])
header = html.H2("Himilo Data Solutions & Research Center", style={'textAlign': 'center'})
title = html.H5("Somaliland Parliamentary and Municipality Voting  Analysis", style={'textAlign': 'center'})

with open(r'json-sml-regions.txt') as j1:
    geojson1 = json.load(j1)
geojson1 = rewind(geojson1, rfc7946=False)

with open(r'json-sml-districts.txt') as j2:
    geojson2 = json.load(j2)
geojson2 = rewind(geojson2, rfc7946=False)

df1 = pd.read_csv(r'realelectons.csv')

input1 = dbc.Col(dcc.RadioItems(id='drop1', options=[{'label': x, 'value': x} for x in df1['Year'].unique()],
                                value=2021))

output1 = dbc.Col(dcc.Graph(id='myfig1', figure={}),xs=12, sm=12, md=12, lg=4, xl=4)
output2 = dbc.Col(dcc.Graph(id='myfig2', figure={}),xs=12, sm=12, md=12, lg=4, xl=4)
output3 = dbc.Col(dcc.Graph(id='myfig3', figure={}),xs=12, sm=12, md=10, lg=4, xl=4)
output4 = dbc.Col(dcc.Graph(id='myfig4', figure={}),xs=12, sm=12, md=12, lg=4, xl=4)
output5 = dbc.Col(dcc.Graph(id='myfig5', figure={}),xs=12, sm=12, md=12, lg=4, xl=4)
output6 = dbc.Col(dcc.Graph(id='myfig6', figure={}),xs=12, sm=12, md=12, lg=4, xl=4)
output7 = dbc.Col(dcc.Graph(id='myfig7', figure={}),xs=12, sm=12, md=12, lg=6, xl=6)
output8 = dbc.Col(dcc.Graph(id='myfig8', figure={}),xs=12, sm=12, md=12, lg=6, xl=6)

# row1 = [input1, style={'textAlign': 'center'}]

row1 = html.H6([ input1], style={'textAlign': 'center'})
row2 = dbc.Row([output1, output2, output3])
row3 = dbc.Row([output4, output5, output6])
row4 = dbc.Row([output7, output8])
app.layout = dbc.Container([header,title,row4, row1, row2, row3])


@app.callback(
    Output(component_id="myfig1", component_property='figure'),
    Output(component_id="myfig2", component_property='figure'),
    Output(component_id="myfig3", component_property='figure'),
    Output(component_id="myfig4", component_property='figure'),
    Output(component_id="myfig5", component_property='figure'),
    Output(component_id="myfig6", component_property='figure'),
    Output(component_id="myfig7", component_property='figure'),
    Output(component_id="myfig8", component_property='figure'),
    Input(component_id='drop1', component_property='value'),
)
def himilo(var1):
    dff = df1[(df1["Year"] == var1)]
    fig1 = px.choropleth(dff, geojson=geojson1, locations='name', color='Kulmiye%', featureidkey="properties.name",range_color=(20, 40),
                         title='Kulmiye Parliment Seats',color_continuous_scale="Viridis", hover_data=["Total","Kulmiye", "Kulmiye%"])
    fig1.update_geos(fitbounds="locations", visible=False)
    fig1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig1.layout.update(dragmode=False)

    dff = df1[(df1["Year"] == var1)]
    fig2 = px.choropleth(dff, geojson=geojson1, locations='name', color='Wadani%', featureidkey="properties.name",range_color=(20, 40),
                         title='Wadani Parliment Seats',color_continuous_scale="Viridis", hover_data=["Total","Wadani", "Wadani%"])
    fig2.update_geos(fitbounds="locations", visible=False)
    fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig2.layout.update(dragmode=False)

    dff = df1[(df1["Year"] == var1)]
    fig3 = px.choropleth(dff, geojson=geojson1, locations='name', color='Ucid%', featureidkey="properties.name",range_color=(20, 40),
                         title='Ucid Parliment Seats', color_continuous_scale="Viridis",hover_data=["Total","Ucid", "Ucid%"])
    fig3.update_geos(fitbounds="locations", visible=False)
    fig3.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig3.layout.update(dragmode=False)

    dff = df1[(df1["Year"] == var1)]
    fig4 = px.choropleth(dff, geojson=geojson2, locations='name', color='kulmiye%', featureidkey="properties.name",range_color=(0, 50),
                         title='Kulmiye Municiplity Seats', color_continuous_scale="Viridis",hover_data=["total","kulmiye", "kulmiye%"])
    fig4.update_geos(fitbounds="locations", visible=False)
    fig4.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig4.layout.update(dragmode=False)

    dff = df1[(df1["Year"] == var1)]
    fig5 = px.choropleth(dff, geojson=geojson2, locations='name', color='wadani%', featureidkey="properties.name",range_color=(0, 50),
                         title='Wadani Municiplity Seats',color_continuous_scale="Viridis", hover_data=["total","wadani", "wadani%"])
    fig5.update_geos(fitbounds="locations", visible=False)
    fig5.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig5.layout.update(dragmode=False)

    dff = df1[(df1["Year"] == var1)]
    fig6 = px.choropleth(dff, geojson=geojson2, locations='name', color='ucid%', featureidkey="properties.name",range_color=(0, 50),
                         title='Ucid Municiplity Seats', color_continuous_scale="Viridis",hover_data=["total","ucid", "ucid%"])
    fig6.update_geos(fitbounds="locations", visible=False)
    fig6.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig6.layout.update(dragmode=False)
    
    fig7 = px.choropleth(dff, geojson=geojson1, locations='name', color='Won', featureidkey="properties.name",range_color=(20, 40),
                         title='Kulmiye Parliment Seats', color_continuous_scale="Viridis",hover_data=["Total","Kulmiye", "Kulmiye%"])
    fig7.update_geos(fitbounds="locations", visible=False)
    fig7.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig7.layout.update(dragmode=False)

    
    dff = df1[(df1["Year"] == var1)]
    fig8 = px.choropleth(dff, geojson=geojson2, locations='name', color='won', featureidkey="properties.name",range_color=(0, 50),
                         title='Kulmiye Municiplity Seats', color_continuous_scale="Viridis",hover_data=["total","kulmiye", "kulmiye%"])
    fig8.update_geos(fitbounds="locations", visible=False)
    fig8.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig8.layout.update(dragmode=False)
    

    return fig1, fig2, fig3, fig4, fig5, fig6,fig7,fig8

app.run(host='0.0.0.0')
#app.run(port = 4060)
server = app.server
