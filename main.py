# Métrica: Quantidade de estudantes
# Autor: Jonathan Pereira
# Data: 2023-08-14
# Versão: 0.0.1

# Dimensoes 
# 1 - UF
# 2 - Município
# 3 - Instituição / IES
# 4 - Modalidade de ensino
# 5 - Curso
# 6 - Ano

# Criar dimensões e tabela fato

# ETL  - Extract Transform Load: serve para extrair, transformar e carregar dados de um banco de dados para outro

# conectar ao banco de dados

import mysql.connector
import pandas as pd


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
    #
    url = 'C:/Users/Aluno/Downloads/Microdados do Censo da Educação Superior 2020/dados/MICRODADOS_CADASTRO_CURSOS_2020.CSV'
    
    # Carregar o arquivo csv
    dados = pd.read_csv(url, sep=';', encoding='iso-8859-1')
    
    #print(dados.head()) # Mostra as 5 primeiras linhas do arquivo

    # Colunas 
    #print (dados.columns)
    # uma unica coluna
    #print(dados.columns['CO_IES'])

    dados_uf = dados['NO_UF'].unique() # Mostra os valores unicos da coluna no formato ndarray
    
    dados_uf = pd.DataFrame(dados_uf, columns=['UF']) # Converte para dataframe

    # print(dados_uf['UF'][1]) # Acessando o valor da linha 1 da coluna UF
    
    for i, r in dados_uf.iterrows(): # Iterando sobre o dataframe dados_uf e acessando o indice e a linha
        
     
        
        #Criando inser com interpolação de string
        insert_statement = f"INSERT INTO dim_uf (tf_uf, uf) VALUES ({i}, '{r['UF']}')"
    
        cursor = conn.cursor() # Criando cursor para executar o comando SQL

        cursor.execute(insert_statement) # Executando o comando SQL

        conn.commit()

        cursor.close() # Fechar o cursor


except mysql.connector.Error as err:
    print("Erro ao conectar ao banco de dados: {}".format(err))
    exit(1)
finally:
    # Fechar a conexão
    conn.close()

