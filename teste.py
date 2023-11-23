import pandas as pd
from sklearn.preprocessing import MinMaxScaler

try:

    # limpa a tela do terminal
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    macPath = '/Users/jonathan/Downloads/breast-cancer.csv'
    df = pd.read_csv(macPath, sep=',')

    print("\nDados originais")
    print(df.head())

    # Crie uma cópia do DataFrame
    df_normalized = df.copy()

    # Remova a coluna 'Class' e armazene-a em uma variável separada
    Class = df_normalized['Class']
    df_normalized = df_normalized.drop(['Class'], axis=1)

    # Converta variáveis categóricas em variáveis dummy/indicadoras
    df_normalized = pd.get_dummies(df_normalized)

    print("\nDados normalizados")
    print(df_normalized.head())

    # Crie o normalizador
    scaler = MinMaxScaler()

    # Aplique o normalizador ao DataFrame
    df_normalized[df_normalized.columns] = scaler.fit_transform(df_normalized[df_normalized.columns])

    # Adicione a coluna 'Class' de volta ao DataFrame
    df_normalized['Class'] = Class

    print("\nDados normalizados e com a coluna 'Class' de volta")
    print(df_normalized.head())     



























except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão de leitura')
except Exception as erro:
    print('Erro desconhecido: ', erro)
