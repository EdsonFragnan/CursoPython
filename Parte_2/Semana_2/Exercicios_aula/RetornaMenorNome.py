def mais_curto(lista):
    for i in lista:
        tamanhoPalavra = len(i)
        for j in lista:
            if tamanhoPalavra < len(j):
                print(i)


lista_de_nomes = ["ana", "josé", "Arquibaldo"]
mais_curto(lista_de_nomes)

#testa_mais_curto()
