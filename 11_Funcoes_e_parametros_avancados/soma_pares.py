def soma_pares(numeros: list, alvo: int) -> bool:
    for i in range(len(numeros)):
        for j in range(i + 1, len(numeros)):  # Evita somar o mesmo número duas vezes
            if numeros[i] + numeros[j] == alvo:
                return True
    return False

def test():
    assert soma_pares([1, 2], 4)
    assert not soma_pares([8], 1)
    assert not soma_pares([8], 10)
    assert soma_pares([3, 4, 6], 9)
    assert soma_pares([3, 4, 6], 7)
