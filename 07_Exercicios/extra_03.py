def real_para_dolar(valor, tx_conversao):
    tx_conversao = 5.20
    valor = int(input("Digite um valor para realizar a conversao")
                print (f"A conversão será {valor} / {tx_conversao}")
  

def test ():
  assert real_para_dolar(500, 5.20) == 96.23
  assert real_para_dolar(500, 1) == 500
  assert real_para_dolar(500, 6) == 83.33333333333333