def maior_numero(lista): 
  escolha = int(input("Escolha qual lista você deseja descobrir o maior número, 1, 2 ou 3: "))
  if escolha < 1 or escolha > 3:
    return None
                
  if escolha == 1:
    maior_numero = max(lista_1)
    print(f"O maior número é {maior_numero}")
  elif escolha == 2:
    maior_numero = max(lista_2)
    print(f"O maior número é {maior_numero}")
  elif escolha == 3:
    maior_numero = max(lista_3)
    print(f"O maior número é {maior_numero}")
                


def menor_numero(lista):
  escolha = int(input("Escolha qual lista você deseja descobrir o maior número, 1, 2 ou 3: "))
  if escolha < 1 or escolha > 3:
    return None     
  if escolha == 1:
    menor_numero = min(lista_1)
    print(f"O maior número é {maior_numero}")
  elif escolha == 2:
    menor_numero = min(lista_2)
    print(f"O maior número é {maior_numero}")
  elif escolha == 3:
    menor_numero = min(lista_3)
    print(f"O maior número é {menor_numero}")
 


def numeros_pares(lista):
  escolha = int(input("Escolha qual lista você deseja descobrir o maior número, 1, 2 ou 3: ")
  if escolha < 1 and > 3:
                return None
  if escolha == 1:
    numero_par = ""
    for numero in lista_1:
      if numero % 2 == 0:
        numero_par += numero
        print(f"Os números pares são {numero_par}")
  if escolha == 2:
    numero_par = ""
    for numero in lista_2:
      if numero % 2 == 0:
        numero_par += numero
        print(f"Os números pares são {numero_par}")
  if escolha == 3:
    numero_par = ""
    for numero in lista_3:
      if numero % 2 == 0:
        numero_par += numero
        print(f"Os números pares são {numero_par}")

         
        



def numeros_impares(lista):
  escolha = int(input("Escolha qual lista você deseja descobrir o maior número, 1, 2 ou 3: ")
  if escolha < 1 or escolha > 3:
                return None
  if escolha == 1:
    numero_impar = ""
    for numero in lista_1:
      if numero % 2 != 0:
        numero_impar += numero
        print(f"Os números ímpares são {numero_impar}")
  if escolha == 2:
    numero_impar = ""
    for numero in lista_2:
      if numero % 2 != 0:
        numero_impar += numero
        print(f"Os números ímpares são {numero_impar}")
  if escolha == 3:
    numero_impar = ""
    for numero in lista_3:
      if numero % 2 == 0:
        numero_impar += numero
        print(f"Os números ímpares são {numero_impar}")


def numeros_positivo(lista):
    if escolha == 1:
      numero_positivo = ''
      for numero in lista_1:
        if numero > 0:
          numero_positivo += numero
          print(f'Os números positivos são {numero_positivo}')
    if escolha == 2:
      numero_positivo = ''
      for numero in lista_2:
        if numero > 0:
          numero_positivo += numero
          print(f'Os números positivos são {numero_positivo}')
    if escolha == 3:
      numero_positivo = ''
      for numero in lista_3:
        if numero > 0:
          numero_positivo += numero
          print(f'Os números positivos são {numero_positivo}')
    


def numeros_negativos(lista):
      if escolha == 1:
      numero_negativo = ''
      for numero in lista_1:
        if numero < 0:
          numero_negativo += numero
          print(f'Os números positivos são {numero_negativo}')
      if escolha == 2:
      numero_negativo = ''
      for numero in lista_2:
        if numero < 0:
          numero_negativo += numero
          print(f'Os números positivos são {numero_negativo}')
      if escolha == 3:
      numero_negativo = ''
      for numero in lista_3:
        if numero < 0:
          numero_negativo += numero
          print(f'Os números positivos são {numero_negativo}')



def soma_numeros(lista):
  if escolha == 1:
    soma = 0
    for numero in lista_1:
      soma += numero
    print(f'Soma dos números da lista 1 é {soma}')
      if escolha == 2:
    soma = 0
    for numero in lista_2:
      soma += numero
    print(f'Soma dos números da lista 2 é {soma}')
      if escolha == 3:
    soma = 0
    for numero in lista_3:
      soma += numero
    print(f'Soma dos números da lista 3 é {soma}')
   


lista_1 = [10, 0, -3, 42, 5, -6, 8, 91]
lista_2 = [20, 2, 27, 74, 19, 85, 3, 22, 95, 11]
lista_3 = [45, 92, 23, 17, 50, 89, 57, 15, 28, 5]

def test():
  assert maior_numero(lista_1) == 91
  assert maior_numero(lista_2) == 95
  assert maior_numero(lista_3) == 92

  assert menor_numero(lista_1) == -6
  assert menor_numero(lista_2) == 2
  assert menor_numero(lista_3) == 5

  assert numeros_pares(lista_1) == [10, 0, 42, -6, 8]
  assert numeros_pares(lista_1) == [20, 2, 74, 22]
  assert numeros_pares(lista_1) == [92, 50, 28]

  assert numeros_impares(lista_1) == [-3, 5, 91]
  assert numeros_impares(lista_1) == [27, 19, 85, 3, 95, 11]
  assert numeros_impares(lista_1) == [45, 23, 17, 89, 57, 15, 5]

  assert numeros_positivo(lista_1) == [10, 0, 42, 5, 8, 91]
  assert numeros_positivo(lista_1) == [20, 2, 27, 74, 19, 85, 3, 22, 95, 11]
  assert numeros_positivo(lista_1) == [45, 92, 23, 17, 50, 89, 57, 15, 28, 5]

  assert numeros_negativos(lista_1) == [-3, -6]
  assert numeros_negativos(lista_1) == []
  assert numeros_negativos(lista_1) == []

  assert soma_numeros(lista_1) == 147
  assert soma_numeros(lista_1) == 358
  assert soma_numeros(lista_1) == 421