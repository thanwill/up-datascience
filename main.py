# Métrica: Quantidade de estudantes
# Autor: Jonathan Pereira
# Data: 2023-08-14
# Versão: 0.0.1

import mysql.connector 
import tkinter as tk 
import pandas as pd  
from tkinter import filedialog 
#Comando para instlar todas as bibliotecas: pip install mysql-connector-python tk pandas

# root = tk.Tk() # Crie uma janela em branco (não é exibida)
# root.withdraw() Janela de diálogo para selecionar o arquivo CSV
# file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
# root.withdraw()
# file_ies_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

#file_path ='C:/Users/Aluno/Documents/microdados_censo_da_educacao_superior_2020/Microdados do Censo da Educação Superior 2020/dados/MICRODADOS_CADASTRO_CURSOS_2020.CSV'
#file_ies_path = 'C:/Users/Aluno/Documents/microdados_censo_da_educacao_superior_2020/Microdados do Censo da Educação Superior 2020/dados/MICRODADOS_CADASTRO_IES_2020.CSV'

file_path = '/Users/jonathan/Downloads/Microdados do Censo da Educaá∆o Superior 2021/dados/MICRODADOS_CADASTRO_CURSOS_2021.CSV'
file_ies_path = '/Users/jonathan/Downloads/Microdados do Censo da Educaá∆o Superior 2021/dados/MICRODADOS_CADASTRO_IES_2021.CSV'

if file_path:
    print("Arquivo de dados selecionado:", file_path)
    print("Arquivo IES selecionado:", file_ies_path)
    
else:
    print("Nenhum arquivo selecionado.")

# Dictionary com as informações de conexão
config = {
    "user" : "root",
    "password" : "atzmkl712",
    "host" : 'localhost',
    "database" : 'dw_inep'
}


# Conectar ao banco de dados
try:
    conn = mysql.connector.connect(**config) 
    print("Conexao ao banco de dados realizada com sucesso!")
    cursor = conn.cursor() #Criando cursor para executar o comando SQL

    dados = pd.read_csv(file_path, sep=';', encoding='iso-8859-1', dtype=str, low_memory=False)
    dados.fillna('Não informado', inplace=True) #alterar nan para não informado
    dados_IES = pd.read_csv(file_ies_path, sep=';', encoding='iso-8859-1', dtype=str, low_memory=False)

    # Realiza truncate na tabela dim_ies
    truncate_statement = "TRUNCATE TABLE dim_ies"
    cursor.execute(truncate_statement) #Executando o comando SQL
    conn.commit()
    
    dados_IES = dados_IES[['CO_IES','NO_IES']] #Seleciona as colunas CO_IES e NO_IES
    dados_IES_curso = pd.DataFrame(dados['CO_IES'].unique(), columns = ['co_ies']) #Converte para dataframe e seleciona a coluna CO_IES e remove os valores duplicados
    
    for i, r in dados_IES_curso.iterrows(): #Iterando sobre o dataframe dados_uf e acessando o indice e a linha
        dados_IES_filtrado=dados_IES[dados_IES['CO_IES'] == r['co_ies']] #Filtra os dados de IES
        no_ies = dados_IES_filtrado['NO_IES'].iloc[0].replace("'","") #Seleciona o nome da IES
        insert_statement = f"insert into dim_ies (tf_ies, ies) values({i+1}, '{no_ies}')" #Cria o comando SQL
        cursor.execute(insert_statement)
        conn.commit()

    print("Dados de IES inseridos com sucesso!")

    # Ano 
    dados_ano = pd.DataFrame(dados['NU_ANO_CENSO'].unique(), columns=['ANO']) #Converte para dataframe
    dados_ano['ANO'].fillna('Não informado', inplace=True) #alterar nan para não informado
    
    truncate_statement = "TRUNCATE TABLE dim_ano"
    cursor.execute(truncate_statement) #Executando o comando SQL
    conn.commit()

    for i, r in dados_ano.iterrows(): #Iterando sobre o dataframe dados_uf e acessando o indice e a linha
        insert_statement = f"INSERT INTO dim_ano (tf_ano, ano) VALUES ({i + 1}, '{r['ANO']}')"
        cursor.execute(insert_statement)
        conn.commit()
    print("Dados de Ano inseridos com sucesso!")

    # Curso
    dados_curso = pd.DataFrame(dados['NO_CURSO'].unique(), columns=['CURSO']) 
    dados_curso['CURSO'].fillna('Não informado', inplace=True)

    limpar = False
    
    if limpar:
        truncate_statement = "TRUNCATE TABLE dim_curso"
        cursor.execute(truncate_statement) 
        truncate_statement = "TRUNCATE TABLE dim_uf"
        cursor.execute(truncate_statement) 
        truncate_statement = "TRUNCATE TABLE dim_municipio"
        cursor.execute(truncate_statement) 
        truncate_statement = "TRUNCATE TABLE dim_modalidade"
        cursor.execute(truncate_statement) 
        truncate_statement = "TRUNCATE TABLE dim_ano"
        cursor.execute(truncate_statement)
        truncate_statement = "TRUNCATE TABLE dim_ies"
        cursor.execute(truncate_statement)
        truncate_statement = "TRUNCATE TABLE fact_matricula"
        cursor.execute(truncate_statement) 
        conn.commit()
        print("Tabelas limpas com sucesso!")
    
    for i, r in dados_curso.iterrows(): 
        insert_statement = f"INSERT INTO dim_curso (tf_curso, curso) VALUES ({i + 1}, '{r['CURSO']}')"
        cursor.execute(insert_statement)
        conn.commit()
    print("Dados de Curso inseridos com sucesso!")

    # UF
    dados_uf = pd.DataFrame(dados['NO_UF'].unique(), columns=['UF']) 
    dados_uf['UF'].fillna('Não informado', inplace=True)

    for i, r in dados_uf.iterrows(): 
        insert_statement = f"INSERT INTO dim_uf (tf_uf, uf) VALUES ({i + 1}, '{r['UF']}')"
        cursor.execute(insert_statement) 
        conn.commit()

    print("Dados de UF inseridos com sucesso!")
    
    # Minicípio
    dados_municipio = pd.DataFrame(dados['NO_MUNICIPIO'].unique(), columns=['MUNICIPIO'])
    dados_municipio['MUNICIPIO'].fillna('Não informado', inplace=True)

    
    for i, r in dados_municipio.iterrows(): 
        insert_statement = "INSERT INTO dim_municipio (tf_municipio, municipio) VALUES (%s, %s)"
        values = (i + 1, r['MUNICIPIO'])
        cursor.execute(insert_statement, values) 
        conn.commit()

    print("Dados de Municipio inseridos com sucesso!")
    
    # Modalidade
    dados_modalidade = pd.DataFrame(dados['TP_MODALIDADE_ENSINO'].unique(), columns=['MODALIDADE'])
    
    
    for i, r in dados_modalidade.iterrows():
        if r["MODALIDADE"] == '1':
            insert_statement = "INSERT INTO dim_modalidade (tf_modalidade, modalidade) VALUES (%s, %s)"
            values = (i +1 , 'Presencial')
           
        elif r["MODALIDADE"] == '2':
            insert_statement = "INSERT INTO dim_modalidade (tf_modalidade, modalidade) VALUES (%s, %s)"
            values = (i + 1, 'Curso a distância')
        else:            
            insert_statement = "INSERT INTO dim_modalidade (tf_modalidade, modalidade) VALUES (%s, %s)"
            values = (i +1, 'Não informado')
            
        cursor.execute(insert_statement, values)
        conn.commit()

    print("Dados de Modalidade inseridos com sucesso!")

    # Tabela fato matriculas
    

    for i, r in dados.iterrows():

        if r['TP_MODALIDADE_ENSINO'] == '1':
            modalidade = 'Presencial'
        elif r['TP_MODALIDADE_ENSINO'] == '2':
            modalidade = 'EAD'
            
        # verifica se o municipio é nulo e insere o valor NULL
        if pd.isnull(r['NO_MUNICIPIO']):
            municipio = "NULL"
        else:
            municipio = r['NO_MUNICIPIO'].replace("'","")

        ies_filtro = dados_IES[dados_IES['CO_IES'] == r['CO_IES']]
        ies = ies_filtro['NO_IES'].iloc[0].replace("'","")

        insert_statement = """
            INSERT INTO fact_matricula (matriculados, tf_ano, tf_uf, tf_ies, tf_curso, tf_modalidade, tf_municipio)
            SELECT DISTINCT * FROM
            (SELECT %s) as matriculados,
            (SELECT tf_ano FROM dim_ano WHERE ano = %s) as tf_ano,
            (SELECT tf_uf FROM dim_uf WHERE uf = %s) as tf_uf,
            (SELECT tf_ies FROM dim_ies WHERE ies = %s) as tf_ies,
            (SELECT tf_curso FROM dim_curso WHERE curso = %s) as tf_curso,
            (SELECT tf_modalidade FROM dim_modalidade WHERE modalidade = %s) as tf_modalidade,
            (SELECT tf_municipio FROM dim_municipio WHERE municipio = %s) as tf_municipio
        """
        cursor.execute(insert_statement, (r['QT_INSCRITO_TOTAL'], r['NU_ANO_CENSO'], r['NO_UF'], ies, r['NO_CURSO'], modalidade, municipio))
        conn.commit()

    print("Dados de Matriculas inseridos com sucesso!")

    cursor.close() 
    print("Fim da execução!")

except mysql.connector.Error as err:
    print("Erro ao conectar ao banco de dados: {}".format(err))
    exit(1)
finally:
    conn.close()
