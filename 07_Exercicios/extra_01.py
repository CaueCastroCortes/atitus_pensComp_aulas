def letra_em_texto(texto, letra): 
  texto = input("Digite um texto: ")
  letra = input("Qual letra você deseja achar?")
  posicao = texto.find(letra)
  print(f"A letra que você procura está na posição {posicao}")



def conta_letra_em_texto(texto, letra):
  texto = input("Digite um texto: ")
  letra_escolhida = input("Qual letra você deseja descobrir a quantidadde de vezes que aparece no texto? ")
  contador = 0
  for letra_escolhida in texto:
      contador += 1
      print(f"A letra escolhida aparece {contador} vezes no texto digitado")



def texto_sem_letra(texto, letra):
  texto = input("Digite um texto: ")
  letra_apagada = input("Qual letra você deseja apagar do texto? ")
  texto_novo = ""
  for letra in texto:
      if letra not in letra_apagada:
          texto_novo += letra
          print(f"Seu novo texto ficará {texto_novo}")



def texto_com_letra_upper(texto, letra):
    texto = input("Digite um texto: ")
    letra_grande = input("Qual letra você gostaria de deixar maiúscula? ")
    novo_texto = ""
    for letra in texto:
        if letra == letra_grande:
            novo_texto += letra.upper()
        else:
            novo_texto = += letra
        print(f"Seu texto ficará assim {novo_texto}")


def test ():
  assert letra_em_texto("Pensamento Computacional", "a")
  assert letra_em_texto("Pensamento Computacional", " ")
  assert not letra_em_texto("Pensamento Computacional", "A")
  assert not letra_em_texto("Pensamento Computacional", "c")

  assert conta_letra_em_texto("Pensamento Computacional", "a") == 3
  assert conta_letra_em_texto("Pensamento Computacional", "A") == 0
  assert conta_letra_em_texto("Pensamento Computacional", "e") == 2

  assert texto_sem_letra("Pensamento Computacional", "a") == "Pensmento Computcionl"
  assert texto_sem_letra("Pensamento Computacional", "z") == "Pensamento Computacional"
  assert texto_sem_letra("Pensamento Computacional", " ") == "PensamentoComputacional"

  assert (texto_com_letra_upper("Pensamento Computacional", "a") == "PensAmento ComputAcionAl")
  assert (texto_com_letra_upper("Pensamento Computacional", "z") == "Pensamento Computacional")
  assert (texto_com_letra_upper("Pensamento Computacional", " ") == "Pensamento Computacional")