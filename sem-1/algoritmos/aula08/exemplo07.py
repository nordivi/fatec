nome = input("Digite seu nome completo: ")
nascimento = input("Digite sua data de nascimento: ")

nome_separado = nome.split(' ')
pre_nome = nome_separado[0]
sobrenome = ' '.join(nome_separado[1:])
print(nome_separado)
print('Nome: ', pre_nome)
print("Sobrenome: ", sobrenome)
print(' | '.join(nome_separado))

dia, mes, ano = nascimento.split('/')
print('Dia: ', dia, " Mês: ", mes, " Ano: ", ano)

