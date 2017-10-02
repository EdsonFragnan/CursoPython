#carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
#carnes2 = []
#for cns in carnes:
#    carnes2.append(cns)
#carnes2.append("ponta de alcatra")

#print(carnes)
#print(carnes2)

#carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
#carnes2 = carnes[:]
#carnes2.append("ponta de alcatra")
#print(carnes)
#print('\n')
#print(carnes2)

#carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
#carnes2 = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]
#if "ponta de alcatra" in carnes:
#    print("XXX")
#else:
#    if "ponta de alcatra" in carnes2:
#        print("YYY")
#    else:
#        print("ZZZ")

#carnes1 = ["picanha", "alcatra"]
#carnes2 = ["filé mignon", "cupim", "ponta de alcatra"]
#carnes3 = carnes2 + carnes1

#print(carnes1)
#print(carnes2)
#print(carnes3)

#pares = [ 2, 4, 6, 8, 10]
#x = pares * 3
#print(x)

#carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
#x = carnes
#del (x[-1])
#print(carnes)
#print(x)

lista1 = ["carro", "ônibus", "barco", "bicicleta"]
lista2 = ["carro", "ônibus", "barco", "bicicleta"]
lista3 = ["carro", "barco"]

print(lista3 == lista1)
print(lista1 is lista2)
print(lista2 == lista1)
print(lista3 is lista2)
print(lista1 is lista3)
print(lista2 is lista3)
