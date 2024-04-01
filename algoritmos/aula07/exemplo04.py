frase = input("Digite uma frase: ")

count = 0
for caracter in frase:
    if caracter.upper() == 'A':
        count+=1
print(f"A frase {frase} contém {count} A's.")