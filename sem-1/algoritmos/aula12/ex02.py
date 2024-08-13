def is_primo(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if not (n%i):
            return False
    return True

a = is_primo(103)
print(a)