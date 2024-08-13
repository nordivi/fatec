# Como não está especificado, irei considerar uma taxa de juros anual simples e o rendimento
# depois de um ano.

deposito = float(input('Valor do depósito inicial: '))
tx = float(input('Taxa de juros anual (a.a.) em %: '))
aumento = (tx/100)*deposito
print(f'Num rendimento a juros simples a taxa de {tx}% a.a. com depósito inicial de {deposito}, '
      f'o aumento é de {aumento} e o valor total depois do rendimento é de {deposito+aumento}. ')