n = int(input("Digite um número: "))
div = 0
for i in range(2, round(n**(1/2))):
    if not n%i:
        div+=1
if div:
    print(f"{n} NÃO é primo!")
else:
    print(f"{n} é primo!")