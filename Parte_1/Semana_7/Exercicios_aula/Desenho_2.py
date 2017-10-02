altura = 5
linha = 1
while linha <= altura:
    print("*", end = "\t")
    coluna = 2
    while coluna < altura:
        if linha == 1 or linha == altura:
            print("*")
        else:
            print(end = " ")
        coluna = coluna + 1
        print("*", end = "")
    linha = linha + 1
