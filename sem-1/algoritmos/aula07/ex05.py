x = int(input("Digite o número: "))
prod=1
for i in range(1, x+1):
    prod*=i

print(f"O fatorial de {x} é: ", prod)

i=1
prod=1
while i != x+1:
    prod*=i
    i+=1

print(f"O fatorial de {x} é: ", prod)