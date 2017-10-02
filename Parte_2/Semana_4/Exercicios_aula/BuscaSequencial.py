#def busca_sequencial(seq, x):
#    for i in range(len(seq)):
#        if seq[i] == x:
#            return i
#    return -1


#def busca_sequencial(seq, x):
#    for i in range(len(seq)):
#        print('AQUI')
#        if seq[i] == x:
#            return True
#    return False

#numeros = [55,33,0,900,-432,10,77,123,11]

def selecao_direta(lista):
    fim = len(lista)
    for i in range(fim-1):
        pos_menor = i
        for j in range(i+1,fim):
            print()
            if lista[j] < lista[pos_menor]:
                pos_menor = j
        lista[i],lista[pos_menor] = lista[pos_menor],lista[i]
        print(lista)
    return lista
