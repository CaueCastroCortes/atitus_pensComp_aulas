def caesar_cipher(texto, desvio):
    resultado = []
    for char in texto:
        if char.isalpha():
            if char.isupper():
                deslocamento = ord('A')  
            else:
                deslocamento = ord('a')  

            novo_char = chr((ord(char) - deslocamento + desvio) % 26 + deslocamento)
            resultado.append(novo_char)
        else:
            resultado.append(char)
    
    return ''.join(resultado)

def test():
  assert caesar_cipher("Hello, World!", 3) == "Khoor, Zruog!"
  assert caesar_cipher("Khoor, Zruog!", -3) == "Hello, World!"

  assert caesar_cipher("Matheus Jardim", 3) == "Pdwkhxv Mduglp"
  assert caesar_cipher("Pdwkhxv Mduglp", -3) == "Matheus Jardim"

  assert caesar_cipher(caesar_cipher("Atitus", 3), -3) == "Atitus"
