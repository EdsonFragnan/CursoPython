largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
coluna = ''

def ColunaLargura(coluna, altura):
    while altura >= 1:
        respAltura = coluna
        print(respAltura)
        altura = altura - 1

while largura >= 1:
    coluna += '#'
    largura = largura - 1
ColunaLargura(coluna, altura)
