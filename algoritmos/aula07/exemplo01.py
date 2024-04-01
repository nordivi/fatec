soma = 0

for i in range(5):
    idade = int(input(f"Digite a idade {i+1}: "))
    soma += idade

print("A média das idades é: ", soma/5, 'anos.')