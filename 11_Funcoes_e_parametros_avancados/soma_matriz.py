def soma_matriz(matriz, alvo):
    soma = sum(sum(linha) for linha in matriz) 
    return soma == alvo

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

def test():
    assert soma_matriz(matriz, 20)
    assert not soma_matriz(matriz, 18)
    assert not soma_matriz(matriz, 21)
    assert not soma_matriz(matriz, 22)
