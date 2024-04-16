dados = {}
for i in range(5):
    n = input("Digite o nome da pessoa: ")
    i = int(input("Digite a idade da pessoa: "))
    dados[n] = i
idades = list(dados.values())
media = sum(idades) / len(idades)

for nome, idade in dados.items():
    if idade > media:
        print(f"{nome}: {idade} (anos) tem a idade maior que a média {media} (anos)")