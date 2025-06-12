import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

# Carrega dados processados
df = pd.read_csv("data/dados_tratados.csv")
fig = px.line(df, x="ano", y="casos", color="estado", title="Casos de Dengue por Estado")

app.layout = html.Div([
    html.H1("Previsão de Casos de Dengue"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)