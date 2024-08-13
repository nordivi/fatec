# 1
celsius = float(input('Digite a temperatura em graus Celsius: '))
fahrenheit = (9*celsius + 160)/5
print(f'{celsius}ºC equivale  {fahrenheit}ºF.')


# 2
def convert_to_fahrenheit(c: float) -> float:
    f = (9*c + 160)/5
    print(f'{c}ºC equivale  {f}ºF.')
    return f

c = float(input('Digite a temperatura em graus Celsius: '))
convert_to_fahrenheit(c)

# 3
fahrenheit = float(input('Digite a temperatura em graus Fahrenheit: '))
celsius = (5*fahrenheit - 160)/9
print(f'{fahrenheit}ºF equivale  {celsius}ºF.')


# 4
def convert_to_celsius(f: float) -> float:
    c = (5*f - 160)/9
    print(f'{f}ºF equivale  {c}ºC.')
    return c

f = float(input('Digite a temperatura em graus Fahrenheit: '))
convert_to_celsius(f)