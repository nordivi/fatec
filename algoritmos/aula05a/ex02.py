nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

media = (nota_1+nota_2)/2


if media >= 9:
    conceito = 'A'
    situacao = 'APROVADO'
elif media >= 7.5:
    conceito = 'B'
    situacao = 'APROVADO'
elif media >= 6:
    conceito = 'C'
    situacao = 'APROVADO'
elif media >= 4:
    conceito = 'D'
    situacao = 'REPROVADO'
else:
    conceito = 'E'
    situacao = 'REPROVADO'

print(f"O aluno tirou as notas {nota_1} e {nota_2}, obteve média {media}, conceito {conceito} e "
      f"foi {situacao}.")




