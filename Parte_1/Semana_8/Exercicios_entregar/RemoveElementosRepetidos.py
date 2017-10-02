def remove_repetidos (valLista):
    l = []
    for i in valLista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

lista = [22, 44, 66, 22, 44, 66]
resultado = remove_repetidos(lista)
print(resultado)
