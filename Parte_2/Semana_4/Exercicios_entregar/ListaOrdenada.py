def ordenada(lista):
    fim = len(lista)
    listaVal = []
    for i in range(fim - 1):
        posicao_do_minimo = i
        for j in range(i+1, fim):
            if lista[j] < lista[posicao_do_minimo]:
                listaVal.append(False)
            else:
                listaVal.append(True)

    for k in listaVal:
        if k == False:
            return False
    return True
