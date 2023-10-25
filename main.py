import pandas as pd
import matplotlib.pyplot as plt
import os
windowsPath = 'C:/Users/Aluno/Downloads/Vendas.csv'
macPath = '/Users/jonathan/Downloads/Vendas.csv'

try:

    # limpa os dados do console
    os.system('cls' if os.name == 'nt' else 'clear')


    # Carregue o arquivo CSV em um DataFrame
    data = pd.read_csv(macPath, sep=';', encoding='ISO-8859-1')

    # Substitua vírgulas por nada para remover separadores de milhares
    data['vendas'] = data['vendas'].str.replace(',', '.').astype(float)
    
    df = pd.DataFrame(data)    
    
    media_vendas = data['vendas'].mean() # Calcule a média das vendas
    media_vendas = round(media_vendas, 2) # Arredonde o valor para duas casas decimais
    mediana_vendas = data['vendas'].median() # Calcule a mediana das vendas

    print('Média de vendas:', media_vendas) # Imprima o valor da média
    print('Mediana de vendas:', mediana_vendas) # Imprima o valor da mediana

    # soma de vendas por ano
    vendas_por_ano = data.groupby('ano').sum()        
    #print(vendas_por_ano['vendas'])

    # soma de vendas por mes
    vendas_por_mes = data.groupby('mes').sum()
    #print(vendas_por_mes['vendas'])
    
    # # cria um gráfico de barras com as vendas por ano com a média
    # plt.bar(vendas_por_ano.index, vendas_por_ano['vendas'])
    # plt.axhline(media_vendas, color='red', linestyle='--')
    # plt.axhline(mediana_vendas, color='yellow', linestyle='--')
    # plt.title('Vendas por ano')

    # Calcule a variância e o desvio padrão das vendas de todos os meses
    variancia_vendas = data['vendas'].var()
    desvio_padrao_vendas = data['vendas'].std()

    # cria um for para calcular a variância e o desvio padrão das vendas por mês e adiciona o valor em uma nova coluna no dataframe
    for index, row in df.iterrows():
        #print(row['mes'], row['vendas'])
        #df.loc[index, 'variancia'] = data[data['mes'] == row['mes']]['vendas'].var()

        # cria a coluna variancia populacional
        df.loc[index, 'var_populacional'] = data[data['mes'] == row['mes']]['vendas'].var(ddof=0)
        
        # cria a coluna para desvio padrão populacional
        df.loc[index, 'desvio_padrao'] = data[data['mes'] == row['mes']]['vendas'].std(ddof=0)
    
    # exibe o dataframe com as novas colunas e o mes ordenado
    df = df.sort_values(by=['mes'])



    

    # exporta o dataframe para um arquivo csv
    df.to_csv('vendas_tratamento.csv', index=False)


except Exception as e:
    print(f"Um erro ocorreu: {e}") # Imprima uma mensagem de erro genérica



# Anotações
# 1. Calcule a média das vendas ao longo dos 4 anos e discuta como ela representa o valor central das vendas