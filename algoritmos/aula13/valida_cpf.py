def valida_cpf(cpf: str):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    t, mult = 0, 0
    for i in range(9):
        t += int(cpf[i]) * mult
        mult -= 1
    resto = t % 11
    if resto < 2:
        d1 = 0
    else:
        d1 = 11 - resto

    t, mult = 0, 0
    for i in range(10):
        t += int(cpf[i]) * mult
        mult -= 1
    resto = t % 11
    if resto < 2:
        d2 = 0
    else:
        d2 = 11 - resto

    return d1 == int(cpf[9]) and d2 == int(cpf[10])


if __name__ == "__main__":
    cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")
    if valida_cpf(cpf):
        print("CPF válido!")
    else:
        print("CPF inválido!")