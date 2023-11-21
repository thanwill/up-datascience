import pandas as pd

df = pd.DataFrame( pd.read_csv('/Users/jonathan/Downloads/Vendas.csv', sep=';') )
df.rename(columns={df.columns[-1]: 'Vendas'}, inplace=True)
vendas_por_ano = df.groupby('Ano').sum()
print(vendas_por_ano['Vendas'])


# MÉDIA
media_vendas_por_ano = vendas_por_ano['Vendas'].mean()
print(f"Média de vendas por ano: {round(media_vendas_por_ano, 2)}")

# MEDIANA
mediana_vendas_por_ano = vendas_por_ano['Vendas'].median()
print(f"Mediana de vendas por ano: {round(mediana_vendas_por_ano, 2)}")

# Plotando gráfico
import matplotlib.pyplot as plt
plt.plot(vendas_por_ano.index, vendas_por_ano['Vendas'], color='blue', marker='o')
plt.title('Vendas por ano')
plt.xlabel('Ano')
plt.ylabel('Vendas')
plt.grid(True)

# indica o ponto da média e da mediana
plt.axhline(media_vendas_por_ano, color='red', linestyle='--')
plt.axhline(mediana_vendas_por_ano, color='green', linestyle='--')


