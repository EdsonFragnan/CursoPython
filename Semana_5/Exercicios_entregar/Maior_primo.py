def e_primo(num):
    return all(num%i!=0 for i in range(2,num))

def maior_primo(n):
    for num in reversed(range(1,n+1)):
        if e_primo(num):
            return num

def test_maximo_a():
    assert maior_primo(100) == 97

def test_maximo_b():
    assert maior_primo(7) == 7
