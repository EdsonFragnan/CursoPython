def busca(lista, x):
        primeiro = 0
        ultimo = len(lista) - 1

        while primeiro <= ultimo:
            meio = (primeiro + ultimo)//2
            if lista[meio] == x:
                print(meio)
                return meio
            else:
                if x < lista[meio]:
                    print(meio)
                    ultimo = meio - 1
                else:
                    print(meio)
                    primeiro = meio + 1
        return False
