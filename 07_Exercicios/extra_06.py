def valor_pgto(valor, forma_pgto):
    if forma_pgto == 1:  # PIX
        resultado = valor - (valor * 0.15)
    elif forma_pgto == 2:  # À Vista
        resultado = valor - (valor * 0.10)
    elif forma_pgto == 3:  # Parcelado em 2x sem juros
        resultado = valor
    elif forma_pgto == 4:  # Parcelado em 3x ou mais com juros
        resultado = valor + (valor * 0.10)
    else:
        return "Opção inválida."

    return resultado  # Agora a função retorna o valor final


def test():
    assert valor_pgto(100, 1) == 85
    assert valor_pgto(100, 2) == 90
    assert valor_pgto(100, 3) == 100
    assert valor_pgto(100, 4) == 110
    assert valor_pgto(100, 5) == "Opção inválida."
