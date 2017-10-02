numero = int(input("Digite um numero: "))

anterior = numero % 10
numero = numero // 10;
n_adjacente = False;
pos = 0

while numero > 0 and not n_adjacente:
    atual = numero % 10
    if atual == anterior:
        n_adjacente = True
    else:
        pos += 1
    anterior = atual
    numero = numero // 10

if n_adjacente:
    print('sim')
else:
    print('não')
