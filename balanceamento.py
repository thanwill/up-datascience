import pandas as pd
from imblearn.over_sampling import SMOTE

from pprint import pprint
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

#---------------------------------------------------

# leitura do arquivo csv e contagem de valores da coluna 'Output' (variável alvo) 

header = ['Season','Age','Childish_diseases','Accident','Surgical_intervention','High_fevers','alcohol_consumption','Smoking','hours_sitting','Output']
fertility = pd.read_csv('C:\\Users\\Aluno\\Downloads\\fertility_Diagnosis.txt', names=header) # lê o arquivo csv
print(fertility['Output'].value_counts())

#---------------------------------------------------

# balanceamento dos dados com SMOTE (Synthetic Minority Oversampling Technique) 
# -> Holdout : técnica comum de validação de modelos de machine learning

dados_classes = fertility['Output']
dados_atributos = fertility.drop('Output', axis=1)

# ---------------------------------------------------

# divisão dos dados em treino e teste (70% e 30%) respectivamente
dados_atributos_treino, dados_atributos_teste, dados_classes_treino, dados_classes_teste = train_test_split(dados_atributos, dados_classes, test_size=0.3, random_state=1)





