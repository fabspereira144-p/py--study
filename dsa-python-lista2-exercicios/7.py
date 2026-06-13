#Crie uma função que receba uma lista de números inteiros e retorne um dicionário contendo a contagem de quantos números são pares e quantos são ímpares.

def contar_impares_pares(listNum):
    pares = 0
    impares = 0

    for numeros in listNum:
        if numeros % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    dic_numeros = {
        "Pares": pares,
        "Ímpares": impares
    }
    
    return dic_numeros

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"{contar_impares_pares(num)}")