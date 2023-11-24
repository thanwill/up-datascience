import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

try:

    # limpa a tela do terminal
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    macPath = '/Users/jonathan/Downloads/breast-cancer.csv'
    df = pd.read_csv(macPath, sep=',')

    # print("\nDados originais")
    # print(df.head())

    # Crie uma cópia do DataFrame
    df_normalized = df.copy()

    # Remova a coluna 'Class' e armazene-a em uma variável separada
    Class = df_normalized['Class']
    df_normalized = df_normalized.drop(['Class'], axis=1)

    # Converta variáveis categóricas em variáveis dummy/indicadoras
    df_normalized = pd.get_dummies(df_normalized)

    # print("\nDados normalizados")
    # print(df_normalized.head())

    # Crie o normalizador
    scaler = MinMaxScaler()

    # Aplique o normalizador ao DataFrame
    df_normalized[df_normalized.columns] = scaler.fit_transform(df_normalized[df_normalized.columns])

    # Adicione a coluna 'Class' de volta ao DataFrame
    df_normalized['Class'] = Class

    # print("\nDados normalizados e com a coluna 'Class' de volta")
    # print(df_normalized.head())

    print("Linha 41: Dados normalizados e com a coluna 'Class' de volta")

    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier

    # Separe os dados em recursos (X) e alvo (y)
    X = df_normalized.drop('Class', axis=1)
    y = df_normalized['Class']

    # Divida os dados em conjuntos de treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Crie uma instância da classe DecisionTreeClassifier
    tree = DecisionTreeClassifier()

    # Treine o modelo
    tree.fit(X_train, y_train)
    print("Linha 58: Modelo treinado")

    # Salve o modelo
    import pickle
    pickle.dump(tree, open('modelo.sav', 'wb'))
    print("Linha 66: Modelo salvo")

    from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

    # Use o modelo treinado para fazer previsões no conjunto de teste
    y_pred = tree.predict(X_test)

    # Gere a matriz de confusão
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=tree.classes_)
    disp.plot()

    # Salve a matriz de confusão    
    plt.savefig('matriz_confusao.png')

    # Exiba a matriz de confusão
    plt.show()    



























except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão de leitura')
except Exception as erro:
    print('Erro desconhecido: ', erro)
