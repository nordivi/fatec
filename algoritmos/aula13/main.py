import random
from exibir_menu import exibir_menu
from valida_data import valida_data
from valida_cpf import valida_cpf

def register():
    name = input("Nome: ")
    surname = input("Sobrenome: ")
    while True:
        cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")
        if valida_cpf(cpf):
            break
        else:
            print("CPF inválido!")
    while True:
        data = input("Data de nascimento (dd/mm/aaaa): ")
        if valida_data(data):
            break
        else:
            print("Data inválida!")
    renda_bruta = float(input("Digite a renda bruta: "))
    print("Cadastro realizado com sucesso!")
    print("Nome:", name)
    print("Sobrenome:", surname)
    print("CPF:", cpf)
    print("Data de Nascimento:", data)
    print("Renda Bruta:", renda_bruta)

def exibir_mensagem():
    messages = [
        "A persistência realiza o impossível",
        "Seus sonhos não precisam de plateia, eles só precisam de você",
        "A persistência é o caminho do êxito",
        "No meio da dificuldade encontra-se a oportunidade"
    ]
    message = random.choice(messages)
    print(message)

if __name__ == "__main__":
    while True:
        choice = exibir_menu()
        if choice == 1:
            register()
        elif choice == 2:
            exibir_mensagem()
        elif choice == 3:
            print("Bye bye!")
            break