largura = float(input("Digite a largura do aposento, em metros: "))
comprimento = float(input("Digite o comprimento do aposento, em metros: "))
litros_lata = float(input("Digite quantos litros têm a lata de tinta: "))

area = largura*comprimento*4 # são 4 paredes
area_porta = 0.8*2.1
area_pintada = area-area_porta # menos a porta
quantidade_latas = (area_pintada/3)/litros_lata # considerando que cada litro pinta 3m²

print(f"A área a ser pintada do aposento é de {area_pintada}m², sendo necessarias "
      f"{quantidade_latas} de latas de tinta para realizar a pintura nas paredes.")