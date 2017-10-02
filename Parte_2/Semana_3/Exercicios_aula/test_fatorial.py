def fatorial(n):
    if n < 0:
        return 0
    i = fat = 1
    while i <= n:
        fat = fat * i
        i = i + 1
    return fat

import pytest

@pytest.mark.parametrize("entrada, esperado", [
    (0, 1),
    (1, 1),
    (-10, 0),
    (4, 24),
    (5, 120)
])

def testa_fatorial(entrada, esperado):
    assert fatorial(entrada) == esperado

#def testa_fatorial():
#    if fatorial(1) == 1:
#        print('Funciona para 1')
#    else:
#        print('Não funciona para 1')
#    if fatorial(2) == 2:
#        print('Funciona para 2')
#    else:
#        print('Não funciona para 2')
#    if fatorial(0) == 1:
#        print('Funciona para 0')
#    else:
#        print('Não funciona para 0')
#    if fatorial(5) == 120:
#        print('Funciona para 5')
#    else:
#        print('Não funciona para 5')
