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

# Conectar ao banco de dados
try:
    conn = mysql.connector.connect(**config) 
    print("Conexao ao banco de dados realizada com sucesso!")
        
    dados = pd.read_csv(file_path, sep=';', encoding='iso-8859-1', dtype=str, low_memory=False)
    cursor = conn.cursor() # Criando cursor para executar o comando SQL

    # Ano 
    dados_ano = pd.DataFrame(dados['NU_ANO_CENSO'].unique(), columns=['ANO']) # Converte para dataframe
    dados_ano['ANO'].fillna('Não informado', inplace=True) # alterar nan para não informado
    
    # realiza um truncate na tabela dim_ano
    truncate_statement = "TRUNCATE TABLE dim_ano"
    cursor.execute(truncate_statement) # Executando o comando SQL
    conn.commit()

    # Insere os dados de ano
    for i, r in dados_ano.iterrows(): # Iterando sobre o dataframe dados_uf e acessando o indice e a linha
        insert_statement = f"INSERT INTO dim_ano (tf_ano, ano) VALUES ({i}, '{r['ANO']}')"
        cursor.execute(insert_statement)
        conn.commit()
    print("Dados de Ano inseridos com sucesso!")

    # Curso
    dados_curso = pd.DataFrame(dados['NO_CURSO'].unique(), columns=['CURSO']) # Converte para dataframe
    dados_curso['CURSO'].fillna('Não informado', inplace=True) # alterar nan para não informado

    # realiza um truncate na tabela dim_curso
    truncate_statement = "TRUNCATE TABLE dim_curso"
    cursor.execute(truncate_statement) # Executando o comando SQL
    conn.commit()

    # Insere os dados de curso
    for i, r in dados_curso.iterrows(): # Iterando sobre o dataframe dados_uf e acessando o indice e a linha
        insert_statement = f"INSERT INTO dim_curso (tf_curso, curso) VALUES ({i}, '{r['CURSO']}')"
        cursor.execute(insert_statement)
        conn.commit()
    print("Dados de Curso inseridos com sucesso!")

    # IES
    dados_ies = pd.DataFrame(dados['NO_IES'].unique(), columns=['IES']) # Converte para dataframe
    dados_ies['IES'].fillna('Não informado', inplace=True) # alterar nan para não informado

    # realiza um truncate na tabela dim_ies
    truncate_statement = "TRUNCATE TABLE dim_ies"
    cursor.execute(truncate_statement) # Executando o comando SQL
    conn.commit()

    # Insere os dados de ies
    for i, r in dados_ies.iterrows(): # Iterando sobre o dataframe dados_uf e acessando o indice e a linha
        insert_statement = f"INSERT INTO dim_ies (tf_ies, ies) VALUES ({i}, '{r['IES']}')"
        cursor.execute(insert_statement)
        conn.commit()
    print("Dados de IES inseridos com sucesso!")


    # UF
    dados_uf = pd.DataFrame(dados['NO_UF'].unique(), columns=['UF']) # Converte para dataframe
    dados_uf['UF'].fillna('Não informado', inplace=True) # alterar nan para não informado

    # realiza um truncate na tabela dim_uf
    truncate_statement = "TRUNCATE TABLE dim_uf"
    cursor.execute(truncate_statement) # Executando o comando SQL
    conn.commit()

    # UF
    for i, r in dados_uf.iterrows(): # Iterando sobre o dataframe dados_uf e acessando o indice e a linha
        insert_statement = f"INSERT INTO dim_uf (tf_uf, uf) VALUES ({i}, '{r['UF']}')"
        cursor.execute(insert_statement) # Executando o comando SQL
        conn.commit()

    print("Dados de UF inseridos com sucesso!")

    # Converte para dataframe
    dados_municipio = pd.DataFrame(dados['NO_MUNICIPIO'].unique(), columns=['MUNICIPIO'])
    dados_municipio['MUNICIPIO'].fillna('Não informado', inplace=True)
    truncate_statement = "TRUNCATE TABLE dim_municipio"
    cursor.execute(truncate_statement) # Executando o comando SQL
    conn.commit()


    # Municipio
    for i, r in dados_municipio.iterrows(): # Iterando sobre o dataframe dados_uf e acessando o indice e a linha
        insert_statement = "INSERT INTO dim_municipio (tf_municipio, municipio) VALUES (%s, %s)"
        values = (i, r['MUNICIPIO'])
        cursor.execute(insert_statement, values) # Executando o comando SQL
        conn.commit()

    print("Dados de Municipio inseridos com sucesso!")
    
    # Modalidade
    dados_modalidade = pd.DataFrame(dados['TP_MODALIDADE_ENSINO'].unique(), columns=['MODALIDADE'])
    truncate_statement = "TRUNCATE TABLE dim_modalidade"
    cursor.execute(truncate_statement) # Executando o comando SQL
    conn.commit()

    # Modalidade: 
    # 1. Presencial
    # 2. Curso a distância"
    

    for i, r in dados_modalidade.iterrows(): # Iterando sobre o dataframe dados_uf e acessando o indice e a linha
        if r["MODALIDADE"] == '1':
            insert_statement = "INSERT INTO dim_modalidade (tf_modalidade, modalidade) VALUES (%s, %s)"
            values = (i, 'Presencial')
           
        elif r["MODALIDADE"] == '2':
            insert_statement = "INSERT INTO dim_modalidade (tf_modalidade, modalidade) VALUES (%s, %s)"
            values = (i, 'Curso a distância')
        else:
            # insere o valor 0 para os valores NaN
            insert_statement = "INSERT INTO dim_modalidade (tf_modalidade, modalidade) VALUES (%s, %s)"
            values = (i, 'Não informado')
            
        cursor.execute(insert_statement, values)
        conn.commit()

    print("Dados de Modalidade inseridos com sucesso!")

    cursor.close() # Fechar o cursor


except mysql.connector.Error as err:
    print("Erro ao conectar ao banco de dados: {}".format(err))
    exit(1)
finally:
    # Fechar a conexão
    conn.close()
