def encontra_impares(lista, tamanho=0, impares=[]):
    if tamanho == len(lista):
        return sorted(impares)
    else:
        valor = lista[tamanho]
        if valor % 2 == 0:
            return encontra_impares(lista, tamanho + 1, impares)
        else:
            impares.append(valor)
            return encontra_impares(lista, tamanho + 1, impares)
