from random import randint

matriz = [[randint(-(10**9), 10**9) for e in range(20)] for e in range(10)]
matriz_soma = [0]*10

for i, linha in enumerate(matriz):
    matriz_soma[i] = sum(linha)

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] *= matriz_soma[i]

print("Matriz soma: ", matriz_soma)
print("Matriz multiplicada pela soma: ", matriz)