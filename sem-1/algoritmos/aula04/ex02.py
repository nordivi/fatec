nascimento = int(input('Ano de nascimento: '))
ano_atual = int(input('Ano atual: '))
idade = ano_atual-nascimento # Considerando que a pessoa já fez aniversário em questão.
print('Idade em anos: ', idade)

meses = idade*12
print('Idade em meses: ', meses)

dias = 365*idade
print('Idade em dias: ', dias)

semanas = idade*52
print('Idade em semanas: ', semanas)