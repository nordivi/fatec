salario = float(input('Digite seu salário: '))
aumento = float(input('Digite o aumento (percentual): '))
print(f"O salário {salario} com um reajuste de {aumento}% de aumento vale {(1+aumento/100)*salario}.")