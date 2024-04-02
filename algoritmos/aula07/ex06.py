ultimo_numero = 1
penultimo_numero = 1
for i in range(8):
    s = ultimo_numero + penultimo_numero
    penultimo_numero = ultimo_numero
    ultimo_numero = s

print("O décimo número da sequência fibonacci é: ", s)

ultimo_numero = 1
penultimo_numero = 1
i=0
while i != 8:
    s = ultimo_numero + penultimo_numero
    penultimo_numero = ultimo_numero
    ultimo_numero = s
    i+=1

print("O décimo número da sequência fibonacci é: ", s)