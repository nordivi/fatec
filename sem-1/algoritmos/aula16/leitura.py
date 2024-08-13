arquivo = open('texto.txt', 'r', encoding='utf-8')
texto = arquivo.read()
print(texto)
arquivo.close()