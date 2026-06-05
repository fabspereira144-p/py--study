altura = input("Digite sua altura em metros: ")
altura_float = float(altura)
peso = input("Digite seu peso em quilos: ")
peso_float = float(peso)

calc_imc = peso_float / altura_float ** 2

print(f"Seu IMC: {calc_imc:.2f}")