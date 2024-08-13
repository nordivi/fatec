from math import ceil
largura = float(input("Digite a largura do aposento, em metros: "))
comprimento = float(input("Digite o comprimento do aposento, em metros: "))
litros_lata = float(input("Digite quantos litros têm a lata de tinta: "))
pe_direito = 2.8
area_paredes = (largura*pe_direito)*2 + (comprimento*pe_direito)*2 # são 4 paredes
area_porta = 0.8*2.1
area_pintada = area_paredes-area_porta # menos a porta
quantidade_latas = (area_pintada/3)/litros_lata # considerando que cada litro pinta 3m²

print(f"A área a ser pintada do aposento é de {area_pintada}m², sendo necessarias "
      f"{ceil(quantidade_latas)} latas de tinta para realizar a pintura nas paredes.")
# quantidade de latas deve ser um inteiro
# Teste
# largura = 10, comprimento = 20, litros por lata: 5
# area_paredes = (10*2.8)*2 + (20*2.8)*2 = 56 + 112 = 168
# area porta = 1,68
# area a ser pintada = 166,32
# quantidade latas = 1 litros pinta 3m². logo sera necessarios 166,32/3 litros = 55,44
# cada lata tem 5 litros, logo serão necessárias 11.088 latas de tinta. como lata se compra
# por unidade, serao necessarias 12 latas.