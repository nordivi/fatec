def is_primo(n):
    if n <= 1: # 0 e 1 não são primos!
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if not (n%i):
            return False
    return True

def primos_ate_n(n):
    res = []
    i = 0 # Partindo de 0
    cont = 0 # Contador de números primos
    while cont < n:
        if is_primo(i):
            res.append(i)
            cont+=1
        i += 1
    return len(res), res

Y = 10
inteiro = Y*2+5
tamanho, lista = primos_ate_n(inteiro)
print(f"A lista dos {inteiro} primeiros números primos é {lista}, tem tamanho {tamanho} e"
      f" a soma dos valores é {sum(lista)}.")

