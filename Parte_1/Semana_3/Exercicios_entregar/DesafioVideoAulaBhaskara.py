import math

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = b ** 2 - 4 * a * c
if delta == 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    print('a raiz desta equação é', int(raiz1))
else:
    if delta < 0:
        print('esta equação não possui raízes reais')
    else:
        x = (-b + math.sqrt(delta)) / (2 * a)
        y = (-b - math.sqrt(delta)) / (2 * a)
        if (x > y):
            print('as raízes da equação são',int(y), 'e', int(x))
        else:
            print('as raízes da equação são',int(x), 'e', int(y))
