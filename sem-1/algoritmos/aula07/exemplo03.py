numero = int(input("Entre com o número: "))
fatorial = 1
if numero < 0:
    print("Fatorial não existe!")
elif not numero:
    print("0! = 1.")
else:
    for i in range(1, numero+1):
        fatorial*=i
    print(f"{numero}! = {fatorial}")

def fatorial(n):

    def rec(i):
        if i <= 1:
            return 1
        return i*rec(i-1)
    return rec(n)


fat = fatorial(5)
print(fat)