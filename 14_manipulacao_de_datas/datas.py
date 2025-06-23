# parcelamento.py

from datetime import date
import calendar

def _add_months(orig: date, months: int) -> date:
    """
    Soma 'months' meses à data 'orig', mantendo o dia original
    ou jogando para o último dia do mês de destino se não existir.
    """
    y = orig.year + (orig.month - 1 + months) // 12
    m = (orig.month - 1 + months) % 12 + 1
    day = min(orig.day, calendar.monthrange(y, m)[1])
    return date(y, m, day)


def parcelamento(valor: int, n: int, data_inicio: date) -> list[list]:
    """
    Divide 'valor' em 'n' parcelas iguais (inteiras), jogando
    o resto para a última parcela, e fixa cada vencimento
    para data_inicio + i meses (i=0..n-1).
    Retorna lista de [valor_parcela, data_vencimento].
    """
    base = valor // n
    resto = valor % n
    parcelas = []
    for i in range(n):
        valor_i = base + (resto if i == n - 1 else 0)
        venc = _add_months(data_inicio, i)
        parcelas.append([valor_i, venc])
    return parcelas


def test_parcelamento():
    from datetime import date

    # Exemplo: 100 em 3x a partir de 31/01/2025
    # → [33,31/01], [33,28/02], [34,31/03]
    esperado = [
        [33, date(2025, 1, 31)],
        [33, date(2025, 2, 28)],
        [34, date(2025, 3, 31)],
    ]
    assert parcelamento(100, 3, date(2025, 1, 31)) == esperado


if __name__ == "__main__":
    test_parcelamento()
    print("✅ parcelamento.py: todos os testes passaram!")



