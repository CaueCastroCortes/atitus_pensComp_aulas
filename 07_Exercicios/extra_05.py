def status_aluno(notas):  
    if not notas or None in notas:  # Se lista estiver vazia ou contiver 'None', retorna False
        return False
    
    # Se todas as notas forem 10, o aluno passa automaticamente
    todas_10 = True
    for nota in notas:
        if nota != 10:
            todas_10 = False
            break

    if todas_10:
        return True

    # Calcula a média das notas
    total = 0
    quantidade = 0
    for nota in notas:
        total += nota
        quantidade += 1

    if quantidade == 0:
        return False

    media = total / quantidade

    return media >= 7  

# Testes automatizados
def test():
    assert status_aluno([10, 10, 10, 10])  
    assert not status_aluno([10, None, 10, 10])  
    assert not status_aluno([10, 5, None, 5])  
    assert not status_aluno([5, 5, 5, 5])  
    assert not status_aluno([0, 0, 0, 0])  
    assert status_aluno([7, 8, 9]) 