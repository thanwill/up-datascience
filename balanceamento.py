import pandas as pd


header = ['Season','Age','Childish_diseases','Accident','Surgical_intervention','High_fevers','alcohol_consumption','Smoking','hours_sitting','Output']
fertility = pd.read_csv('C:\\Users\\Aluno\\Downloads\\fertility_Diagnosis.txt', names=header) # lê o arquivo csv

print(fertility.head()) # print as 5 primeiras linhas do dataset

# imprime a contagem de Output para cada valor de Output
print(fertility['Output'].value_counts())