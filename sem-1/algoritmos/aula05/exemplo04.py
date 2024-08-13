nota = float(input("Digite a nota: "))

if nota < 0 or nota > 1:
    print("Entrada Errada!")
elif nota >= 0.9:
    print("Conceito A!")
elif nota >= 0.8:
    print("Conceito B!")
elif nota >= 0.7:
    print("Conceito C!")
elif nota >= 0.6:
    print("Conceito D!")
elif nota < 0.6:
    print("Conceito F!")
