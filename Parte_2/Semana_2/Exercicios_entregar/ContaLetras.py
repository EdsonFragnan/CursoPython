def conta_letras(frase, contar='vogais'):
    vogais = ['a', 'e', 'i', 'o', 'u']
    arrayLetras = []
    totalVogaisConsoantes = []
    if contar == 'vogais':
        for i in frase:
            for j in vogais:
                if j == i:
                    totalVogaisConsoantes += j
    else:
        if contar == 'consoantes':
            for z in frase:
                arrayLetras += z.strip()

            for i in frase:
                for j in vogais:
                    if j == i:
                        totalVogaisConsoantes += j

    valor = len(arrayLetras) - len(totalVogaisConsoantes)
    if valor < 0:
        return abs(valor)
    else:
        return valor
