def desenha_losango(altura):
    if altura % 2 == 0:
        print("Por favor, insira um valor ímpar para a altura.")
        return
    
    meio = altura // 2
    
    for i in range(altura):
        if i <= meio:
            espacos = meio - i
            asteriscos = 2 * i + 1
        else:
            espacos = i - meio
            asteriscos = 2 * (altura - i) - 1
        
        print(' ' * espacos + '*' * asteriscos)


altura = int(input("Digite um valor ímpar para a altura do losango: "))
desenha_losango(altura)
