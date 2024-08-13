l1 = [int(input(f"{i+1}º valor da lista_1: ")) for i in range(5)]
l2 = [int(input(f"{i+1}º valor da lista_2: ")) for i in range(5)]
uniao = set(l1).union(l2)
print("Lista 1: ", l1)
print("Lista 2: ", l2)
print("\nUnião entre lista_1 e lista_2:", uniao)