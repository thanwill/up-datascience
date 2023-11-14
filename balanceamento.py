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

# print(dados_classes_teste)

tree = DecisionTreeClassifier()
fertility_balanceado = tree.fit(dados_atributos_treino, dados_classes_treino)

classe_predita = fertility_balanceado.predict(dados_atributos_teste)

# print(classe_predita)

# ---------------------------------------------------

# Matriz de contingência / Confusion Matrix (TP, FP, FN, TN)

import matplotlib.pyplot as plt
import sklearn
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

matriz_confusao = confusion_matrix(dados_classes_teste, classe_predita)
disp = ConfusionMatrixDisplay(confusion_matrix=matriz_confusao, display_labels=fertility_balanceado.classes_)
disp.plot()
plt.show()





