data = input('Digite uma data ano formato DD/MM/AAAA: ')
data_separada = data.split('/')
print("A conversão dessa data no formato AAAAMMDD é: ",
      data_separada[2]+data_separada[1]+data_separada[0])