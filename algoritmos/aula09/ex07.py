lista_primos = []
i=100
while len(lista_primos) < 10:
    for j in range(2, i):
        if j == i-1:
            lista_primos.append(i)

            i+=1
            break
        if not i % j:
            i+=1
            break
        else:
            continue


print(lista_primos)