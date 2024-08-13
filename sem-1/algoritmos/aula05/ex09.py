h_degrau = float(input("Digite a altura de cada degrau em cm: "))
h_target = float(input("Digite a altura que deseja alcançar em m: "))

h_target*=100
degraus = h_target//h_degrau + 1 if h_target//h_degrau != h_target/h_degrau else h_target/h_degrau
print(f"Para andar {h_target/100}m em uma escada com degraus de {h_degrau}cm de altura,"
      f"você deve subir {degraus} degraus.")
# Como não tem como subir uma quantidade decimal de degraus, arredonda-se para cima, para que a
# altura objetivo seja alcançada.