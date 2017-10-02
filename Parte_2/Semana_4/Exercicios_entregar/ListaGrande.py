def lista_grande(n):
    import random
    listaDados = []
    for i in range(n):
        listaDados.append(i*n)

    random.shuffle(listaDados)
    return listaDados
