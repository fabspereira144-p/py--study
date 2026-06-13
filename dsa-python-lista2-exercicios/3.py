#Você recebeu um dicionário com os nomes dos alunos e suas respectivas notas. Escreva uma função que calcula a média da turma e retorna uma lista com os nomes dos alunos que tiveram nota acima da média.

def acima_da_media(alunos):
    media = sum(alunos.values()) / len(alunos)

    resultado = []
    for nome, nota in alunos.items():
        if nota > media:
            resultado.append(nome)
    
    return resultado

notas_alunos = {
    "Fabrício" : 90,
    "Louise": 80,
    "Rafael": 70,
}

print(f"Alunos acima da média: {acima_da_media(notas_alunos)}")


"""
Funções usadas:
.values(): retorna os valores;
.sum(): soma os valores;
.len(): tamanho da lista;
.append(): adiciona um elemento ao final da lista
"""
