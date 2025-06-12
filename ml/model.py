from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

# Supondo que o dados_tratados.csv já tenha colunas: 'ano', 'casos'
df = pd.read_csv("data/dados_tratados.csv")
X = df[["ano"]]
y = df["casos"]
model = LinearRegression()
model.fit(X, y)
print("Previsão para 2025:", model.predict([[2025]]))