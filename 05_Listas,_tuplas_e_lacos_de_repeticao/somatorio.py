def somatorio(numero):
    if numero < 0:
       return None
    resultado = 0 
    for numero in range(1, numero + 1):
        resultado += numero
    return resultado

    # Preencher com um laço e 
    # Somar em 'resultado' algo

def test():
    assert somatorio(-1) is None
    assert somatorio(0) == 0
    assert somatorio(1) == 1
    assert somatorio(2) == 3
    assert somatorio(3) == 6
    assert somatorio(4) == 10
    assert somatorio(5) == 15
    assert somatorio(6) == 21
    assert somatorio(7) == 28
    assert somatorio(8) == 36
    assert somatorio(9) == 45

print(somatorio(9))   
