import numpy as np

#Função que simula o jogo de dado e soma os resultados de rodada e atribui em um Array
def doisDados():
    resultArray = np.array([])
    dados = np.random.randint(1,7, (2,1))
    resultado = sum(dados)
    resultArray = np.append(resultArray,resultado)
  
    return resultArray

#Chamando a função doisDados e rodando 1000 vezes e atribui os resultados em um array

resultados = np.array([])

for i in range (1000):
    if i < 1001:
        resultados = np.append(resultados, doisDados())

#Calculos de média, máximo e minimo
media = np.average(resultados)
maximo = np.amax(resultados.astype(int))
minimo = np.amin(resultados.astype(int))

print('Média dos resultados: ', media, '\nMaior resultado: ', maximo, '\nMenor resultado: ', minimo)

#Resultados que sairam e a frequência 
numUnico, frequencia = np.unique(resultados.astype(int), return_counts=True)

numsFrequencia = dict(zip(numUnico, frequencia))
print('Números e Frequências: ', numsFrequencia)


#Teste de Hipótese: Agora vamos fazer um pouco de teste de hipóteses:
 
