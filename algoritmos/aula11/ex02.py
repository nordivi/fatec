tupla_primos = ()
i=100
while len(tupla_primos) < 10:
    for j in range(2, i):
        if j == i-1:
            tupla_primos += (i,)

            i+=1
            break
        if not i % j:
            i+=1
            break
        else:
            continue

print(tupla_primos)
