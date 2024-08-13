tracking = {}

def convert_bits_em_mega (bits):
    return round(bits/(1024**2),2)

with open('entrada_ex1.txt', 'r', encoding='utf-8') as arq:
    for linha in arq:
        name = linha.split(' ')[0]
        value = int(linha.split(' ')[-1].replace('\n',''))
        tracking[name] = convert_bits_em_mega(value)
soma = sum(tracking.values())
media = round(soma/len(tracking),2)


print('ACME Inc.' + 20*' ' + 'Uso do espaço em disco pelos usuários')
print(68*'-')
print('Nr.' + '   ' + 'Usuário' + 10*' ', 'Espaço utilizado', 9*' ', '% do uso')
index = 0
for key, value in tracking.items():
    print(str(index+1)+ '     ' + key + (30-len(key)-len(str(value)))*' ' + str(value) + ' MB' + (18-len(str(round(value/soma,2))))*' ' + str(round((value/soma)*100,2))+ '%')
    index+=1

print(f"Espaço total ocupado: {soma} MB")
print(f"Espaço médio ocupado: {media} MB")