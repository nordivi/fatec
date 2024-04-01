count = 0
sum = 0
idade = 0
while idade != -1:
    sum += idade
    count += 1
    idade = int(input(f"Digite a idade {count}: "))

print(f"A média de {count-1} idades é de {sum/(count-1)}")