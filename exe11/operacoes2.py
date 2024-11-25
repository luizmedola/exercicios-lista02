def produto_escalar(vetor1, vetor2):
    if len(vetor1) != len(vetor2):
        raise ValueError("os vetores devem ter o mesmo tamanho.")
    
    produto = sum(x * y for x, y in zip(vetor1, vetor2))
    return produto
