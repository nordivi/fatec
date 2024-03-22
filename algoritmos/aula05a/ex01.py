qttd_hora = float(input("Digite a quantidade de horas: "))
valor_hora = float(input("Digite o valor ganho por hora: "))
salario = qttd_hora*valor_hora


# Cálculo do IR
if salario >= 2500:
    aliquita = 0.2
elif salario >= 1500:
    aliquita = 0.1
elif salario >= 900:
    aliquita = 0.05

ir = aliquita*salario
#INSS
inss = 0.1*salario

#FGTS
fgts = 0.11*salario
salario_liquido = salario - ir - inss


print(f"Salário bruto: ({valor_hora}*{qttd_hora}): {salario} \n"
      f"(-) IR ({aliquita}): {ir} \n"
      f"(-) INSS (10%): {inss} \n"
      f"FGTS (11%): {fgts} \n"
      f"Total de descontos: {ir + inss} \n"
      f"Salário Líquido: {salario_liquido}")
