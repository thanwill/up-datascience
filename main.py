import pandas as pd

windowsPath = 'C:/Users/Aluno/Downloads/Vendas.csv'
macPath = '/Users/jonathan/Downloads/Vendas.csv'

try:
    # Carregue o arquivo CSV em um DataFrame
    data = pd.read_csv(macPath, sep=';', encoding='ISO-8859-1')
     
    # Substitua vírgulas por nada para remover separadores de milhares
    data['vendas'] = data['vendas'].str.replace(',', '').astype(float)
    
    media_vendas = data['vendas'].mean() # Calcule a média das vendas
    media_vendas = round(media_vendas, 2) # Arredonde o valor para duas casas decimais
    mediana_vendas = data['vendas'].median() # Calcule a mediana das vendas

    print('Média de vendas:', media_vendas) # Imprima o valor da média
    print('Mediana de vendas:', mediana_vendas) # Imprima o valor da mediana

except Exception as e:
    print(f"Um erro ocorreu: {e}") # Imprima uma mensagem de erro genérica
