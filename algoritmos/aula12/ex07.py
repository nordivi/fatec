from ex02 import is_primo


def lista_primos(n):
    res = []
    for i in range(2, n+1):
        if is_primo(i):
            res.append(i)
    return res

# 1 não é primo
lista = lista_primos(10)
print(lista)