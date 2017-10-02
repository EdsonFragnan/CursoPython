def primeiro_lex(lista):
    palavra = sorted(lista)
    return palavra[0]

print(primeiro_lex(['maria', 'josé', 'PAULO', 'Catarina']))
