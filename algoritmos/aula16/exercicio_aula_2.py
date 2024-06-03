tracking={'F':[0,0], 'M':[0,0]}
with open('idades.txt', 'r') as idades:
    for line in idades.readlines():
        i = line.split(',')
        tracking[i[-1].replace('\n','')][0]+=1
        tracking[i[-1].replace('\n','')][1] += int(i[0])

print('Idade média dos homens: ', tracking['M'][1]/tracking['M'][0])
print('Idade média das mulheres: ', tracking['F'][1]/tracking['F'][0])