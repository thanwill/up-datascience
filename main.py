# Métrica: Quantidade de estudantes
# Autor: Jonathan Pereira
# Data: 2023-08-14
# Versão: 0.0.1

import mysql.connector # Biblioteca para conectar ao banco de dados
import tkinter as tk # Biblioteca para criar janelas
from tkinter import filedialog # Biblioteca para abrir janela de diálogo
import pandas as pd  # Biblioteca para trabalhar com dataframes

# Comando para instlar todas as bibliotecas: pip install mysql-connector-python tk pandas
# Crie uma janela em branco (não é exibida)
root = tk.Tk()
root.withdraw()


# Janela de diálogo para selecionar o arquivo CSV
file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

# Verifica se o usuário selecionou um arquivo
if file_path:
    print("Arquivo selecionado:", file_path)
else:
    print("Nenhum arquivo selecionado.")

# Dictionary com as informações de conexão

config = {
    "user" : "root",
    "password" : "positivo",
    "host" : 'localhost',
    "database" : 'dw_inep'
}

config2 = {
    "user" : "root",
    "password" : "atzmkl712",
    "host" : 'localhost',
    "database" : 'dw_inep'
}

# Conectar ao banco de dados
try:
    conn = mysql.connector.connect(**config2) 
    print("Conexao ao banco de dados realizada com sucesso!")
        
    dados = pd.read_csv(file_path, sep=';', encoding='iso-8859-1', dtype=str, low_memory=False)
    dados_uf = dados['NO_UF'].unique() # Mostra os valores unicos da coluna no formato ndarray
    dados_uf = pd.DataFrame(dados_uf, columns=['UF']) # Converte para dataframe

    # print(dados_uf['UF'][1]) # Acessando o valor da linha 1 da coluna UF
    # realiza um truncate na tabela dim_uf
    truncate_statement = "TRUNCATE TABLE dim_uf"
    cursor = conn.cursor() # Criando cursor para executar o comando SQL
    cursor.execute(truncate_statement) # Executando o comando SQL
    conn.commit()
    cursor.close() # Fechar o cursor

    # UF
    for i, r in dados_uf.iterrows(): # Iterando sobre o dataframe dados_uf e acessando o indice e a linha
        
        insert_statement = f"INSERT INTO dim_uf (tf_uf, uf) VALUES ({i}, '{r['UF']}')"
        cursor = conn.cursor() # Criando cursor para executar o comando SQL
        cursor.execute(insert_statement) # Executando o comando SQL
        conn.commit()
        cursor.close() # Fechar o cursor

    print("Dados de UF inseridos com sucesso!")

    
    # Converte para dataframe
    dados_municipio = pd.DataFrame(dados['NO_MUNICIPIO'].unique(), columns=['MUNICIPIO'])
    truncate_statement = "TRUNCATE TABLE dim_municipio"
    cursor = conn.cursor() # Criando cursor para executar o comando SQL
    cursor.execute(truncate_statement) # Executando o comando SQL
    conn.commit()
    cursor.close() # Fechar o cursor

    # Municipio
    for i, r in dados_municipio.iterrows(): # Iterando sobre o dataframe dados_uf e acessando o indice e a linha
        if pd.notna(r['MUNICIPIO']):  # Verifica se o valor não é NaN
            insert_statement = "INSERT INTO dim_municipio (tf_municipio, municipio) VALUES (%s, %s)"
            values = (i, r['MUNICIPIO'])
            cursor = conn.cursor() # Criando cursor para executar o comando SQL
            cursor.execute(insert_statement, values) # Executando o comando SQL
            conn.commit()
            cursor.close() # Fechar o cursor            
        
    print("Dados de Municipio inseridos com sucesso!")

except mysql.connector.Error as err:
    print("Erro ao conectar ao banco de dados: {}".format(err))
    exit(1)
finally:
    # Fechar a conexão
    conn.close()
