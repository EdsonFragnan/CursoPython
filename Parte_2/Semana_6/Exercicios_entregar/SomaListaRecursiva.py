def soma_lista(lista, tamanho=0, soma=0):
    if tamanho == len(lista):
        return soma
    else:
        soma += lista[tamanho]
        return soma_lista(lista, tamanho + 1, soma)
