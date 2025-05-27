def calcular_juros_compostos(principal, taxa, tempo):
    investimento = principal * ((1 + taxa) ** tempo)
    return investimento