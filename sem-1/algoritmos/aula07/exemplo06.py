n = 0
while True:
    if n%2:
        n+=1
        continue
    print("O valor de n é: ", n)
    n+=1
    if n>100:
        break