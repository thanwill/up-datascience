import pandas as pd
import matplotlib.pyplot as plt
import os
windowsPath = 'C:/Users/Aluno/Downloads/Vendas.csv'
macPath = '/Users/jonathan/Downloads/Vendas.csv'

try:

    
    df = pd.DataFrame( pd.read_csv(macPath, sep=';') )
    df.rename(columns={df.columns[-1]: 'Vendas'}, inplace=True)
    vendas_por_ano = df.groupby('Ano').sum()
    print(vendas_por_ano['Vendas'])


    # define a média de vendas por ano
    media_vendas_por_ano = vendas_por_ano['Vendas'].mean()
    for index, row in vendas_por_ano.iterrows():
        if row['Vendas'] > media_vendas_por_ano:
            print(index, row['Vendas'])

    # soma de vendas por Ano
    vendas_por_Ano = df.groupby('Ano').sum()        
    #print(vendas_por_Ano['vendas'])

    # soma de vendas por Mes
    vendas_por_Mes = df.groupby('Mes').sum()
    #print(vendas_por_Mes['vendas'])
    
    # # cria um gráfico de barras com as vendas por Ano com a média
    # plt.bar(vendas_por_Ano.index, vendas_por_Ano['vendas'])
    # plt.axhline(media_vendas, color='red', linestyle='--')
    # plt.axhline(mediana_vendas, color='yellow', linestyle='--')
    # plt.title('Vendas por Ano')

    # Calcule a variância e o desvio padrão das vendas de todos os Meses
    variancia_vendas = df['Vendas'].var()
    desvio_padrao_vendas = df['Vendas'].std()

    # cria um for para calcular a variância e o desvio padrão das vendas por mês e adiciona o valor em uma nova coluna no dfframe
    for index, row in df.iterrows():
        #print(row['Mes'], row['vendas'])
        #df.loc[index, 'variancia'] = df[df['Mes'] == row['Mes']]['vendas'].var()

        # cria a coluna variancia populacional
        df.loc[index, 'var_populacional'] = df[df['Mes'] == row['Mes']]['Vendas'].var(ddof=0)
        
        # cria a coluna para desvio padrão populacional
        df.loc[index, 'desvio_padrao'] = df[df['Mes'] == row['Mes']]['Vendas'].std(ddof=0)
    
    # exibe o dfframe com as novas colunas e o Mes ordenado
    df = df.sort_values(by=['Mes'])

    # exibe as linhas do dfframe para o mês com a maior venda e o mês com a menor venda e exporta para um arquivo html
    # print(df[df['vendas'] == df['vendas'].max()])
    # print(df[df['vendas'] == df['vendas'].min()])

    # Divida os dados de vendas em três quartis
    primeiro_quartil = df['Vendas'].quantile(0.25)
    segundo_quartil = df['Vendas'].quantile(0.50)
    terceiro_quartil = df['Vendas'].quantile(0.75)

    # Divida os dados de vendas em três quartis
    primeiro_quartil = df['Vendas'].quantile(0.25)
    segundo_quartil = df['Vendas'].quantile(0.50)
    terceiro_quartil = df['Vendas'].quantile(0.75)

    # Imprima os valores dos quartis
    print('Primeiro quartil:', primeiro_quartil)
    print('Segundo quartil:', segundo_quartil)
    print('Terceiro quartil:', terceiro_quartil)

    # Calcule os intervalos interquartil (Quadrantes) para as vendas 
    iqr = terceiro_quartil - primeiro_quartil

    # plota um grático de Diagrama de extremos e quartis (Boxplot) exibindo os dados de vendas, o primeiro quartil, o segundo quartil e o terceiro quartil e o max e min 
    plt.boxplot(df['Vendas'], showmeans=True)
    plt.axhline(primeiro_quartil, color='grey', linestyle='--')
    plt.axhline(segundo_quartil, color='grey', linestyle='--')
    plt.axhline(terceiro_quartil, color='grey', linestyle='--')
    plt.title('Quartis de vendas')
    

    # Calcule os limites inferior e superior
    limite_inferior = primeiro_quartil - (1.5 * iqr)
    limite_superior = terceiro_quartil + (1.5 * iqr)

    # cria uma legenda para o gráfico
    plt.legend(['Vendas', 'Limite inferior', 'Limite superior'])
    
    # plota um gráfico com os limites inferior e superior e os dados de venda
    plt.plot(df['Mes'], df['vendas'])
    plt.axhline(limite_inferior, color='red', linestyle='--')
    plt.axhline(limite_superior, color='blue', linestyle='--')
    plt.title('Vendas')
    

    # exporta o dfframe para um arquivo csv
    df.to_csv('vendas_tratamento.csv', index=False)


except Exception as e:
    print(f"Um erro ocorreu: {e}") # Imprima uma mensagem de erro genérica



# Anotações
# 1. Calcule a média das vendas ao longo dos 4 Anos e discuta como ela representa o valor central das vendas