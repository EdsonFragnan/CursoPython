def dimensoes(matriz):
    val_matriz = (len(matriz), len(matriz[0]))
    print('{}X{}'.format(val_matriz[0], val_matriz[1]))

def chama_dimensao():
    minha_matriz = [[1], [2], [3]]
    dimensoes(minha_matriz)
