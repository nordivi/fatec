# 1
print('Digite os valores do Quadrilátero...')
base = int(input('Valor da base: '))
altura = int(input('Valor da altura: '))
area = base*altura
print('Base: ', base, ' Altura: ', altura, ' Área: ', area)

# 2
def calc_area(b: float, h: float) -> float:
    a=b*h
    print(f'Um retângulo de base {b} e altura {h} tem área {a}.')
    return a

print('Digite as dimensões do retângulo.')
b = float(input('Digite o valor da base: '))
h = float(input('Digite o valor da altura: '))
calc_area(b, h)