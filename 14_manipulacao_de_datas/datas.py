from datetime import date

def delta_dias(d1: date, d2: date) -> int:
    """
    Retorna a diferença de dias entre d1 e d2, excluindo o dia final.
    Sempre não-negativo.
    """
    total = abs((d2 - d1).days)
    return max(0, total - 1)


# ---------- Testes ----------
if __name__ == "__main__":
    from datetime import date

    # Exclui o dia final: 01/01/2025 → 02/01/2026 = 366 dias totais → 365
    assert delta_dias(date(2025, 1, 1), date(2026, 1, 2)) == 365

    # Intervalo de 1 dia → 0
    assert delta_dias(date(2025, 1, 1), date(2025, 1, 2)) == 0

    # Mesma data → 0
    assert delta_dias(date(2025, 1, 1), date(2025, 1, 1)) == 0

    # Ordem invertida → mesmo resultado
    assert delta_dias(date(2026, 1, 2), date(2025, 1, 1)) == 365






