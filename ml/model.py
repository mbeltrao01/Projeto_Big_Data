import pandas as pd
from prophet import Prophet

# Carregar o dataset completo com histórico (e não só 2024)
pdf = pd.read_csv('notebooks/pdf_exportado.csv')  # <--- esse é o histórico completo
pdf['ds'] = pd.to_datetime(pdf['ds'])

# Treinar o modelo com dados históricos completos
modelo = Prophet()
modelo.fit(pdf)

# Prever os próximos 12 meses
future = modelo.make_future_dataframe(periods=12, freq='M')
forecast = modelo.predict(future)

# Salvar previsões
forecast[['ds', 'yhat']].rename(columns={'yhat': 'y'}).to_csv('notebooks/previsao_2025.csv', index=False, encoding='utf-8')

print('Previsão gerada com base no histórico completo e salva como notebooks/previsao_2025.csv')
