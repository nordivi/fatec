frase = input("Digite uma frase de no máximo 20 palavras: ")
palavras = frase.split()

frase_final = ''
for palavra in palavras:
    frase_final+= palavra[::-1]+' '
print(frase_final.strip())