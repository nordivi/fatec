ultimo_numero = 1
penultimo_numero = 1
print('1: 1')
print('2: 1')
for i in range(48):
    s = ultimo_numero + penultimo_numero
    print(f'{i+3}: {s}')
    penultimo_numero = ultimo_numero
    ultimo_numero = s


ultimo_numero = 1
penultimo_numero = 1
print('1: 1')
print('2: 1')
i=0
while i != 48:
    s = ultimo_numero + penultimo_numero
    print(f'{i + 3}: {s}')
    penultimo_numero = ultimo_numero
    ultimo_numero = s
    i+=1

