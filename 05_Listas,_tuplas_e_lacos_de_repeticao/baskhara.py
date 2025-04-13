import math

def baskhara(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return None

    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    
    return x1, x2
    
    # retorne None se discriminante < 0
    # retorne apenas um valor se discriminante == 0
    # retorne [x1, x2] nos outros casos

raizes = (a, b, c)
print(baskhara(*raizes))

def test():

    assert baskhara(1, -3, 2) == [2, 1]
    assert baskhara(2, 3, -2) == [-2, 0.5]
    assert baskhara(1, -5, 6) == [2, 3]
    assert baskhara(1, -7, 10) == [2, 5]

    assert baskhara(1, 2, 3) is None
    assert baskhara(1, 0, 0) == 0