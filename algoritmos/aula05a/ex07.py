q = float(input("Digite a quantidade de litros de combustível: "))
tipo = input("Digite o código do combustível (A ou G): ")

if tipo == 'G':
    if q <= 20:
        valor = 2.5*0.96*q
    else:
        valor = 2.5*0.94*q
elif tipo == 'A':
    if q <= 20:
        valor = 1.9 * 0.97 * q
    else:
        valor = 1.9 * 0.95 * q
print(f"O valor a ser pago por {q}L de combustível do tipo {tipo} é de R${valor}")

