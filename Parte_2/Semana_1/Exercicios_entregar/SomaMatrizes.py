def soma_matrizes(m1, m2):
    if(len(m1) != len(m2) or len(m1[0]) != len(m2[0])):
        return False
    matriz = []
    for i in range(len(m1)):
        matriz.append([])
        for j in range(len(m1[0])):
            matriz[i].append(m1[i][j] + m2[i][j])
    return matriz


def chamada_soma():
    #m1 = [[1, 2, 3], [4, 5, 6]]
    #m2 = [[2, 3, 4], [5, 6, 7]]
    m1 = [[1], [2], [3]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    return soma_matrizes(m1, m2)
