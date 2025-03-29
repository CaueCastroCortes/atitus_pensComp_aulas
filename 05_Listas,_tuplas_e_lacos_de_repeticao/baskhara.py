def baskhara(a, b, c):
    a,b,c = b**2 - 4*a*c
    
    # retorne None se discriminante < 0
    # retorne apenas um valor se discriminante == 0
    # retorne [x1, x2] nos outros casos
    


assert baskhara(1, -3, 2) == [2, 1]
assert baskhara(2, 3, -2) == [-2, 0.5]
assert baskhara(1, -5, 6) == [2, 3]
assert baskhara(1, -7, 10) == [2, 5]

assert baskhara(1, 2, 3) is None
assert baskhara(1, 0, 0) == 0
