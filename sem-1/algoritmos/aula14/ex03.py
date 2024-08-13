def ex03(ra):
    soma = sum([int(i) for i in ra])
    prod = 1
    for i in ra:
        prod *= int(i)

    print(f"Valor do RA: {ra}")
    print(f"Valor da soma dos dígitos do RA: {soma}")
    print(f"Valor do produto dos dígitos do RA: {prod}")
    return soma, prod

soma, prod = ex03('3011392413010')
print("Soma: ", soma)
print("Produto: ", prod)