
idade = 'b'
while not idade.isdigit():
    idade = input('Digite sua idade: ')
else:
    idade = int(idade)

print('A idade é: ', idade)