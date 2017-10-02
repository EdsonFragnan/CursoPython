valor = int(input('Digite um número inteiro: '))
primo = True
divisor = 2

while divisor < valor and primo:
        if valor % divisor == 0:
            primo = False
        divisor += 1

if primo and valor != 1:
    print('primo')
else:
    print('não primo')
