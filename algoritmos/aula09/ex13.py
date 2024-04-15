from random import randint


matriz = [[randint(-(10)**9, 10**9) for e in range(10)] for e in range(10)]
# print(matriz)
maior_numero = min(matriz[0])
l, c = 0,0
for i in range(10):
    for j in range(10):
        if matriz[i][j] > maior_numero:
            maior_numero = matriz[i][j]
            l, c = i+1, j+1

print(f"O maior número da matriz é {maior_numero} e está na posição ({l}, {c}), considerando "
      f"que o primeiro elemento da lista está na posição (1,1).")