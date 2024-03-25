valor_roupa = float(input("Digite o preço da roupa (em reais): "))

if valor_roupa > 5000:
    desconto = 0.3
elif valor_roupa >= 1001:
    desconto = 0.2
else:
    desconto = 0.1

novo_valor_roupa = (1 - desconto)*valor_roupa

print(f"A roupa com valor de R${valor_roupa} recebe desconto de {desconto*100}%, "
      f"com valor de R${desconto*valor_roupa}"
      f" e terá o valor final de R${novo_valor_roupa}.")