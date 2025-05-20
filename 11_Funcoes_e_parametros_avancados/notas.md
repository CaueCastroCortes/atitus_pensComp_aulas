def lista_de_lista(lista: list, numero: int)-> bool:
    for linha in lista:
        for elemento in linha:
            if elemento == numero:
                return True
    return False

tabela =  [
    [1, 2, 3],
    [4],
    [5, 6, 7, 8, 9, 10],
]

print(procura_numero(tabela, numero: 15))

def verificando_palindromo(palavra: str)-> bool:
    for letra in palavra:
        if palavra 