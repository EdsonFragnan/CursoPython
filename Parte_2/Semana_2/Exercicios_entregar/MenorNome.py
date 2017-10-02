def menor_nome(nomes):
    novaLista = []
    for d in nomes:
        novaLista.append(d.strip())

    tamNomes = [len(s) for s in novaLista]
    tamNomes2 = []
    for i in novaLista:
        tamNomes2.append(i)

    lista_final = list(set(tamNomes) - set(tamNomes2))
    valorNomes = [j for j in lista_final if lista_final.count(i) < 2]
    menorNome = min(valorNomes)
    for z in novaLista:
        if len(z) <= menorNome:
            return z.capitalize()
