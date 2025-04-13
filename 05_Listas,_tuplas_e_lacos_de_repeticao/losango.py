def desenha_losango(altura):
    if altura % 2 == 0:
        print("Por favor, insira uma altura ímpar para um losango simétrico.")
        return
    
    meio = altura // 2
    
    # Parte superior do losango
    for i in range(meio + 1):
        print(' ' * (meio - i) + '#' * (2 * i + 1))
    
    # Parte inferior do losango
    for i in range(meio - 1, -1, -1):
        print(' ' * (meio - i) + '#' * (2 * i + 1))

altura = int(input("Digite um valor ímpar para a altura do losango: "))
desenha_losango(altura)


#Range produz uma lista
#