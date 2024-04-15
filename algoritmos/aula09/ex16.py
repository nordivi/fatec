from random import random

matriz = [[random()*((e+1)**3) for e in range(5)] for e in range(5)]
# Isso é apenas outra forma de gerar números aleatórios arbitrariamente!
for linha in matriz:
    print(linha)
soma = 0
total_nums = 0
for i, linha in enumerate(matriz):
    if (i + 1) % 2 != 0:
        total_nums += len(linha)
        soma += sum(linha)

print("A média da soma dos números em linhas ímpares é: ", soma/total_nums)