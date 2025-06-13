import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import flask
import os
from security.auth import authenticate, log_user_access

df_pdf = pd.read_csv(os.path.join("data", "dados_agrupados.csv"))
df_pdf["ds"] = pd.to_datetime(df_pdf["ds"])
df_pdf["ANO"] = df_pdf["ds"].dt.year

# Adicionando leitura das previsões futuras
df_forecast = pd.read_csv(os.path.join("data", "previsao_futura.csv"))
df_forecast["ds"] = pd.to_datetime(df_forecast["ds"])
df_forecast["ANO"] = df_forecast["ds"].dt.year

df_2024 = pd.read_csv(os.path.join("data", "pdf_2024_exportado.csv"))
df_2024["DATA"] = pd.to_datetime(df_2024["DATA"])
# df_2024 já tem coluna ANO

# Inicializa o app
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Dashboard de Casos de Dengue"
server = app.server

# Sessão Flask para login
app.server.secret_key = 'supersecretkey'  # Troque em produção

# Layout do app
def serve_layout():
    if flask.session.get('logged_in'):
        return dbc.Container([
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.H1([
                            html.I(className="bi bi-bar-chart-line-fill me-2 text-primary", style={"fontSize": "2rem"}),
                            "Dashboard de Casos de Dengue"
                        ], className="text-center my-4 fw-bold")
                    ])
                ]),
                # Card de filtros
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.Div([
                                    html.Label("Escolha o conjunto de dados:", className="fw-bold mb-2"),
                                    dcc.RadioItems(
                                        id='dataset-radio',
                                        options=[
                                            {"label": "Previsão Prophet (dados_agrupados)", "value": "pdf"},
                                            {"label": "Previsão Futura Prophet", "value": "future"},
                                            {"label": "Dados Reais 2024 (pdf_2024_exportado)", "value": "2024"}
                                        ],
                                        value='pdf',
                                        labelStyle={'display': 'inline-block', 'margin-right': '20px'}
                                    )
                                ], className="mb-3"),
                                html.Div([
                                    html.Label("Selecione o ano:", className="fw-bold mb-2"),
                                    dcc.Dropdown(
                                        id='dropdown-ano',
                                        options=[{"label": str(ano), "value": ano} for ano in sorted(df_pdf['ANO'].unique())],
                                        value=df_pdf['ANO'].max(),
                                        clearable=False,
                                        style={"width": "100%"}
                                    )
                                ])
                            ])
                        ], className="shadow-sm border-0")
                    ], md=8, className="mx-auto")
                ], className="mb-4 justify-content-center"),
                # Card do gráfico
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                dcc.Graph(id='grafico-linha', config={"displayModeBar": False})
                            ])
                        ], className="shadow-lg border-0")
                    ], md=10, className="mx-auto")
                ]),
                # Botões de download
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            dbc.Button("Baixar dados_agrupados.csv", href="/baixar-dados?file=pdf", color="primary", className="me-2 mb-2", size="lg"),
                            dbc.Button("Baixar previsao_futura.csv", href="/baixar-dados?file=future", color="info", className="me-2 mb-2", size="lg"),
                            dbc.Button("Baixar pdf_2024_exportado.csv", href="/baixar-dados?file=2024", color="success", className="mb-2", size="lg")
                        ], className="text-center my-4")
                    ], md=10, className="mx-auto")
                ]),
                # Rodapé
                dbc.Row([
                    dbc.Col([
                        html.Footer([
                            html.Span("Desenvolvido por Alexandre, Carla, Khyra, Mario e Sabrina • Projeto Big Data", className="text-muted small")
                        ], className="text-center py-2")
                    ])
                ])
            ], style={"background": "#f8fafc", "minHeight": "100vh", "paddingBottom": "2rem"})
        ], fluid=True)
    else:
        # Tela de Login
        return dbc.Container([
            dcc.Location(id="url", refresh=True),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H2("Login", className="text-center mb-4 text-primary"),
                            dbc.Alert(id="login-alert", color="danger", is_open=False),
                            dbc.Input(id="login-username", placeholder="Usuário", type="text", className="mb-2"),
                            dbc.Input(id="login-password", placeholder="Senha", type="password", className="mb-2"),
                            dbc.Button("Entrar", id="login-button", color="primary", className="w-100 mb-2"),
                        ])
                    ], className="shadow-lg border-0 p-3")
                ], md=4, className="mx-auto mt-5")
            ])
        ], fluid=True)

def serve_layout():
    return dbc.Container([
        dcc.Location(id="url", refresh=True),
        # ÁREA DE LOGIN (sempre presente)
        html.Div([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H2("Login", className="text-center mb-4 text-primary"),
                            dbc.Alert(id="login-alert", color="danger", is_open=False),
                            dbc.Input(id="login-username", placeholder="Usuário", type="text", className="mb-2"),
                            dbc.Input(id="login-password", placeholder="Senha", type="password", className="mb-2"),
                            dbc.Button("Entrar", id="login-button", color="primary", className="w-100 mb-2"),
                        ])
                    ], className="shadow-lg border-0 p-3")
                ], md=4, className="mx-auto mt-5")
            ])
        ], id="login-area", style={"display": "block"}),
        # ÁREA DO DASHBOARD (sempre presente)
        html.Div([
            dbc.Row([
                dbc.Col([
                    html.H1([
                        html.I(className="bi bi-bar-chart-line-fill me-2 text-primary", style={"fontSize": "2rem"}),
                        "Dashboard de Casos de Dengue"
                    ], className="text-center my-4 fw-bold"),
                    dbc.Button("Logout", id="logout-button", color="secondary", className="float-end mb-2", size="sm"),
                ])
            ]),
            # Card de filtros
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Div([
                                html.Label("Escolha o conjunto de dados:", className="fw-bold mb-2"),
                                dcc.RadioItems(
                                    id='dataset-radio',
                                    options=[
                                        {"label": "Previsão Prophet (dados_agrupados)", "value": "pdf"},
                                        {"label": "Previsão Futura Prophet", "value": "future"},
                                        {"label": "Dados Reais 2024 (pdf_2024_exportado)", "value": "2024"}
                                    ],
                                    value='pdf',
                                    labelStyle={'display': 'inline-block', 'margin-right': '20px'}
                                )
                            ], className="mb-3"),
                            html.Div([
                                html.Label("Selecione o ano:", className="fw-bold mb-2"),
                                dcc.Dropdown(
                                    id='dropdown-ano',
                                    options=[{"label": str(ano), "value": ano} for ano in sorted(df_pdf['ANO'].unique())],
                                    value=df_pdf['ANO'].max(),
                                    clearable=False,
                                    style={"width": "100%"}
                                )
                            ])
                        ])
                    ], className="shadow-sm border-0")
                ], md=8, className="mx-auto")
            ], className="mb-4 justify-content-center"),
            # Card do gráfico
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id='grafico-linha', config={"displayModeBar": False})
                        ])
                    ], className="shadow-lg border-0")
                ], md=10, className="mx-auto")
            ]),
            # Botões de download
            dbc.Row([
                dbc.Col([
                    html.Div([
                        dbc.Button("Baixar dados_agrupados.csv", href="/baixar-dados?file=pdf", color="primary", className="me-2 mb-2", size="lg"),
                        dbc.Button("Baixar previsao_futura.csv", href="/baixar-dados?file=future", color="info", className="me-2 mb-2", size="lg"),
                        dbc.Button("Baixar pdf_2024_exportado.csv", href="/baixar-dados?file=2024", color="success", className="mb-2", size="lg")
                    ], className="text-center my-4")
                ], md=10, className="mx-auto")
            ]),
            # Rodapé
            dbc.Row([
                dbc.Col([
                    html.Footer([
                        html.Span("Desenvolvido por Alexandre, Carla, Khyra, Mario e Sabrina • Projeto Big Data", className="text-muted small")
                    ], className="text-center py-2")
                ])
            ])
        ], id="dashboard-area"),
    ], fluid=True)

app.layout = serve_layout

from dash.dependencies import Output, Input, State
from dash import callback_context
import flask

@app.callback(
    [
        Output("login-area", "style"),
        Output("dashboard-area", "style"),
        Output("login-alert", "is_open"),
        Output("login-alert", "children"),
    ],
    [
        Input("login-button", "n_clicks"),
        Input("logout-button", "n_clicks"),
    ],
    [
        State("login-username", "value"),
        State("login-password", "value"),
    ],
    prevent_initial_call=True
)
def login_logout_callback(login_click, logout_click, username, password):
    ctx = callback_context
    if not ctx.triggered:
        raise dash.exceptions.PreventUpdate
    trigger = ctx.triggered[0]["prop_id"].split(".")[0]
    if trigger == "login-button":
        if authenticate(username or "", password or ""):
            flask.session['logged_in'] = True
            log_user_access(username)
            # Mostra dashboard, esconde login
            return {"display": "none"}, {"display": "block"}, False, ""
        else:
            # Mostra login, esconde dashboard, alerta aberto
            return {"display": "block"}, {"display": "none"}, True, "Usuário ou senha inválidos."
    elif trigger == "logout-button":
        flask.session['logged_in'] = False
        # Mostra login, esconde dashboard
        return {"display": "block"}, {"display": "none"}, False, ""
    # fallback
    return {"display": "block"}, {"display": "none"}, False, ""

# Callback para atualizar o gráfico
from dash import callback_context

from dash import callback_context
from dash.dependencies import Output, Input

@app.callback(
    [Output('dropdown-ano', 'options'), Output('dropdown-ano', 'value'), Output('dropdown-ano', 'disabled')],
    [Input('dataset-radio', 'value')]
)
def atualizar_dropdown(dataset):
    if dataset == 'pdf':
        anos = sorted(df_pdf['ANO'].unique())
        return ([{"label": str(ano), "value": ano} for ano in anos], anos[-1], False)
    elif dataset == 'future':
        anos = sorted(df_forecast['ANO'].unique())
        return ([{"label": str(ano), "value": ano} for ano in anos], anos[0], False)
    else:
        # Desabilita o dropdown para dados reais
        return ([], None, True)

@app.callback(
    Output('grafico-linha', 'figure'),
    [Input('dataset-radio', 'value'),
     Input('dropdown-ano', 'value')]
)
def atualizar_grafico(dataset, ano):
    if dataset == 'pdf':
        if ano is None:
            ano = df_pdf['ANO'].max()
        df_filtrado = df_pdf[df_pdf['ANO'] == ano]
        fig = px.line(
            df_filtrado,
            x='ds', y='y', markers=True,
            title=f"Previsão Prophet - Casos de Dengue no Ano de {ano}",
            labels={'ds': 'Mês', 'y': 'Casos previstos'}
        )
        fig.update_traces(mode='lines+markers')
        fig.update_layout(xaxis_tickformat="%b/%Y", xaxis_title="Mês", yaxis_title="Nº de Casos")
        return fig
    elif dataset == 'future':
        if ano is None:
            ano = df_forecast['ANO'].min()
        df_futuro = df_forecast[df_forecast['ANO'] == ano]
        fig = px.line(
            df_futuro,
            x='ds', y='yhat', markers=True,
            title=f"Previsão Futura Prophet - Casos de Dengue no Ano de {ano}",
            labels={'ds': 'Mês', 'yhat': 'Casos previstos (futuro)'}
        )
        fig.update_traces(mode='lines+markers')
        fig.update_layout(xaxis_tickformat="%b/%Y", xaxis_title="Mês", yaxis_title="Nº de Casos")
        return fig
    else:
        fig = px.line(
            df_2024,
            x='DATA', y='count', markers=True,
            title="Casos Reais de Dengue em 2024",
            labels={'DATA': 'Mês', 'count': 'Casos reais'}
        )
        fig.update_traces(mode='lines+markers')
        fig.update_layout(xaxis_tickformat="%b/%Y", xaxis_title="Mês", yaxis_title="Nº de Casos")
        return fig

# Serviço para exportar CSV
from flask import send_file, request
@app.server.route("/baixar-dados")
def baixar_csv():
    file = request.args.get("file", "pdf")
    if file == "2024":
        caminho = os.path.join("data", "pdf_2024_exportado.csv")
        nome = "pdf_2024_exportado.csv"
    elif file == "future":
        caminho = os.path.join("data", "previsao_futura.csv")
        nome = "previsao_futura.csv"
    else:
        caminho = os.path.join("data", "dados_agrupados.csv")
        nome = "dados_agrupados.csv"
    return send_file(caminho,
                     mimetype='text/csv',
                     download_name=nome,
                     as_attachment=True)

# Roda o servidor
if __name__ == '__main__':
    app.run(debug=True)
