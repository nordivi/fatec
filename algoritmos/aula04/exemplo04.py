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