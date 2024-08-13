a = float(input("Digite o valor de a: "))
if a:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Valor de delta negativo!")
    elif delta == 0:
        x = -b/(2*a)
        print(f"O programa só possui uma raiz e ela é {x}")
    else:
        x_1 = (-b + delta**(1/2))/2*a
        x_2 = (-b - delta**(1/2))/2*a
        print(f"O programa possui duas raízes e elas são: {x_1} e {x_2}")
else:
    print(f"Valor de {a} não deve ser nulo.")


