from datetime import date

def str_to_date(date_str):
    try:
        return datetime.strptime(date_str, '%m-%d-%Y').date()
    except ValueError:


def test():
    assert str_to_date('10-01-2025') == date(day=10, month=1, year=2025)
    assert str_to_date('10-99-2025') is None

def nome_dia_semana(data):
    dias = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo']
    return dias[data.weekday()]

def test():
    assert nome_dia_semana(date(year=2025, month=1, day=1)) == 'quarta-feira'
    assert nome_dia_semana(date(year=2025, month=1, day=2)) == 'quinta-feira'


def dias_para_finde(data):
    return (5 - data.weekday()) % 7

def test():
    assert dias_para_finde(date(year=2025, month=1, day=1)) == 3
    assert dias_para_finde(date(year=2025, month=1, day=2)) == 2


def delta_dias(data_a, data_b):
    return (data_b - data_a).days

def test():
    assert delta_dias(date(year=2025, month=1, day=1), date(year=2026, month=1, day=2)) == 365
    assert delta_dias(date(year=2026, month=1, day=1), date(year=2025, month=1, day=2)) == -365
    assert delta_dias(date(year=2025, month=1, day=1), date(year=2025, month=1, day=2)) == 0


def proximo_mes(data_a):
    prox_mes = data_a.month % 12 + 1
    prox_ano = data_a.year + (data_a.month // 12)
    day = min(data_a.day, (date(prox_ano, prox_mes, 1) - date(prox_ano, prox_mes - 1, 1)).days)
    return date(ano=prox_ano, mes=prox_mes, day=day)

def test():
    assert proximo_mes(date(year=2025, month=1, day=1)) == date(year=2025, month=2, day=1)
    assert proximo_mes(date(year=2025, month=1, day=29)) == date(year=2025, month=2, day=28)
    assert proximo_mes(date(year=2024, month=1, day=29)) == date(year=2024, month=2, day=29)
    assert proximo_mes(date(year=2025, month=1, day=30)) == date(year=2025, month=2, day=28)



def data_futuro(data: date) -> str:
    today = date.today()
    if data > today:
        return 1
    elif data < today:
        return -1
    else:
        return 0

def test():
    assert data_futuro(date(day=1, month=1, year=2099)) == 1
    assert data_futuro(date(day=1, month=1, year=1999)) == -1
    assert data_futuro(date.today()) == 0
