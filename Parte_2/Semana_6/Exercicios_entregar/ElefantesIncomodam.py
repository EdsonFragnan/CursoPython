def elefantes(n, n2=1, frase=''):
    if n < 2:
        return ''
    else:
        incomodamQuantidade = incomodam(n2)
        if n2 == 1:
            frase+= 'Um elefante incomoda muita gente'
            return elefantes(n, n2 + 1, frase)
        elif n >= 3:
            frase+= '\n{} elefantes {} muito mais'.format(str(n2), incomodamQuantidade[:-1])
            frase+= '\n{} elefantes incomodam muita gente'.format(str(n2))
            return elefantes(n - 1, n2 + 1, frase)
        elif n == 2:
            frase+= '\n{} elefantes {} muito mais'.format(str(n2), incomodamQuantidade[:-1])
            return frase

def incomodam(n, palavra='incomodam '):
    if n < 1 or type(n) != int:
        return ''
    if n > 1:
        palavra += 'incomodam '
        return incomodam(n - 1, palavra)
    else:
        return palavra
