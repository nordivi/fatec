tupla = ()
for i in range(10):
    num = (int(input("Digite um inteiro: ")),)
    tupla += num

print(tupla[::-1])