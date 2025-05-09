def eh_bissexto(ano):
    if (ano % 4 == 0):
        return True
    else:
        return False

#solução professor
def proximo_bissexto(ano):
    return(ano + 3) // 4 * 4 


def test():
    
    assert eh_bissexto(0)
    assert eh_bissexto(2020)
    assert eh_bissexto(2024)

    assert not eh_bissexto(1)
    assert not eh_bissexto(2022)
    assert not eh_bissexto(2023)

    assert proximo_bissexto(2024) == 2024
    assert proximo_bissexto(2025) == 2028
    assert proximo_bissexto(2029) == 2032
    assert proximo_bissexto(2020) == 2020
    
print(eh_bissexto(0))
print(eh_bissexto(2020))
print(eh_bissexto(2024))
