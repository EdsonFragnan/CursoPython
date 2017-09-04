def trataArray(lista):
    for i in lista:
        valor2 = i
        print(valor2)

def inverte_sequencia(valLista):
    valor = 0
    val = 0
    for i in valLista:
        valor = valLista[::-1]
    trataArray(valor)

array_val = []
def criaArray(val):
    if val == 0:
        inverte_sequencia(array_val)
    else:
        array_val.append(val)
        entrada = int(input('Digite um número: '))
        criaArray(entrada)

valores = int(input('Digite um número: '))
criaArray(valores)
