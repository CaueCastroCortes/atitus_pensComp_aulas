"""
Meses sao representados como: 1=Jan, 2=Feb, 3=Mar..
"""

MESES_31_DIAS = [1, 3, 5, 7, 8, 10, 12]
MESES_30_DIAS = [4, 6, 9, 11]


def eh_bissexto(ano: int) -> bool:
    """Verifica se um ano é bissexto."""
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)


def total_dias_no_mes(mes: int, ano: int) -> int:
    """Retorna o número total de dias em um determinado mês e ano."""
    if mes in MESES_31_DIAS:
        return 31
    elif mes in MESES_30_DIAS:
        return 30
    elif mes == 2:
        return 29 if eh_bissexto(ano) else 28
    else:
        raise ValueError("Mês inválido")


assert total_dias_no_mes(1, 2024) == 31
assert total_dias_no_mes(2, 2024) == 29
assert total_dias_no_mes(3, 2024) == 31
assert total_dias_no_mes(11, 2024) == 30


def formata_data(data: list) -> str:
    """Formata uma lista [dia, mes, ano] em uma string 'dia/mes/ano'."""
    dia, mes, ano = data
    return f"{dia}/{mes}/{ano}"


assert formata_data([1, 2, 2024]) == "1/2/2024"
assert formata_data([1, 12, 2024]) == "1/12/2024"


def calcula_diferenca(data1: list, data2: list) -> int:
    """Calcula a diferença em dias entre duas datas."""
    from datetime import date

    d1 = date(data1[2], data1[1], data1[0])
    d2 = date(data2[2], data2[1], data2[0])
    return abs((d2 - d1).days)


# Diferenca em dias entre 2/7/2004 e 27/5/2024 é de 7268 dias
assert calcula_diferenca([2, 7, 2004], [27, 5, 2024]) == 7268
# Diferenca entre 27/5/2024 e 2/7/2089 é de 23779 dias
assert calcula_diferenca([27, 5, 2024], [2, 7, 2004 + 85]) == 23779
# Diferenca entre 2/7/2004 e 2/7/2089 é de 31047 dias
assert calcula_diferenca([2, 7, 2004], [2, 7, 2004 + 85]) == 31047
# A data 27/5/2024 representa 23.409669211195926% entre 2/7/2004 e 2/7/2089


# Diferenca em dias entre 24/7/1991 e 24/10/2024 é de 12146 dias
assert calcula_diferenca([24, 7, 1991], [24, 10, 2024]) == 12146
# Diferenca entre 24/10/2024 e 24/7/2076 é de 18900 dias
assert calcula_diferenca([24, 10, 2024], [24, 7, 1991 + 85]) == 18900
# Diferenca entre 24/7/1991 e 24/7/2076 é de 31046 dias
assert calcula_diferenca([24, 7, 1991], [24, 7, 1991 + 85]) == 31046
# A data 24/10/2024 representa 39.12259228241963% entre 24/7/1991 e 24/7/2076
