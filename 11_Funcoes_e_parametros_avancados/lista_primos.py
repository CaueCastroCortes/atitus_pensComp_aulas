def lista_primos(numero):
    result = []
    for x in range(valor + 1):
        if eh_primo(x):
            result.append(x)
    return result

def test():

assert lista_primos(10) == [2, 3, 5, 7]
assert lista_primos(13) == [2, 3, 5, 7, 11, 13]
assert lista_primos(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
