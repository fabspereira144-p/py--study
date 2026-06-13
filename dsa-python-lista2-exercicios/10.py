#Crie um jogo onde o computador escolhe um número secreto entre 1 e 20. O jogador tem 5 tentativas para adivinhar. A cada tentativa, o programa informa se o palpite foi muito alto ou muito baixo. Se o jogador acertar, o loop deve ser interrompido com uma mensagem de vitória.

import random 

numero_secreto = random.randint(1, 20) #random.randint(inicio, fim)

acertou = False

for i in range(5):
    palpite = int(input("Digite um número: "))

    if (palpite == numero_secreto):
        print("Você acertou o número secreto!")
        acertou = True
        break
    elif palpite > numero_secreto:
        print("Muito alto!")
    else:
        print("Muito baixo!")

if not acertou:
    print("Você não acertou o número secreto!")