vetor = [0]*5
for i in range(5):
    vetor[i] = int(input(f"Digite o número {i+1}: "))

print(f"O maior número é {max(vetor)} na posição {vetor.index(max(vetor))}")