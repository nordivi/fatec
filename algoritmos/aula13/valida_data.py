from datetime import datetime, date

def valida_data(data):
    try:
        birth_date = datetime.strptime(data, "%d/%m/%Y")
        today = date.today()
        idade = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return idade >= 18
    except ValueError:
        return False

if __name__ == "__main__":
    data = input("Data de nascimento (dd/mm/aaaa): ")
    if valida_data(data):
        print("Pessoa maior de idade!")
    else:
        print("Data inválida ou pessoa tem menos de 18 anos.")