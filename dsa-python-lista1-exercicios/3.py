#Qual é a principal diferença entre uma variável de escopo local e uma de escopo global?

nome_global = "Fabrício" #global

def chamarNome():
    nome = "Ana" #local
    print(f"Olá, {nome}")
    print(f"Olá, {nome_global}")

print(f"Olá, {nome_global}")

chamarNome()

print(f"Ola, {nome}") #tentando acessar a variável local fora da função