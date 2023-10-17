import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from statsmodels.tsa.seasonal import seasonal_decompose # importa o método de decomposição sazonal pip install statsmodels


#### CONFIGURAÇÃO ####

# root = Tk()
# root.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
filename = 'C:/Users/Aluno/Downloads/airline-passengers.csv' # caminho do arquivo
df = pd.read_csv(filename, sep=',', parse_dates=True, index_col='Month' ) # lê o arquivo csv e define a coluna Month como índice
#f = open('path.txt', 'w') # abre o arquivo path.txt em modo de escrita
#f.write(root.filename) # escreve o caminho do arquivo no arquivo path.txt
#f.close() # fecha o arquivo path.txt

#### CONFIGURAÇÃO ####
 
result = seasonal_decompose(df['Passengers'], model='multiplicative') # cria a decomposição sazonal multiplicativa
# result = seasonal_decompose(df['Passengers'], model='additional') # cria a decomposição sazonal aditiva
# result.plot() 
# df.plot() # cria o gráfico

# Definir a frequencia  do ínidce como mensal
df.index.freq = 'MS' # MS: mensal, AS: anual, W: semanal, D: diário
meses = 12
alpha = 1/( 2 * meses) # suavização simples: formula do alpha alpha = 1/(2*m) aonde m é o número de períodos

# Aplicar o método de Holt-Winters: Simple Exponential Smoothing
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

model = SimpleExpSmoothing(df['Passengers']) # cria o modelo
fitted_model = model.fit(smoothing_level=alpha, optimized=False, use_brute=True) # ajusta o modelo fit( parametro de suavização, otimização, uso de força bruta)
df['SES12'] = fitted_model.fittedvalues.shift(-1) # cria a coluna SES12 e atribui os valores ajustados pelo modelo
# df.plot() # cria o gráfico

# exponencial duplo aditivo e multiplicativo
from statsmodels.tsa.holtwinters import ExponentialSmoothing

df['HWES2_ADD'] = ExponentialSmoothing(df['Passengers'], trend='add').fit().fittedvalues
df['HWES2_MUL'] = ExponentialSmoothing(df['Passengers'], trend='mul').fit().fittedvalues
df['e'] = df['Passengers'] - df['HWES2_ADD'] # cria a coluna e e atribui a diferença entre os valores reais e os valores ajustados pelo modelo
df[['Passengers', 'HWES2_ADD', 'HWES2_MUL']].plot(title='Holt Winters Double Exponential Smoothing: ') # cria o gráfico
# cria o grafico com o valor real, o valor ajustado pelo modelo e o erro
df[['Passengers', 'HWES2_ADD', 'e']].plot(subplots=True, figsize=(15,8)) # cria o gráfico


plt.show() # mostra o gráfico



