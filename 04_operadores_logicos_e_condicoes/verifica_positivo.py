def eh_positivo(valor):
   if valor > 0:
      return True
   else:
      return False

def eh_negativo(valor):
      return not eh_positivo(valor)

def test():
    
    assert eh_positivo(1)
    assert eh_positivo(2)
    assert eh_positivo(10)
    assert not eh_positivo(0)
    assert not eh_positivo(-1)
    assert not eh_positivo(-10)

    assert eh_negativo(-1)
    assert eh_negativo(-2)
    assert eh_negativo(-10)
    assert not eh_negativo(0)
    assert not eh_negativo(1)
    assert not eh_negativo(10)

print(numero eh_negativo)
print(numero eh_positivo)