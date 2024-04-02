count=0
s=0
for i in range(2, 1000, 2):
    if not i%2:
        count+=1
        s+=i
    if count == 50:
        break

print("A soma dos 50 primeiros pares é: ", s)

count2=0
s2=0
i=2
while count2!=50:
    if not i%2:
        count2+=1
        s2+=i
        i+=2
print("A soma dos 50 primeiros pares é: ", s2)

if not 2%2:
    print('A')