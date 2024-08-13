n = int(input("Digite o número inteiro: "))

if not n%15:
    print(f"O número {n} é divisível por 3 e 5 ao mesmo tempo.")
else:
    print(f"O número {n} NÃO é divisível por 3 e 5 ao mesmo tempo.")

# Explicação:
# Note que um número ser divisível por 3 e 5 ao mesmo tempo significa que ele, necessariamente,
# é divisível por 15, multiplicando os fatores.
# n%15 será True se houver resto, explicando a utilização do not.