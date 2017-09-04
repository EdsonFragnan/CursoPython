def fizzbuzz(numero):
    if (numero % 3 == 0 and numero % 5 == 0):
        return 'FizzBuzz'
    else:
        if numero % 3 == 0:
            return 'Fizz'
        else:
            if numero % 5 == 0:
                return 'Buzz'
            else:
                if numero % 3 != 0 and numero % 5 != 0:
                    return numero


def test_fizzbuzz_FizzBuzz():
    assert fizzbuzz(3) == 'Fizz'

def test_fizzbuzz_Fizz():
    assert fizzbuzz(5) == 'Buzz'

def test_fizzbuzz_Buzz():
    assert fizzbuzz(15) == 'FizzBuzz'

def test_fizzbuzz_():
    assert fizzbuzz(4) == 4
