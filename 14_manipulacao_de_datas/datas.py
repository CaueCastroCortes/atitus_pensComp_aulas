from datetime import date

def delta_dias(d1: date, d2: date) -> int:
    """
    Diferença de dias entre d1 e d2, excluindo o dia final.
    Ex: de 01/01/2025 até 02/01/2026 → 365 dias
    """
    total = abs((d2 - d1).days)  
    
    return max(0, total - 1)


def test_delta_dias():
    from datetime import date

    assert delta_dias(date(2025, 1, 1), date(2026, 1, 2)) == 365

    assert delta_dias(date(2025, 1, 1), date(2025, 1, 2)) == 0
    
    assert delta_dias(date(2025, 1, 1), date(2025, 1, 1)) == 0
    
    assert delta_dias(date(2026, 1, 2), date(2025, 1, 1)) == 365


