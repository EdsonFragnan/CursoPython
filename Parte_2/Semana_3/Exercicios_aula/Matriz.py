def cria_matriz(num_linhas, num_colunas):
    ''' (int, int) -> matriz (lista de listas)
    Cria e retorna uma matriz com num_linhas linhas e num_colinas
    colunas em que cada elemento é digitado pelo usuário.
    '''
    matriz = [] # lista vazia
    for i in range(num_linhas):
        # cria a linha vazia i
        linha = [] # lista vazia
        for j in range(num_colunas):
            linha.append(j)
            # adiciona linha à matriz
        matriz.append(linha)
    return matriz
