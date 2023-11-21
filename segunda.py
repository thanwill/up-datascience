import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.arima.model import ARIMA


df = pd.DataFrame( pd.read_csv('vendas_alterada.csv', sep=',') )

# Divida os dados de vendas em quatro quartis com variacoes de 0.25
primeiro_quartil = df['Vendas'].quantile(0.25)
segundo_quartil = df['Vendas'].quantile(0.50)
terceiro_quartil = df['Vendas'].quantile(0.75)
quarto_quartil = df['Vendas'].quantile(1)

# Crie uma nova coluna chamada Quartil e atribua valores de 1 a 4 para cada linha
for index, row in df.iterrows():
    if row['Vendas'] <= primeiro_quartil:
        df.loc[index, 'Quartil'] = 1
    elif row['Vendas'] <= segundo_quartil:
        df.loc[index, 'Quartil'] = 2
    elif row['Vendas'] <= terceiro_quartil:
        df.loc[index, 'Quartil'] = 3
    else:
        df.loc[index, 'Quartil'] = 4

# Imprima os valores dos quartis
print(f"Primeiro quartil: {primeiro_quartil}")
print(f"Segundo quartil: {segundo_quartil}")
print(f"Terceiro quartil: {terceiro_quartil}")
print(f"Quarto quartil: {quarto_quartil}")

# Criando um gráfico de caixa
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 7))
plt.boxplot(df['Vendas'])
plt.title('Vendas')
plt.ylabel('Vendas')
plt.xlabel('Vendas')
#plt.show()

# calcula os intervalos interquartil (Quadrantes) para as vendas
import numpy as np
q1 = np.percentile(df['Vendas'], 25)
q3 = np.percentile(df['Vendas'], 75)
iqr = q3 - q1
print(f"Primeiro quartil: {q1}")
print(f"Terceiro quartil: {q3}")
print(f"Intervalo interquartil: {round(iqr, 2)}")

# intervalos máximo e mínimo
minimo = df['Vendas'].min()
maximo = df['Vendas'].max()
print(f"Valor mínimo: {minimo}")
print(f"Valor máximo: {maximo}")

# Criando o modelo
modelo = ExponentialSmoothing(df['Vendas'], trend='mul', seasonal='mul', seasonal_periods=12).fit()
# Criando previsões
previsoes = modelo.forecast(12*5) # 12 meses

print(f"Previsões: \n{previsoes}")

# Plotando o gráfico

plt.figure(figsize=(10, 7))
plt.plot(df['Vendas'], label='Vendas')
plt.plot(previsoes, label='Previsões')
plt.title('Vendas')
plt.ylabel('Vendas')
plt.xlabel('Vendas')
plt.legend(loc='best')
#plt.show()

ema = sum(abs(previsao - real) for previsao, real in zip(previsoes, df['Vendas'])) / len(previsoes)
print(f"Erro médio absoluto: {round(ema, 2)}")

epma = sum(abs((previsao - real) / real) for previsao, real in zip(previsoes, df['Vendas'])) / len(previsoes)
print(f"Erro médio percentual absoluto: {round(epma, 2)}")

# Criando um índice temporal mensal (assumindo que começa em janeiro de 2024)
datas = pd.date_range(start='2024-01-01', periods=len(df['Vendas']), freq='M')

# Criando um DataFrame com datas e vendas
dataframe = pd.DataFrame({'Data': datas, 'Vendas': df['Vendas']})
dataframe.set_index('Data', inplace=True)

# Ajustando o modelo ARIMA aos dados de vendas
modelo_arima = ARIMA(dataframe['Vendas'], order=(5, 1, 0))  # Parâmetros do modelo ARIMA (p, d, q)
resultado_arima = modelo_arima.fit()

# Previsão para os próximos cinco anos (2028 a 2032)
previsao_5_anos = resultado_arima.forecast(steps=60)  # 60 meses para os próximos cinco anos

# Gerando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(dataframe.index, dataframe['Vendas'], label='Vendas Históricas')
plt.plot(pd.date_range(start='2028-01-01', periods=60, freq='M'), previsao_5_anos, label='Previsão 2028-2032', linestyle='dashed', color='red')
plt.title('Previsão de Vendas para os Próximos Cinco Anos (2028 a 2032)')
plt.xlabel('Data')
plt.ylabel('Vendas')
plt.legend()
plt.show()