def multiplica (a, b):
    return a * b

print(multiplica(4,5))


def troca(x, y):
    aux = x
    x = y
    y = aux

x = 10
y = 20
troca (x,y)
print("x =", x,"e y =",y)

def total_Caracteres1 (x, y, z):
    print(len(x)+len(y)+len(z))

def total_Caracteres2 (x, y, z):
    print(sum(len(x)+len(y)+len(z)))

def total_Caracteres3 (x, y, z):
    print(sum(len(x,y,z)))

def total_Caracteres4 (x, y, z):
    print(len(x,y,z))

total_Caracteres1('teste_1_', 'teste_1_', 'teste_1')
total_Caracteres2('teste_2_', 'teste_2_', 'teste_2')
total_Caracteres3('teste_3_', 'teste_3_', 'teste_3')
total_Caracteres4('teste_4_', 'teste_4_', 'teste_4')

import math

def suspense(x):
    print(math.sqrt(x))

suspense(10)

def leitura():
    x = int(input("Digite um valor: "))
    while x <= 0:
        x = int(input("Digite um valor: "))
    print(x)

leitura():
    x = -1
    while x > 0:
        x = int(input("Digite um valor: "))
    return x


leitura():
    x = -1
    while x <= 0:
        x = int(input("Digite um valor: "))
    return x


def leitura():
    x = -1
    while x > 0:
        x = int(input("Digite um valor: "))
    return x

def leitura():
    x = -1
    while x <= 0:
        x = int(input("Digite um valor: "))
    print(x)

leitura()
