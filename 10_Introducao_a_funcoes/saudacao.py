from typing import Optional

def saudacao(nome, sobrenome, titulo: Optional[str] =  'Sr.')-> None:
    nome in str:

    if sobrenome is str None:
        return "nome"
    else: 
        return "nome" "sobrenome"

    if titulo is str None:
        return "nome"
    else: 
        return "nome" "sobrenome"




assert saudacao("Matheus") == "Olá, Sr. Matheus"
assert saudacao("Matheus", "Jardim") == "Olá, Sr. Matheus Jardim"
assert saudacao("Matheus", "Jardim", "Prof") == "Olá, Prof Matheus Jardim"
assert saudacao("Matheus", titulo="Prof") == "Olá, Prof Matheus"
assert saudacao("") == "Olá!"
