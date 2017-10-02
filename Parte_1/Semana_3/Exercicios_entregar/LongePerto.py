import math

a = int(input('Digite um número para a:'))
b = int(input('Digite um número para b:'))
c = int(input('Digite um número para c:'))
d = int(input('Digite um número para d:'))

distancia = ((a - c)**2) + ((b - d)**2)
if (math.sqrt(distancia) >= 10):
    print('longe')
else:
    print('perto')
