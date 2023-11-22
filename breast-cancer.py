import pandas as pd
from imblearn.over_sampling import SMOTE # pip install imblearn


# normalizar, balancear e segmentar os df, treinar o modelo e avaliar a acurácia do modelo

try:
    macPath = '/Users/jonathan/Downloads/breast-cancer.csv'
    df = pd.read_csv(macPath, sep=',')
    
    # segumenta os df de atributos e classes
    classes = df['Class'] 
    atributos = df.drop('Class', axis=1)

    # normaliza os df de atributos e classes usando o get_dummies
    atributos_balanceados = pd.get_dummies(atributos)
    classes_balanceadas = pd.get_dummies(classes)
    

    # Balanceamento de df usando o SMOTE
    resampler = SMOTE()
    atributos_balanceados, classes_balanceadas = resampler.fit_resample(atributos_balanceados, classes_balanceadas)

    print(df.head())
    # verifica a frequencia das classes balanceadas
    from collections import Counter
    print(sorted(Counter(classes_balanceadas).items()))






except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão de leitura')
except Exception as erro:
    print('Erro desconhecido: ', erro)
