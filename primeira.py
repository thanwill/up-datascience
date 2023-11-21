import pandas as pd

df = pd.DataFrame( pd.read_csv('/Users/jonathan/Downloads/Vendas.csv', sep=';') )
df.rename(columns={df.columns[-1]: 'Vendas'}, inplace=True)
em_anos = df.groupby('Ano').sum()
em_meses = df.groupby('Mes').sum()

vendas = df['Vendas'].sum()
print(f"Total de vendas: {vendas}")

media_vendas = df['Vendas'].mean()
print(f"Média de vendas: {round(media_vendas, 2)}")


# MÉDIA
media_em_anos = em_anos['Vendas'].mean()
print(f"Média de vendas por ano: {round(media_em_anos, 2)}")

# MEDIANA
mediana_em_anos = em_anos['Vendas'].median()
print(f"Mediana de vendas por ano: {round(mediana_em_anos, 2)}")

# Plotando gráfico
import matplotlib.pyplot as plt
plt.plot(em_anos.index, em_anos['Vendas'], color='blue', marker='o')
plt.title('Vendas por ano')
plt.xlabel('Ano')
plt.ylabel('Vendas')
plt.grid(True)

# indica o ponto da média e da mediana
plt.axhline(media_em_anos, color='red', linestyle='--')
plt.axhline(mediana_em_anos, color='green', linestyle='--')
# plt.show()

print(em_meses)
# MEDIA: meses
media_em_meses = em_meses['Vendas'].mean()
print(f"Média de vendas por mês: {round(media_em_meses, 2)}")

# MEDIANA: meses
mediana_em_meses = em_meses['Vendas'].median()
print(f"Mediana de vendas por mês: {round(mediana_em_meses, 2)}")

# DESVIO PADRÃO: 
desvio_padrao_em_meses = em_meses['Vendas'].std()
print(f"Desvio padrão de vendas por mês: {round(desvio_padrao_em_meses, 2)}")

# VARIANCIA: meses
variancia_em_meses = em_meses['Vendas'].var()
print(f"Variância de vendas por mês: {round(variancia_em_meses, 2)}")

for index, row in df.iterrows():
    df.loc[index, 'variancia'] = df[df['Mes'] == row['Mes']]['Vendas'].var(ddof=0)
    df.loc[index, 'desvio_padrao'] = df[df['Mes'] == row['Mes']]['Vendas'].std(ddof=0)

df = df.sort_values(by=['Mes'])

#mês com a maior venda e o mês com a menor venda
print("Maior venda:")
print(df[df['Vendas'] == df['Vendas'].max()])
print("Menor venda:")
print(df[df['Vendas'] == df['Vendas'].min()])

#df.to_html('vendas.html', index=False)
# exporta para um arquivo csv
df.to_csv('vendas_alterada.csv', index=False)



