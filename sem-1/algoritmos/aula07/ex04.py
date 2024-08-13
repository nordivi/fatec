soma = 0
k=0
for i in range(1000):
    n = int(input("Digite um número"))
    if not n%2 and n != 0:
        soma+=n
        k+=1
    if n == 0:
        break
print(f"A média aritmética dos números pares fornecidos é: ", soma/k)

soma = 0
i=0
while True:
    n = int(input("Digite um número"))
    if not n%2 and n != 0:
        soma+=n
        i+=1
    if n == 0:
        break
print(f"A média aritmética dos números pares fornecidos é: ", soma/i)