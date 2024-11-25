def media_ponderada(lista_valores, lista_pesos):

    if len(lista_valores) != len(lista_pesos):
        raise ValueError("As listas de valores e pesos devem ter o mesmo tamanho.")
    
    soma_ponderada = sum(valor * peso for valor, peso in zip(lista_valores, lista_pesos))
    
    soma_pesos = sum(lista_pesos)
    
    if soma_pesos == 0:
        raise ValueError("A soma dos pesos não pode ser zero.")
    
    media = soma_ponderada / soma_pesos
    return media
