fruta = input("Fruta: ").upper()

if fruta == "BANANA":
    print("O preço do quilo da banana é de 5.23 reais.")
elif fruta == "MAÇA":
    print("O preço do quilo da maçã é de 12.10 reais")
elif fruta == "CEREJA":
    print("O preço do quilo da cereja é de 58.00 reais")
else:
    print(f"Não temos {fruta}")
# Outra forma
fruta_dict = {"BANANA": 5.23, "MAÇA": 12.10, "CEREJA": 58}

if fruta in fruta_dict:
    print(f"O preço do quilo da {fruta} é de {fruta_dict[fruta]}")
else:
    print(f"Não temos {fruta}")