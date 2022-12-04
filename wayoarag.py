import plotly.graph_objects as go

fig = go.Figure()
import pandas as pd

import dash
import plotly.express as px
import pandas as pd
from dash import Input, Output, html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.QUARTZ])
title = html.H1("Wayoarag-Statistics", style={'textAlign': 'center'})

df= pd.read_csv(r'wayoarag.csv')
#print(df.head())
Ahmed_S = pd.DataFrame(df['Ahmed_S'].value_counts(normalize=True) * 100).reset_index()
Salo = pd.DataFrame(df['Salo'].value_counts(normalize=True) * 100).reset_index()
Abdishakur = pd.DataFrame(df['Abdishakur'].value_counts(normalize=True) * 100).reset_index()
Ali = pd.DataFrame(df['Ali'].value_counts(normalize=True) * 100).reset_index()
Abdiraxman = pd.DataFrame(df['Abdiraxman'].value_counts(normalize=True) * 100).reset_index()
Ahmed_C = pd.DataFrame(df['Ahmed_C'].value_counts(normalize=True) * 100).reset_index()
Abshir = pd.DataFrame(df['Abshir'].value_counts(normalize=True) * 100).reset_index()
Mukhtar = pd.DataFrame(df['Mukhtar'].value_counts(normalize=True) * 100).reset_index()
Mustafe = pd.DataFrame(df['Mustafe'].value_counts(normalize=True) * 100).reset_index()
M_Hassan = pd.DataFrame(df['M_Hassan'].value_counts(normalize=True) * 100).reset_index()
Idiris = pd.DataFrame(df['Idiris'].value_counts(normalize=True) * 100).reset_index()
Hamse = pd.DataFrame(df['Hamse'].value_counts(normalize=True) * 100).reset_index()
Baxraawi = pd.DataFrame(df['Baxraawi'].value_counts(normalize=True) * 100).reset_index()
Janaale = pd.DataFrame(df['Janaale'].value_counts(normalize=True) * 100).reset_index()


fig1 = px.pie(Ahmed_S, values='Ahmed_S', names='index', title='Ahmed_S ')
fig2 = px.pie(Salo, values='Salo', names='index', title='Salo ')
fig3 = px.pie(Abdishakur, values='Abdishakur', names='index', title='Abdishakur ')
fig4 = px.pie(Ali, values='Ali', names='index', title='Ali ')
fig5 = px.pie(Abdiraxman, values='Abdiraxman', names='index', title='Abdiraxman ')
fig6 = px.pie(Ahmed_C, values='Ahmed_C', names='index', title='Ahmed_C ')
fig7 = px.pie(Abshir, values='Abshir', names='index', title='Abshir ')
fig8 = px.pie(Mukhtar, values='Mukhtar', names='index', title='Mukhtar ')
fig9 = px.pie(Mustafe, values='Mustafe', names='index', title='Mustafe ')
fig10 = px.pie(Idiris, values='Idiris', names='index', title='Idiris ')
fig11 = px.pie(Hamse, values='Hamse', names='index', title='Hamse ')
fig12 = px.pie(Baxraawi, values='Baxraawi', names='index', title='Baxraawi')
fig13 = px.pie(M_Hassan, values='M_Hassan', names='index', title='M_Hassan')
fig14 = px.pie(Janaale, values='Janaale', names='index', title='Janaale')


fig1 = dbc.Col(dcc.Graph(figure=fig1))
fig2 = dbc.Col(dcc.Graph(figure=fig2))
fig3 = dbc.Col(dcc.Graph(figure=fig3))
fig4 = dbc.Col(dcc.Graph(figure=fig4))
fig5 = dbc.Col(dcc.Graph(figure=fig5))
fig6 = dbc.Col(dcc.Graph(figure=fig6))
fig7 = dbc.Col(dcc.Graph(figure=fig7))
fig8 = dbc.Col(dcc.Graph(figure=fig8))
fig9 = dbc.Col(dcc.Graph(figure=fig9))
fig10 = dbc.Col(dcc.Graph(figure=fig10))
fig11 = dbc.Col(dcc.Graph(figure=fig11))
fig12 = dbc.Col(dcc.Graph(figure=fig12))
fig13 = dbc.Col(dcc.Graph(figure=fig13))
fig14 = dbc.Col(dcc.Graph(figure=fig14))

row1 = dbc.Row([fig1])
row2 = dbc.Row([fig2])
row3 = dbc.Row([fig3])
row4 = dbc.Row([fig4])
row5 = dbc.Row([fig5])
row6 = dbc.Row([fig6])
row7 = dbc.Row([fig7])
row8 = dbc.Row([fig8])
row9 = dbc.Row([fig9])
row10 = dbc.Row([fig10])
row11 = dbc.Row([fig11])
row12 = dbc.Row([fig12])
row13 = dbc.Row([fig13])
row14 = dbc.Row([fig14])
app.layout = dbc.Container([title,row1,row2,row3,row4,row5,row6,row7,row8,row9,row10,row11,row12,row13,row14])

app.run(host='0.0.0.0')

server = app.server
