A = [int(input(f"Digite o valor de posição {j+1}º do vetor.")) for j in range(10)]


B = sorted(A)

print('A (lista inicial): ', A, 'B (lista em ordem crescente): ',B)