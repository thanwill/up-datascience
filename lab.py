import pandas as pd
import matplotlib.pyplot as plt

windowsPath = 'C:/Users/Aluno/Downloads/Vendas.csv'
macPath = '/Users/jonathan/Downloads/Vendas.csv'

try:
    # Carregue o arquivo CSV em um DataFrame
    data = pd.read_csv(macPath, sep=';', encoding='ISO-8859-1')
    
    # Substitua vírgulas por nada para remover separadores de milhares
    data['vendas'] = data['vendas'].str.replace(',', '').astype(float)
    
    # cria um dataframe com as vendas por ano 


except Exception as e:
    print(f"Um erro ocorreu: {e}") # Imprima uma mensagem de erro genérica



# Anotações
# 1. Calcule a média das vendas ao longo dos 4 anos e discuta como ela representa o valor central das vendasCalcule a média das vendas ao longo dos 4 anos e discuta como ela representa o valor central das vendas
