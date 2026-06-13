def multiplicacao(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num * i}")
    print(f"Tabuada de {num} finalizada!")

num_tabuada = int(input("Número para saber a tabuada (1-10): "))
multiplicacao(num_tabuada)