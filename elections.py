import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Output, Input

import plotly.express as px
import pandas as pd

 #owner: Dustin Childers on Kaggle, source: https://data.brla.gov/Public-Safety/Animal-Control-Incidents/qmns-hw3s
df = pd.read_csv("elections.csv")

app = dash.Dash(__name__,
                meta_tags=[{'name': 'viewport',
                             'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}]
                )


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


app.layout = dbc.Container([title, row1,output1,output2])


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
    fig1 = px.pie(dff, names="Party", values="Percent", title="Percent")



    return fig1,fig2

app.run_server(debug=True)
server = app.server
