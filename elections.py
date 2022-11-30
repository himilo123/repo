
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

fig = go.Figure()
import dash
import plotly.express as px
import pandas as pd
from dash import Input, Output, html, dcc


app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])
title = html.H1("Somaliland Presidential Eelections", style={'textAlign': 'center'})

df = pd.read_csv('elections.csv')


input1 = dbc.Col(dcc.Dropdown(id='drop1', options=[{'label': x, 'value': x} for x in df['Year'].unique()],
                              value=2017))
input2 = dbc.Col(dcc.Dropdown(id='drop2', options=[{'label': x, 'value': x} for x in df['Region'].unique()],
                            value="Awdal"))

output1 = dbc.Col(dcc.Graph(id='myfig1', figure={}))
output2 = dbc.Col(dcc.Graph(id='myfig2', figure={}))


row1 = dbc.Row([input1,input2])
row2 = dbc.Row([output1,output2])


app.layout = dbc.Container([title, row1,row2])


@app.callback(
    Output(component_id="myfig1", component_property='figure'),
    Output(component_id="myfig2", component_property='figure'),
    Input(component_id='drop1', component_property='value'),
    Input(component_id='drop2', component_property='value'),

)
def himilo(var1,var2):
    dff = df[(df["Year"] == var1) & (df["Region"] == var2)]

    fig1 = px.pie(dff, names="Party", values="Percent", title="Percent")
    fig2 = px.bar(dff, x="Party", y="Votes", title="Votes",color = "Party")


    return fig1,fig2

app.run_server(0.0.0.0,debug=True)
server = app.server
