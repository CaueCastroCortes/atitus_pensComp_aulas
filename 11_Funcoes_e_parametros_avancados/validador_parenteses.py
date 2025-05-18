def validador_parenteses(entrada: str) -> bool:
    contador = 0
    for caractere in entrada:
        if caractere == '(':
            contador += 1
        elif caractere == ')':
            contador -= 1
        # Se em algum momento o contador for negativo, 
        # significa que há fechamento sem abertura correspondente
        if contador < 0:
            return False
    return contador == 0

    
# Valores válidos
assert validador_parenteses("()")
assert validador_parenteses("()()")
assert validador_parenteses("(())")
assert validador_parenteses("(()()())")
assert validador_parenteses("(((())()))")

# Valores inválidos
assert validador_parenteses(")")
assert validador_parenteses("(")
assert validador_parenteses("()(")
assert validador_parenteses("()()())")
assert validador_parenteses("(((())())")
