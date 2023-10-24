from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

import pandas as pd
import numpy as np

file = 'C:/Users/Aluno/Downloads/Vendas.csv'

try:
    serie = pd.read_csv(file, sep=';', encoding='latin1', usecols=['Vendas'])
    # Limpe a coluna 'Vendas (em unidades monetárias)' removendo vírgulas e convertendo para numérico
    serie['Vendas'] = serie['Vendas'].str.replace(',', '.').astype(float)

    
    # calcula a média das vendas ao longo dos 4 anos  (2024, 2025, 2026, 2027)
    media = serie['Vendas'].mean()
    media = round(media, 2)
    print('Média', media)

   

except Exception as e:
    print(f"Um erro ocorreu: {e}")





