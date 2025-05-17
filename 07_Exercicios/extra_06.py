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

# Interface interativa separada do cálculo
if valor_pgto:
    valor = float(input("Digite o valor a ser pago: "))
    print("Formas de pagamento:\n1 - PIX\n2 - À Vista\n3 - Parcelado em 2x sem juros\n4 - Parcelado em 3x ou mais com juros")
    forma_pgto = int(input("Digite o número correspondente à forma de pagamento: "))
    
    resultado = valor_pgto(valor, forma_pgto)
    print(f"Valor final: {resultado}" if isinstance(resultado, float) else resultado)

# Testes automatizados
def test():
    assert valor_pgto(100, 1) == 85
    assert valor_pgto(100, 2) == 90
    assert valor_pgto(100, 3) == 100
    assert valor_pgto(100, 4) == 110