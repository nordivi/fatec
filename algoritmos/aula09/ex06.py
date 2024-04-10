from random import randint

dois=0
tres=0
quatro=0
cinco=0
seis=0
sete=0
oito=0
nove=0
dez=0
onze=0
doze=0


for i in range(30000):
    n1 = randint(1,7)
    n2 = randint(1, 7)
    soma = n1+n2
    if soma == 2:
        dois+=1
    elif soma == 3:
        tres+=1
    elif soma == 4:
        quatro+=1
    elif soma == 5:
        cinco+=1
    elif soma == 6:
        seis+=1
    elif soma == 7:
        sete+=1
    elif soma == 8:
        oito+=1
    elif soma == 9:
        nove+=1
    elif soma == 10:
        dez+=1
    elif soma == 11:
        onze+=1
    elif soma == 12:
        doze+=1

print(f"A frequência da soma dois é {dois*100/30000}%")
print(f"A frequência da soma três é {tres*100/30000}%")
print(f"A frequência da soma quatro é {quatro*100/30000}%")
print(f"A frequência da soma cinco é {cinco*100/30000}%")
print(f"A frequência da soma seis é {seis*100/30000}%")
print(f"A frequência da soma sete é {sete*100/30000}%")
print(f"A frequência da soma oito é {oito*100/30000}%")
print(f"A frequência da soma nove é {nove*100/30000}%")
print(f"A frequência da soma dez é {dez*100/30000}%")
print(f"A frequência da soma onze é {onze*100/30000}%")
print(f"A frequência da soma doze é {doze*100/30000}%")

print(f"Frequência da soma 7 corresponde a {sete*100/30000}% das jogadas")
