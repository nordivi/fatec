
def mdc(a, b):
    curr = 1
    for x in range(1, min([a,b])+1):
        if not a % x and not b % x:
            curr = x
    return curr

a = mdc(100,60)
print(a)