def is_bissexto(ano):
    if ano % 4 != 0:
        return 0
    else:
        if ano % 100 != 0:
            return 1
        else:
            if ano % 400 == 0:
                return 1
            else:
                return 0

ano = 1000
a = is_bissexto(ano)
print(a)