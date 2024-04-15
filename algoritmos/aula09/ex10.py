from random import random

matriz = [[random() for e in range(2)] for e in range(2)]

maior_numero = min(matriz[0])

for linha in matriz:
    maior_numero = max(maior_numero, max(linha))

for i in range(len(matriz[0])):
    for j in range(len(matriz[0])):
        matriz[i][j] *= maior_numero

print(matriz)