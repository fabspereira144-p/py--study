#Maniupulação de String
frase = " Python é uma linguagem poderosa e estou aprendendo com a DSA. "
frase_sem_espacos = frase.strip()

print(f"Frase sem espaços: \n{frase_sem_espacos}")

print(f"Frase em maiúsculo: \n{frase_sem_espacos.upper()}")

print(f"Frase em minúsculo: \n{frase_sem_espacos.lower()}")

print(f"Trocando 'poderosa' por 'incrível': {frase_sem_espacos.replace('poderosa', 'incrível')}")

print(f"Tamanho da frase: {len(frase_sem_espacos)}")

print(f"{frase_sem_espacos[0:6]}")