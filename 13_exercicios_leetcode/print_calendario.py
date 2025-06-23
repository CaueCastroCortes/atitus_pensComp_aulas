def imprimir_calendario_mes(dia_inicial: int, total_dias: int):
    cabecalho = "Do.Se.Te.Qu.Qu.Se.Sá"
    linhas = [cabecalho]

    dia = 1
    
    while dia <= total_dias:
        
        vazio = dia_inicial if dia == 1 else 0
        
        qtd = min(7 - vazio, total_dias - dia + 1)

        linha = "..." * vazio
        for _ in range(qtd):
          
            cel = f"{dia:>2}."
            
            cel = cel.replace(" ", ".")
            linha += cel
            dia += 1

        linhas.append(linha.rstrip('.'))
        
        dia_inicial = 0

    return linhas


def test_imprimir_calendario_mes():
    assert imprimir_calendario_mes(0, 31) == [
        "Do.Se.Te.Qu.Qu.Se.Sá",
        ".1..2..3..4..5..6..7",
        ".8..9.10.11.12.13.14",
        "15.16.17.18.19.20.21",
        "22.23.24.25.26.27.28",
        "29.30.31",
    ]

    assert imprimir_calendario_mes(1, 31) == [
        "Do.Se.Te.Qu.Qu.Se.Sá",
        "....1..2..3..4..5..6",
        ".7..8..9.10.11.12.13",
        "14.15.16.17.18.19.20",
        "21.22.23.24.25.26.27",
        "28.29.30.31",
    ]

    assert imprimir_calendario_mes(2, 31) == [
        "Do.Se.Te.Qu.Qu.Se.Sá",
        ".......1..2..3..4..5",
        ".6..7..8..9.10.11.12",
        "13.14.15.16.17.18.19",
        "20.21.22.23.24.25.26",
        "27.28.29.30.31",
    ]

