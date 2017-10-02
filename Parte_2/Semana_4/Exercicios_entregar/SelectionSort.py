def ordena(lista):
    for i in reversed(range(len(lista))):
        val = 0
        for j in range(1, i + 1):
            if lista[j] > lista[val]:
                val = j
        lista[i], lista[val] = lista[val], lista[i]
    return lista
