from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from urllib.request import urlopen
import json
import geojson_rewind
from geojson_rewind import rewind
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Output, Input

app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])
header = html.H2("Himilo Data Solutions & Research", style={'textAlign': 'center'})
title = html.H5("Somaliland Polotical Parties voting pool analysis", style={'textAlign': 'center'})

df11 = pd.read_excel(r'C:\Users\Admin\Desktop\YAHOO\fips1.xlsx')
df12 = pd.read_excel(r'C:\Users\Admin\Desktop\YAHOO\fips2.xlsx')
df13 = pd.read_excel(r'C:\Users\Admin\Desktop\YAHOO\fips3.xlsx')

with open(r'C:\Users\Admin\Desktop\YAHOO\json.txt') as j1:
    geojson1 = json.load(j1)
geojson1 = rewind(geojson1, rfc7946=False)

fig1 = px.choropleth(df11, geojson=geojson1, locations='name', color='Vote%', featureidkey="properties.name",
                     title='Kulmiye Votes% Region Level')
fig1.update_geos(fitbounds="locations", visible=False)
fig1 = dbc.Col(dcc.Graph(figure=fig1))

fig2 = px.choropleth(df12, geojson=geojson1, locations='name', color='Vote%', featureidkey="properties.name",
                     title='Wadani Votes% Region Level')
fig2.update_geos(fitbounds="locations", visible=False)
fig2 = dbc.Col(dcc.Graph(figure=fig2))

fig3 = px.choropleth(df13, geojson=geojson1, locations='name', color='Vote%', featureidkey="properties.name",
                     title='Ucid Votes% Region Level')
fig3.update_geos(fitbounds="locations", visible=False)
fig3 = dbc.Col(dcc.Graph(figure=fig3))

df21 = pd.read_excel(r'C:\Users\Admin\Desktop\YAHOO\fipss1.xlsx')
df22 = pd.read_excel(r'C:\Users\Admin\Desktop\YAHOO\fipss2.xlsx')
df23 = pd.read_excel(r'C:\Users\Admin\Desktop\YAHOO\fipss3.xlsx')

with open(r'C:\Users\Admin\Desktop\YAHOO\sml.txt') as j2:
    geojson2 = json.load(j2)

geojson2 = rewind(geojson2, rfc7946=False)

fig4 = px.choropleth(df21, geojson=geojson2, locations='name', color='Vote%', featureidkey="properties.name",
                     title='Kulmiye Votes% District Level')
fig4.update_geos(fitbounds="locations", visible=False)
fig4 = dbc.Col(dcc.Graph(figure=fig4))

fig5 = px.choropleth(df22, geojson=geojson2, locations='name', color='Vote%', featureidkey="properties.name",
                     title='Wadani Votes% District Level')
fig5.update_geos(fitbounds="locations", visible=False)
fig5 = dbc.Col(dcc.Graph(figure=fig5))

fig6 = px.choropleth(df23, geojson=geojson2, locations='name', color='Vote%', featureidkey="properties.name",
                     title='Ucid Votes% District Level')
fig6.update_geos(fitbounds="locations", visible=False)
fig6 = dbc.Col(dcc.Graph(figure=fig6))

row1 = dbc.Row([fig1, fig2, fig3])
row2 = dbc.Row([fig4, fig5, fig6])

app.layout = dbc.Container([title, row1, row2])
app.run_server(port=4089)