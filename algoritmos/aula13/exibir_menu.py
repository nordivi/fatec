def exibir_menu():
    while True:
        print("Menu:")
        print("1. Cadastrar")
        print("2. Exibir Frase")
        print("3. Sair")

        choice = input("Escolha uma opção: ")

        if choice.isdigit():
            if int(choice) in list(range(1, 4)):
                return choice

        print("Opção inválida! Por favor, escolha uma opção entre 1 e 3.")


if __name__ == '__main__':
    exibir_menu()