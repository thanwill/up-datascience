from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pickle 
from pickle import load
# importa o normalizador pip install scikit_learn

file = 'C:/Users/Aluno/Downloads/dados_normalizar.csv'

try:

    # 1. Ler o arquivo
    # 2. Segmentar os dados em escalares e categóricos
    # 3. Normalizar os dados
    # 4. Recompor os dados normalizados em um dataframe
    # 5. Salvar o normalizador para uso posterior (pickle)
    # 6. Normalizar os dados de uma nova instância desconhecida (não vista pelo modelo)
    # Mensagem para o commit: Normalização de dados com MinMaxScaler e pickle 


    print('\033c') # limpa a tela
        
    serie = pd.read_csv(file, sep=';', encoding='latin1', usecols=['idade', 'altura', 'Peso', 'sexo']) # lê o arquivo csv

    serie_numerica = serie[['idade', 'altura', 'Peso']] # segmenta os dados em escalares
    serie_categorica = serie[['sexo']] # segmenta os dados em categóricos

    # normaliza os dados
    serie_normalizada = (serie_numerica - serie_numerica.min()) / (serie_numerica.max() - serie_numerica.min())
    # normaliza os dados categorias sexo
    serie_categorica_normalizada = pd.get_dummies(data = serie_categorica, prefix_sep='_') # argumentos: dados, separador de prefix
    
    normalizador = MinMaxScaler() # cria o objeto normalizador
    modelo = normalizador.fit(serie_numerica) # treina o modelo com os dados
    serie_normalizada_sklearn = modelo.fit_transform(serie_numerica) # aplica a normalização aos dados


    # recompor dados normalizados em um dataframe
    dados_normalizados = pd.DataFrame(serie_normalizada_sklearn, columns=['idade', 'altura', 'Peso'])
    dados_normalizados['sexo_F'] = serie_categorica_normalizada['sexo_F'] # adiciona a coluna sexo_F
    dados_normalizados['sexo_M'] = serie_categorica_normalizada['sexo_M'] # adiciona a coluna sexo_M

    # salvar o normalizador para uso posteriror
    pickle.dump(modelo, open('normalizador.pkl', 'wb')) # salva o modelo no arquivo normalizador.pkl (wb = write binary)   

    # carrega o normalizador
    normalizador = load(open('normalizador.pkl', 'rb')) # rb = read binary

    paciente = [[40, 1.70, 70]] # dados de um novo paciente
    paciente_normalizado = normalizador.transform(paciente) # aplica a normalização aos dados
    print(paciente_normalizado) # imprime os dados normalizados


except Exception as e:
    print(f"Um erro ocorreu: {e}")