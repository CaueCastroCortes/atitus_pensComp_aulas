def fahrenheit_para_celsius(valor):
    f_para_c = (valor - 32) / 1.8
    print(f"A temperatura em graus Celsius é: {f_para_c}C°")
    return f_para_c

def celsius_para_fahrenheit(valor):
    c_para_f = (1.8 * valor) + 32
    print(f"A temperatura em graus Fahrenheit é: {c_para_f}F°")
    return c_para_f

def test():
    assert round(fahrenheit_para_celsius(104)) == 40
    assert round(fahrenheit_para_celsius(-13)) == -25

    assert round(celsius_para_fahrenheit(40)) == 104
    assert round(celsius_para_fahrenheit(-25)) == -13

    assert round(celsius_para_fahrenheit(fahrenheit_para_celsius(30))) == 30 