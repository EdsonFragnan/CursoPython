def maximo(a, b, c):
    if a > b > c or a > c > b:
        return a
    else:
        if b > a > c or b > c > a:
            return b
        else:
            if c > a > b or c > b > a:
                return c
            else:
                if a == b == c:
                    return a

def maximo(a, b):
    if a > b:
        return a
    else:
        return b

def test_maximo_a():
    assert maximo(3, 4) == 4

def test_maximo_b():
    assert maximo(0, -1) == 0

def test_maximo_a():
    assert maximo(30, 14, 10) == 30

def test_maximo_b():
    assert maximo(0,-1, 1) == 1

def test_maximo_c():
    assert maximo(7,7,7) == 7
