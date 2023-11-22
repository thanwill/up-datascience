import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.arima.model import ARIMA


df = pd.DataFrame( pd.read_csv('vendas_alterada.csv', sep=',') )
# Mapeamento dos nomes dos meses para os números dos meses
meses = {'Janeiro': 1, 'Fevereiro': 2, 'Marco': 3, 'Abril': 4, 'Maio': 5, 'Junho': 6, 'Julho': 7, 'Agosto': 8, 'Setembro': 9, 'Outubro': 10, 'Novembro': 11, 'Dezembro': 12}
# Aplica o mapeamento à coluna 'Mes'
df['Mes'] = df['Mes'].map(meses).astype(int)

# Crie uma coluna 'Data' concatenando as colunas 'Ano' e 'Mes' e o dia 1
df['Data'] = pd.to_datetime(df['Ano'].astype(str) + '-' + df['Mes'].astype(str) + '-' + str(1))
# Certifique-se de ordenar o DataFrame pela coluna de data, se necessário
df = df.sort_values('Data')
# Defina 'Data' como o índice do DataFrame
df.set_index('Data', inplace=True)
# Defina a frequência do índice para mensal
df = df.asfreq('MS')

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


# Criando um gráfico de caixa
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 7))
plt.boxplot(df['Vendas'])
plt.title('Vendas')
plt.ylabel('Vendas')
plt.xlabel('Vendas')
##plt.show()

# calcula os intervalos interquartil (Quadrantes) para as vendas
import numpy as np
q1 = np.percentile(df['Vendas'], 25)
q3 = np.percentile(df['Vendas'], 75)
iqr = q3 - q1


# intervalos máximo e mínimo
minimo = df['Vendas'].min()
maximo = df['Vendas'].max()


# Criando o modelo
modelo = ExponentialSmoothing(df['Vendas'], trend='mul', seasonal='mul', seasonal_periods=12).fit()
# Criando previsões
previsoes = modelo.forecast(9) # 12 meses
print("\nPrevisões de vendas para os próximos 9 meses:\n")
print(previsoes)


plt.figure(figsize=(10, 7))
plt.plot(df['Vendas'], label='Vendas')
plt.plot(previsoes, label='Previsões')
plt.title('Vendas')
plt.ylabel('Vendas')
plt.xlabel('Vendas')
plt.legend(loc='best')
##plt.show()

ema = sum(abs(previsao - real) for previsao, real in zip(previsoes, df['Vendas'])) / len(previsoes)
epma = sum(abs((previsao - real) / real) for previsao, real in zip(previsoes, df['Vendas'])) / len(previsoes)

# cria uma estrtura para imprimir os dados
print("\n")
print(f"Vendas: {round(df['Vendas'].sum(), 2)}")
print(f"Vendas média: {round(df['Vendas'].mean(), 2)}")
print(f"Vendas mediana: {round(df['Vendas'].median(), 2)}")
print(f"Vendas variância: {round(df['Vendas'].var(), 2)}")
print(f"Vendas desvio padrão: {round(df['Vendas'].std(), 2)}")

print("\n")

print(f"Primeiro quartil: {primeiro_quartil}")
print(f"Segundo quartil: {segundo_quartil}")
print(f"Terceiro quartil: {terceiro_quartil}")

print("\n")
print(f"Intervalo interquartil: {round(iqr, 2)}")
print("\n")
print(f"Valor mínimo: {minimo}")
print(f"Valor máximo: {maximo}")
print("\n")
print(f"Erro médio absoluto: {round(ema, 2)}")
print(f"Erro médio percentual absoluto: {round(epma, 2)}")

# Criando um índice temporal mensal (assumindo que começa em janeiro de 2024)
dataframe = pd.DataFrame({'Vendas': df['Vendas']}, index=pd.date_range(start='2024-01-01', periods=len(df), freq='MS'))
# Criando o modelo
modelo_arina = ARIMA(dataframe, order=(1, 1, 1))

# Treinando o modelo
modelo_arina_fit = modelo_arina.fit()

# Criando previsões para os próximos 5 anos (60 meses)
previsoes_arima = modelo_arina_fit.forecast(steps=12*5)[0]


plt.figure(figsize=(10, 7))
plt.plot(df['Vendas'], label='Vendas')
plt.plot(previsoes_arima, label='Previsões')
plt.title('Vendas')
plt.ylabel('Vendas')
plt.xlabel('Anos')
plt.legend(loc='best')
plt.show()

