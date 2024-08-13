letra = input("Digite a letra: ").upper()

if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print(f"{letra} é uma vogal!")
else:
    print(f"{letra} é uma consoante!")

# Outra forma
if letra in {"A", "E", "I", "O", "U"}:
    print(f"{letra} é uma vogal!")
else:
    print(f"{letra} é uma consoante!")
