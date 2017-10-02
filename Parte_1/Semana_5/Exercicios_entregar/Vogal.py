def vogal(valor):
    if valor.lower() == 'a' or valor.lower() == 'e' or valor.lower() == 'i' or valor.lower() == 'o' or valor.lower() == 'u':
        return True
    else:
        return False

def test_vogalA():
    assert vogal('a') == True

def test_vogalB():
    assert vogal('b') == False

def test_vogalE():
    assert vogal('E') == True
