def multiplica_matrizes(matriz1, matriz2):
    if len(matriz1) != 2 or len(matriz1[0]) != 2 or len(matriz2) != 2 or len(matriz2[0]) != 2:
        raise ValueError("ambas as matrizes devem ser 2x2.")
    
    resultado = [
        [
            matriz1[0][0] * matriz2[0][0] + matriz1[0][1] * matriz2[1][0],  # Elemento (0,0)
            matriz1[0][0] * matriz2[0][1] + matriz1[0][1] * matriz2[1][1],  # Elemento (0,1)
        ],
        [
            matriz1[1][0] * matriz2[0][0] + matriz1[1][1] * matriz2[1][0],  # Elemento (1,0)
            matriz1[1][0] * matriz2[0][1] + matriz1[1][1] * matriz2[1][1],  # Elemento (1,1)
        ]
    ]
    
    return resultado
