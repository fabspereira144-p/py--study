#Uma lista de frases, use a função map() em conjunto com uma expressão lambda para criar uma nova lista onde cada frase é convertida para letras maiúsculas e tem a palavra "PYTHON" anexada ao final.

frases = [
    "Python é uma linguagem muito versátil.",
    "A prática diária ajuda a aprender programação.",
    "List comprehensions tornam o código mais conciso.",
    "Funções ajudam a reutilizar código.",
    "Resolver exercícios fortalece a lógica de programação."
]

frases_filtradas = list(map(lambda frase: frase.upper() + "PYTHON", frases)) #Pra cada frase na lista de frases...
print(frases_filtradas)

#map tem dois parâmetros: a função, e onde a função deve ser aplicada