#Variável acumuladora
total_de_jogos = 1

while(True):
    #Apresentação do jogo
    print("-" * 52)
    print("--- Jogo Pedra, Papel ou Tesoura (2 Jogadores) ---")
    print("--- Cada Jogador deve escolher uma das opções! ---")
    print("-" * 52)

    # Usamos tupla pois não podemos alterar as opções válidas
    opcoes_validas = ("pedra", "papel", "tesoura")
    print(f"Opções válidas: {opcoes_validas}")
    print("-" * 52)

    jogada_jogador1_inicial = input("Jogador 1, digite a sua jogada: ") 
    jogada_jogador2_inicial = input("Jogador 2, digite a sua jogada: ") 

    #Os espaçõs das respostas são e transformados em minúsculos
    jogada_jogador1 = jogada_jogador1_inicial.lower().strip()
    jogada_jogador2 = jogada_jogador2_inicial.lower().strip()

    print("-" * 25)
    print(f"Jogador 1 escolheu: {jogada_jogador1}")
    print(f"Jogador 2 escolheu: {jogada_jogador2}")
    print("-" * 25)

    #Caso 1: Opções de entrada inválidos
    if jogada_jogador1 not in opcoes_validas or jogada_jogador2 not in opcoes_validas:
        print("Uma ou ambas as jogadas são inválidas! Use apenas 'pedra', 'papel' ou 'tesoura'!")

    #Caso 2: Empate
    elif jogada_jogador1 == jogada_jogador2:
        print("Resultado: É um empate!")

    #Caso 3: Jogador 1 vence
    elif (jogada_jogador1 == "pedra" and jogada_jogador2 == "tesoura") or \
        (jogada_jogador1 == "tesoura" and jogada_jogador2 == "papel") or \
        (jogada_jogador1 == "papel" and jogada_jogador2 == "pedra"):
        print("Resultado: Jogador 1 venceu! Parabéns!")

    #Caso 4: Jogador 2 vence
    else:
        print("Resultado: Jogador 2 venceu! Parabéns!")

    #Pergunta se os jogadores querem jogar novamente
    resposta = input("Vocês desejam jogar novamente? (s/n): ")

    #Os espaçõs das respostas são e transformados em minúsculos
    resposta_convertida = resposta.strip().lower()

    #Caso 1: o loop se repete
    if resposta_convertida == "s":
        total_de_jogos+=1
        continue
        
    #Caso 2: o loop é encerrado
    else:
        break

print("Fim de Jogo!")
print(f"Total de vezes jogadas: {total_de_jogos}")