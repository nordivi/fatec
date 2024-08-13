from random import randint

matriz = [[randint(-(10**9), 10**9) for e in range(8)] for e in range(8)]
for linha in matriz:
    print(linha)
simetrica = True
while simetrica:
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] != matriz[j][i]:
                simetrica = False

if simetrica:
    print("A MATRIZ É SIMÉTRICA!")
else:
    print("A MATRIZ NÃO É SIMÉTRICA!")
