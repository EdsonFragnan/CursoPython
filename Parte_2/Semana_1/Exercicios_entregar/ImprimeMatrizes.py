def imprime_matriz(mat):
    linhas = len(mat)
    colunas = len(mat[0])
    for i in range(linhas):
        for j in range(colunas):
            if(j == colunas - 1):
                print("%d" %mat[i][j])
            else:
                print("%d" %mat[i][j], end = " ")
    print()
