import random # biblioteca para gerar numeros aleatorios
import statistics # biblioteca para calcular media, mediana, etc
import numpy as np # biblioteca para trabalhar com vetores e matrizes
import matplotlib.pyplot as plt
from scipy.stats import norm

# pip install scipy matplotlib numpy statistics
serie = []
# serie de 100 valores entre 7 e 500 (inclusive) gerados aleatoriamente
serie = random.sample(range(7, 501), 100)
    
# converte a lista em ndarray
serie = np.array(serie)
media = np.mean(serie)
desvio_padrao = np.std(serie)

print("Media: ", np.mean(serie))
print("Mediana: ", np.median(serie))
print("Desvio padrao: ", np.std(serie))
print("Variancia: ", np.var(serie))


# Crie um intervalo de valores para o eixo x
x = np.linspace(min(serie), max(serie), 100)

# Calcule a densidade de probabilidade da distribuição normal
pdf = norm.pdf(x, loc=media, scale=desvio_padrao)

# Crie o gráfico de densidade de probabilidade
plt.plot(x, pdf, label='Distribuição Normal', color='blue')
plt.hist(serie, density=True, alpha=0.5, color='green', bins=20, edgecolor='k', label='Dados Observados')
plt.xlabel('Valores')
plt.ylabel('Densidade de Probabilidade')
plt.title('Diagrama de Distribuição Normal')
plt.show()

# gráfico de controle   
plt.plot(serie, color='blue', label='Dados Observados')
plt.axhline(media, color='red', label='Media')
plt.axhline(media + 3*desvio_padrao, color='green', label='Limite Superior')
plt.axhline(media - 3*desvio_padrao, color='green', label='Limite Inferior')
plt.xlabel('Amostras')
plt.ylabel('Valores')
plt.title('Gráfico de Controle')
plt.legend()
plt.show()




