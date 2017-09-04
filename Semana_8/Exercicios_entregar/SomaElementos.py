def soma_elementos(valLista):
    soma = 0
    for i in valLista:
        soma = soma + i
    return soma

lista = [22, 44, 66]
resultado = soma_elementos(lista)
print(resultado)
