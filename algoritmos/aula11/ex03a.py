idade_nome = {}
for _ in range(10):
    sn = input("Digite o sobrenome da pessoa: ")
    i = int(input("Digite a idade da pessoa: "))
    idade_nome[sn] = i

sobrenome_mais_velho = max(idade_nome, key=lambda x: idade_nome.get(x))

print(f"\nO sobrenome do mais velho é: {sobrenome_mais_velho}")