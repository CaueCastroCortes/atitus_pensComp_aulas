def calcula_classe_social(salarios, salario_minimo):
    """Calcula a classe social com base na renda média em relação ao salário mínimo."""
    if not salarios:
        return "Lista de salários está vazia."

    media = sum(salarios) / len(salarios)  # Calcula a média salarial
    renda_em_salarios_minimos = media / salario_minimo  # Converte para múltiplos do salário mínimo

    # Classificação social baseada na renda
    if renda_em_salarios_minimos <= 1:
        return "E"
    elif renda_em_salarios_minimos <= 2:
        return "D"
    elif renda_em_salarios_minimos <= 4:
        return "C"
    elif renda_em_salarios_minimos <= 10:
        return "B"
    else:
        return "A"

# Exemplo de uso sem input()
salarios_exemplo = [2000, 3000, 2500, 4000]  # Lista fixa de salários
salario_minimo_exemplo = 1300  

classe_social = calcula_classe_social(salarios_exemplo, salario_minimo_exemplo)
print(f"A classe social é: {classe_social}")


def test(): 
    assert calcula_classe_social([], 1000) is None
    assert calcula_classe_social([1000], 1000) == "E"
    assert calcula_classe_social([500], 1000) == "E"
    assert calcula_classe_social([500], 1000) == "E"
    assert calcula_classe_social([1000, 0], 900) == "E"
    assert calcula_classe_social([1000], 900) == "D"
    assert calcula_classe_social([10000, 15000], 1000) == "B"
    assert calcula_classe_social([20000, 25000], 1000) == "A"
    assert calcula_classe_social([20000, 0, 0, 0, 0], 1000) == "C"
