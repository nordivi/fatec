l1 = float(input("Digite o primeiro lado do triângulo: "))
l2 = float(input("Digite o segundo lado do triângulo: "))
l3 = float(input("Digite o terceiro lado do triângulo: "))

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l1:
    if l1 == l2 == l3:
        print("Triângulo equilátero!")
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print("Triângulo isósceles!")
    else:
        print("Triângulo escaleno!")
else:
    print("Não forma um triângulo!")
