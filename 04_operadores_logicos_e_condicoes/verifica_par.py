def eh_par(numero):
    if ((numero % 2) == 0):
        return True
    else: 
        return False

def eh_impar(numero):
    if ((numeros % 1) == 0):
        return True
    else:
        return False


assert eh_par(0)
assert eh_par(2)
assert eh_par(4)
assert not eh_par(1)
assert not eh_par(3)

assert eh_impar(1)
assert eh_impar(3)
assert eh_impar(5)
assert not eh_impar(0)
assert not eh_impar(2)

print(eh_par(0))
print(eh_impar(0))