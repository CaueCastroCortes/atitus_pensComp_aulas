import random

def escolher_dificuldade():
    while True:
        dificuldade_str = input("Escolha a dificuldade (1 - Fácil [5 letras], 2 - Médio [6 letras], 3 - Difícil [7 letras]): ").strip()
        try:
            dificuldade = int(dificuldade_str)
        except ValueError:
            print("Digite um número válido!")
            continue

        if dificuldade in (1, 2, 3):
            return dificuldade
        else:
            print("Opção inválida! Escolha 1, 2 ou 3.")

def gerar_dica(palpite, secreta):
    
    # Gera uma dica comparando o palpite com a palavra secreta.
    # Letras na posição correta são envolvidas por colchetes [x].
    # Letras presentes, mas fora do lugar, são envolvidas por parênteses (x).
    # Letras não encontradas permanecem como [ ].

    # Definindo o tamanho da palavra secreta
    tamanho = len(secreta)
    dica = ["[ ]"] * tamanho

    # Faz uma cópia da palavra secreta para "consumir" letras já identificadas
    secret_list = list(secreta)

    # Primeira passagem: identifica acertos exatos
    for i in range(tamanho):
        if palpite[i] == secreta[i]:
            dica[i] = f"[{palpite[i]}]"
            secret_list[i] = None  # Marca essa ocorrência

    # Segunda passagem: verifica letras presentes mas em posição incorreta
    for i in range(tamanho):
        if dica[i] == "[ ]" and palpite[i] in secret_list:
            dica[i] = f"({palpite[i]})"
            indice = secret_list.index(palpite[i])
            secret_list[indice] = None

    return "".join(dica)

def play_game():
    palavras = {
        1: [
            "manga", "carro", "aviao", "navio", "peixe",
            "cacto", "tenis", "plano", "bingo", "rifle",
            "sorte", "tempo", "festa", "mundo", "amigo"
        ],
        2: [
            "banana", "girafa", "coelho", "baleia", "futuro",
            "dentro", "branco", "amargo", "buscas", "risada",
            "sombra", "pranto", "correr", "seguro", "magico"
        ],
        3: [
            "deboche", "atraves", "almejar", "saudade", "contudo",
            "coragem", "amizade", "carinho", "sorriso", "exemplo",
            "liberal", "poderia", "caminho", "alegria", "premiar"
        ]
    }

    print("SEJA BEM-VINDO AO JOGO DE ADIVINHAÇÃO!")
    print("INSTRUÇÕES:")
    print("• Digite a palavra completa.")
    print("• A dificuldade determina o tamanho da palavra:")
    print("    1 - Fácil: 5 letras")
    print("    2 - Médio: 6 letras")
    print("    3 - Difícil: 7 letras")
    print("• O número de tentativas é igual ao número de letras da palavra.")
    print("• Após cada tentativa, você receberá uma dica:")
    print("    - Letras na posição correta: [x]")
    print("    - Letras presentes, mas fora do lugar: (x)")

    dificuldade = escolher_dificuldade()
    secreta = random.choice(palavras[dificuldade])
    tamanho_palavra = len(secreta)
    tentativas = tamanho_palavra

    print(f"\nA palavra tem {tamanho_palavra} letras. Você tem {tentativas} tentativas para adivinhá-la.")

    while tentativas > 0:
        palpite = input("Digite sua palavra: ").lower().strip()

        if len(palpite) != tamanho_palavra:
            print(f"A palavra deve ter exatamente {tamanho_palavra} letras!")
            continue

        if palpite == secreta:
            print("Parabéns! Você adivinhou a palavra!")
            return

        dica = gerar_dica(palpite, secreta)
        tentativas -= 1
        print(f"Dica: {dica}")
        print(f"Tentativas restantes: {tentativas}")

    print(f"Suas tentativas acabaram. A palavra correta era: {secreta}")
    print("FIM DO JOGO!")

if __name__ == "__main__":
    play_game()
