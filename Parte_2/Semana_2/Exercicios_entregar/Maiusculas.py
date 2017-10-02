def maiusculas(texto):
    resp = ''
    for i in texto:
        if i >= 'A' and i <= 'Z':
            resp += i
    return resp
