import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import numpy as np
import math

# exibe um comando cls no prompt de comando
print('\033c') # limpa a tela

# 1. Carregue o dataset
fertility = pd.read_csv('C:\\Users\\Aluno\\Downloads\\fertility_Diagnosis.txt', sep=',', header=None)

# remove a ultima coluna
fertility.drop(fertility.columns[9], axis=1, inplace=True)

# numero máximo de clusters que queremos testar é o numero de linhas do dataset
max_k = fertility.shape[0] # shape[0] retorna o numero de linhas do dataset

# lista vazia para receber as distancias
distortions = []

# lista vazia para receber os valores de k

K = range(1, max_k)

# 2. Para cada valor de k, vamos calcular a soma quadrática dos erros (SSE)

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
    
    # cdist calcula a distância entre dois pontos (euclidean = distância euclidiana)
    # euclidean = sqrt(sum((x - y)^2)) : é uma medida de distância entre dois pontos
    # manhattan = sum(|x - y|) : é uma medida de distância entre dois pontos


# 3. Plotar o gráfico com os valores de k e as distâncias
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show()

