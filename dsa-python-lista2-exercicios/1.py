#Escreva uma função que receba os valores de três lados de um triângulo e o classifique como "Equilátero" (todos os lados iguais), "Isósceles" (dois lados iguais) ou "Escaleno" (todos os lados diferentes).

a = float(input("Primeiro lado do triângulo: "))
b = float(input("Segundo lado do triângulo: "))
c = float(input("Terceiro lado do triângulo: "))

if a + b > c and a + c > b and b + c > a:
    print("Os valores formam um triângulo")

    #Todos os lados iguais
    if a == b == c:
        print("\n Triângulo equilátero")
    #Dois lados iguais
    elif a == b or b == c or a == c:
        print("\nTriângulo isósceles.")
    #Lados diferentes
    else:
        print("Triângulo escaleno")

else:
    print("Os valores informados não formam um triângulo")