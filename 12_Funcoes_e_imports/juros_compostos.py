def calcular_juros_compostos(principal, taxa, tempo):
    investimento = principal * ((1 + taxa) ** tempo)
    return investimento

from op_math import *
def calcular_juros_compostos_recursivo(principal, taxa, tempo):
    if principal == 0:
        return 1
    else:
     return principal * ((1 + taxa) ** tempo)
   


def test():
    assert calcular_juros_compostos(1000, 0.05, 5) == 1276.2815625000003
    assert calcular_juros_compostos(1000, 0.05, 10) == 1628.894626777442
    assert calcular_juros_compostos(1000, 0.05, 0) == 1000

    assert calcular_juros_compostos_recursivo(1000, 0.05, 5) == 1276.2815625000003
    assert calcular_juros_compostos_recursivo(1000, 0.05, 10) == 1628.894626777442
    assert calcular_juros_compostos_recursivo(1000, 0.05, 0) == 1000
