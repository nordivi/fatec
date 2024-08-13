from random import random

# Matriz de elementos reais
matriz = [[random() for e in range(4)] for e in range(4)]

soma = 0
for i in range(4):
    soma+=matriz[i][i]

print("A soma da diagonal da matriz é: ", soma)