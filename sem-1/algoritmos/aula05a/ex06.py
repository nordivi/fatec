inteiro = int(input("Digite um inteiro positivo menor que 1000: "))
resposta = ''
if inteiro < 0 or inteiro >= 1000:
    print("O valor deve ser positivo e maior que 1000.")
else:
    cent = inteiro // 100

    inteiro -= cent*100
    if cent:
        if cent == 1:
            resposta += '1 centena'
        else:
            resposta += f'{cent} centenas'

    if not inteiro:
        print(resposta)
    else:
        dezenas = inteiro // 10
        inteiro -= dezenas*10
        if not inteiro and cent:
            resposta += ' e '
        if dezenas and inteiro and cent:
            resposta += ', '
        if dezenas:
            if dezenas == 1:
                resposta += f'1 dezena'
            else:
                resposta += f'{dezenas} dezenas'
        if resposta:
            if inteiro == 1:
                print(resposta + ' e ' + '1 unidade')
            elif inteiro > 1:
                print(resposta + ' e ' + str(inteiro) + ' unidades')
            else:
                print(resposta)
        else:
            if inteiro == 1:
                print('1 unidade')
            elif inteiro > 1:
                print(str(inteiro) + ' unidades')


