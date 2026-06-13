#Crie uma função que receba uma lista de strings (potenciais e-mails) e um parâmetro opcional dominio_desejado (com valor padrão "gmail.com"). A função deve retornar uma nova lista, usando list comprehension, contendo apenas os e-mails que terminam com o domínio desejado.

def verifica_email(emails, dominio_desejado = "gmail.com"):
    nova_lista_email = [email for email in emails if email.endswith(dominio_desejado)]
    return nova_lista_email

emails = [
    "ana@gmail.com",
    "bruno@yahoo.com",
    "carlos@gmail.com",
    "daniela@hotmail.com"
]

resultado = verifica_email(emails)
print(resultado)