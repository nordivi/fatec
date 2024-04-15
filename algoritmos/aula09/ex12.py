from random import random


matriz = [[random() for e in range(3)] for e in range(3)]
result = [[0 for e in range(3)] for e in range(3)]

for i in range(len(matriz)):
   for j in range(len(matriz[0])):
       result[j][i] = matriz[i][j]

print(result)