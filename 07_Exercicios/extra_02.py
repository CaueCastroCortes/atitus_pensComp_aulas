def maior_numero(lista):
    """Retorna o maior número da lista."""
    return max(lista)

def menor_numero(lista):
    """Retorna o menor número da lista."""
    return min(lista)

def numeros_pares(lista):
    """Retorna uma lista com os números pares encontrados na lista."""
    return [numero for numero in lista if numero % 2 == 0]

def numeros_impares(lista):
    """Retorna uma lista com os números ímpares encontrados na lista."""
    return [numero for numero in lista if numero % 2 != 0]

def numeros_positivo(lista):
    """
    Retorna uma lista com os números positivos da lista.
    Aqui, consideramos o zero como positivo conforme os asserts.
    """
    return [numero for numero in lista if numero >= 0]

def numeros_negativos(lista):
    """Retorna uma lista com os números negativos da lista."""
    return [numero for numero in lista if numero < 0]

def soma_numeros(lista):
    """Retorna a soma de todos os números da lista."""
    return sum(lista)


# Listas para os testes
lista_1 = [10, 0, -3, 42, 5, -6, 8, 91]
lista_2 = [20, 2, 27, 74, 19, 85, 3, 22, 95, 11]
lista_3 = [45, 92, 23, 17, 50, 89, 57, 15, 28, 5]


def test():
    # Testes para o maior número
    assert maior_numero(lista_1) == 91
    assert maior_numero(lista_2) == 95
    assert maior_numero(lista_3) == 92

    # Testes para o menor número
    assert menor_numero(lista_1) == -6
    assert menor_numero(lista_2) == 2
    assert menor_numero(lista_3) == 5

    # Testes para números pares
    assert numeros_pares(lista_1) == [10, 0, 42, -6, 8]
    assert numeros_pares(lista_2) == [20, 2, 74, 22]
    assert numeros_pares(lista_3) == [92, 50, 28]

    # Testes para números ímpares
    assert numeros_impares(lista_1) == [-3, 5, 91]
    assert numeros_impares(lista_2) == [27, 19, 85, 3, 95, 11]
    assert numeros_impares(lista_3) == [45, 23, 17, 89, 57, 15, 5]

    # Testes para números positivos (incluindo o zero)
    assert numeros_positivo(lista_1) == [10, 0, 42, 5, 8, 91]
    assert numeros_positivo(lista_2) == [20, 2, 27, 74, 19, 85, 3, 22, 95, 11]
    assert numeros_positivo(lista_3) == [45, 92, 23, 17, 50, 89, 57, 15, 28, 5]

    # Testes para números negativos
    assert numeros_negativos(lista_1) == [-3, -6]
    assert numeros_negativos(lista_2) == []
    assert numeros_negativos(lista_3) == []

    # Testes para a soma dos números
    assert soma_numeros(lista_1) == 147
    assert soma_numeros(lista_2) == 358
    assert soma_numeros(lista_3) == 421

    print("Todos os testes passaram com sucesso!")
