def real_para_dolar(valor, tx_conversao):
    print(f"A conversão será {valor} / {tx_conversao}")
    return valor / tx_conversao

  
def test():

    assert real_para_dolar(500, 5.20) == 500 / 5.20
    assert real_para_dolar(500, 1) == 500
    assert real_para_dolar(500, 6) == 500 / 6



