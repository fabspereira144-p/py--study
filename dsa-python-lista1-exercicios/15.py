#Dicionários

filme = {
    "titulo": "O Poderoso Chefão",
    "ano": 1972,
    "diretor": "Francis Ford Coppola"
}

print(f"Ano de lançamento: {filme["ano"]}")

filme["gênero"] = "drama"
print(f"Dicionário do filme completo: {filme}")

filme["ano"] = 1973
print(f"Ano do filme modificado: {filme["ano"]}")