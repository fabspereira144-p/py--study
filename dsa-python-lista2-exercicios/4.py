# Dada uma lista de números, crie uma nova lista usando list comprehension que contenha o quadrado de cada número par da lista original.

numeros_lista = [1, 2, 3, 4, 5, 6, 7]
numeros_square = [x ** 2 for x in numeros_lista]

print(f"Lista: {numeros_lista}")
print(f"Lista ao quadrado: {numeros_square}")