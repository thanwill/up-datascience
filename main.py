import pandas as pd
import matplotlib.pyplot as plt

windowsPath = 'C:/Users/Aluno/Downloads/Vendas.csv'
macPath = '/Users/jonathan/Downloads/Vendas.csv'

try:
    # Carregue o arquivo CSV em um DataFrame
    data = pd.read_csv(macPath, sep=';', encoding='ISO-8859-1')

    # Substitua vírgulas por nada para remover separadores de milhares
    data['vendas'] = data['vendas'].str.replace(',', '.').astype(float)
    
    df = pd.DataFrame(data)
    print(df)
    
    media_vendas = data['vendas'].mean() # Calcule a média das vendas
    media_vendas = round(media_vendas, 2) # Arredonde o valor para duas casas decimais
    mediana_vendas = data['vendas'].median() # Calcule a mediana das vendas

    print('Média de vendas:', media_vendas) # Imprima o valor da média
    print('Mediana de vendas:', mediana_vendas) # Imprima o valor da mediana

    # soma de vendas por ano
    vendas_por_ano = data.groupby('ano').sum()        
    print(vendas_por_ano['vendas'])

    # soma de vendas por mes
    vendas_por_mes = data.groupby('mes').sum()
    print(vendas_por_mes['vendas'])
    

except Exception as e:
    print(f"Um erro ocorreu: {e}") # Imprima uma mensagem de erro genérica



# Anotações
# 1. Calcule a média das vendas ao longo dos 4 anos e discuta como ela representa o valor central das vendas