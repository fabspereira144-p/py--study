#Crie uma função chamada dsa_calcula_imc que aceite dois argumentos: peso (em kg) e altura (em metros). A função deve calcular o Índice de Massa Corporal (IMC) usando a fórmula IMC=peso/altura^2 e retornar o valor do IMC.

def dsa_calcula_imc(peso, altura):
    calculo_imc = peso / altura ** 2
    return calculo_imc

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
print(f"Seu IMC é: {dsa_calcula_imc(peso, altura):.2f}");