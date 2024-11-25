def diagonais_matriz(matriz):
    if len(matriz) != len(matriz[0]):
        raise ValueError("A matriz não é quadrada.")
    
    diagonais = []
    tamanho = len(matriz)
    
    for i in range(tamanho):
        diagonais.append(matriz[i][i])  
        diagonais.append(matriz[i][tamanho - 1 - i])  
    
    return diagonais
