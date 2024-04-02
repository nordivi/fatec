n = int(input("Digite o valor de n: "))
e=0
for i in range(1, n+1):
    e+=2**i

print("O resultado é ", e)

i = 1
e2=0
while i != n+1:
    e2+=2**i
    i+=1

print("O resultado é ", e2)