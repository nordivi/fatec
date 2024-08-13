def converte_segundos(h, m, s):
    s+=h*3600
    s+=m*60
    return s

a = converte_segundos(2, 40, 10)
print(a)