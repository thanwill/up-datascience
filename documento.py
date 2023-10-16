import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from statsmodels.tsa.seasonal import seasonal_decompose # importa o método de decomposição sazonal pip install statsmodels


root = Tk()


root.filename = 'C:/Users/Aluno/Downloads/airline-passengers.csv'
# filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
df = pd.read_csv(root.filename, sep=',', parse_dates=True, index_col='Month' )
f = open('path.txt', 'w')
f.write(root.filename)
f.close()

# cria um gráfico de linhas
df.plot()
plt.show()


# trend 
result = seasonal_decompose(df['Passengers'], model='multiplicative')
result.plot()
plt.show()


