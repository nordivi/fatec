maior_imc = 0
menor_imc = 200
soma_peso = 0
soma_altura = 0
for i in range(1, 6):
    peso = float(input(f"Digite o peso {i} em quilos:"))
    altura = float(input(f"Digite a altura {i} em metros:"))
    soma_peso += peso
    soma_altura += altura
    imc = peso/(altura**2)
    if imc > maior_imc:
        maior_imc = imc
    if menor_imc > imc:
        menor_imc = imc
print("O peso médio é: ", soma_peso/5)
print("A altura média é: ", soma_altura/5)
print("O menor imc é: ", menor_imc)
print("O maior imc é: ", maior_imc)

maior_imc = 0
menor_imc = 200
soma_peso = 0
soma_altura = 0
i=1
while i < 6:
    peso = float(input(f"Digite o peso {i} em quilos:"))
    altura = float(input(f"Digite a altura {i} em metros:"))
    soma_peso += peso
    soma_altura += altura
    imc = peso/(altura**2)
    if imc > maior_imc:
        maior_imc = imc
    if menor_imc > imc:
        menor_imc = imc
    i+=1
print("O peso médio é: ", soma_peso/5)
print("A altura média é: ", soma_altura/5)
print("O menor imc é: ", menor_imc)
print("O maior imc é: ", maior_imc)