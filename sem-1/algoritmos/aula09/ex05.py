from random import randint
um=0
dois=0
tres=0
quatro=0
cinco=0
seis=0

for i in range(6000):
    num = randint(1, 6)
    if num == 1:
        um+=1
    elif num ==2:
        dois+=1
    elif num == 3:
        tres+=1
    elif num ==4:
        quatro+=1
    elif num == 5:
        cinco+=1
    elif num ==6:
        seis+=1
print("Frequência de 1's: ", um*100/6000, '%')
print("Frequência de 2's: ", dois*100/6000, '%')
print("Frequência de 3's: ", tres*100/6000, '%')
print("Frequência de 4's: ", quatro*100/6000, '%')
print("Frequência de 5's: ", cinco*100/6000, '%')
print("Frequência de 6's: ", seis*100/6000, '%')