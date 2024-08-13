palavra = input("Digite uma palavra: ")


print('É um palíndromo!!!' if palavra.upper() == palavra.upper()[::-1] else "Não é um palíndromo!")