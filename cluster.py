import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import numpy as np
import math
from pickle import dump
from pickle import load

try:
    
    fertility = pd.read_csv('C:\\Users\\Aluno\\Downloads\\fertility_Diagnosis.txt', names=header) # lê o arquivo csv
    fertility.drop(fertility.columns[9], axis=1, inplace=True) # remove a coluna 9

    # numero máximo de clusters que queremos testar é o numero de linhas do dataset
    max_k = fertility.shape[0] # shape[0] retorna o numero de linhas do dataset
    distortions = [] # lista vazia para receber as distancias
    K = range(1, max_k)

    # For para calcular a distância de cada ponto para o centróide mais próximo
    for k in K:
        # 2.1. Criar o modelo KMeans com o valor de k
        kmeanModel = KMeans(n_clusters=k).fit(fertility)
        kmeanModel.fit(fertility)
        # 2.2. Calcular a distância de cada ponto para o centróide mais próximo
        # 2.3. Somar a distância de cada ponto para o centróide mais próximo e dividir pelo número de pontos
        # 2.4. Adicionar a soma na lista de distâncias
        distortions.append(
            sum(
                np.min(
                    cdist(fertility, kmeanModel.cluster_centers_, 'euclidean'), axis=1)
                ) / fertility.shape[0])

    x0 = K[0] # primeiro ponto do gráfico
    y0 = distortions[0]  # primeiro ponto do gráfico 
    x1 = K[len(K)-1] # último ponto do gráfico
    y1 = distortions[len(distortions)-1] # último ponto do gráfico

    distancias = [] # lista vazia para receber as distancias entre os pontos e a reta

    for i in range(len(distortions)):
        x = K[i]
        y = distortions[i]
        numerador = abs((y1 - y0) * x + (x0 - x1) * y + (x1 * y0 - x0 * y1))
        denominador = math.sqrt((y1 - y0) ** 2 + (x0 - x1) ** 2)
        distancias.append(numerador / denominador)
    
    print(f" O maior valor de distancias é {max(distancias)}") # print maior valor de distancias
    print(f" A posição do maior valor de distancias é {distancias.index(max(distancias))}") # print posição do maior valor de distancias 
    n_clusters = K[distancias.index(max(distancias))] # n_clusters recebe o valor de k
    print(f" O valor de k é {n_clusters}") # print valor de k

    # 5. Criar o modelo KMeans com o valor de k
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(fertility)
    centroides = kmeans.cluster_centers_ # obtem os centroides
    dump(kmeans, open('C:\\Users\\Aluno\\Downloads\\kmeans.pkl', 'wb')) # salva o modelo no arquivo kmeans.pkl (wb = write binary)
    novo_paciente = fertility.iloc[98] # dados de um novo paciente
    kmeans = load(open('C:\\Users\\Aluno\\Downloads\\kmeans.pkl', 'rb')) # rb = read binary

    resultado = kmeans.predict([novo_paciente]) # aplica o modelo aos dados do novo paciente

    print(resultado)
    print(f"O paciente {novo_paciente} pertence ao cluster {resultado[0]}")
    print(f"Centroide do cluster: {centroides[resultado[0]]}") # exibe o centroide do cluster do novo paciente
    
    print(fertility['Output'].value_counts())


except Exception as e:
        print(f"Um erro ocorreu: {e}")
    
