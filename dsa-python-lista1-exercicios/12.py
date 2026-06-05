#Crie uma lista chamada compras com os seguintes itens: "arroz", "feijão", "macarrão", "carne". Imprima a lista.

compras = ["arroz", "feijão", "macarrão", "carne"]
print(f"Lista de compras: {compras}")

compras.append("leite")
print(f"Lista atualizada: {compras}")

print(f"Segundo item da lista: {compras[1]}")

compras.remove("macarrão")
print(f"Lista atualizada: {compras}")