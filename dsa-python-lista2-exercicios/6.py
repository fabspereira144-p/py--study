#Você tem uma lista de dicionários, onde cada dicionário representa uma pessoa com nome e idade. Use a função sorted() com uma expressão lambda como chave (key) para ordenar a lista de pessoas da mais nova para a mais velha.

pessoas = [
    {"nome": "Ana", "idade": 25},
    {"nome": "Bruno", "idade": 18},
    {"nome": "Carlos", "idade": 30},
    {"nome": "Daniela", "idade": 22}
]

pessoas_ordenadas = sorted(pessoas, key=lambda pessoa: pessoa["idade"])
print(f"{pessoas_ordenadas}")

#O parâmetro key= serve para dizer ao Python qual valor deve ser usado para comparar e ordenar os elementos.

