vetor1 = [1,2,3,4,5]
vetor2 = [6,7,8,9,10]
vetor1 = [int(input(f"Digite o valor de posição {j} do vetor 1")) for j in range(5)]
vetor2 = [int(input(f"Digite o valor de posição {j} do vetor 2")) for j in range(5)]

vet3=[]
for i,j in zip(vetor1, vetor2):
    vet3.append(i)
    vet3.append(j)



print(vet3)