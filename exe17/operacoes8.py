def intercala_listas_ordenadas(lista1, lista2):
    i, j = 0, 0
    resultado = []
    
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    
    
    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])
    
    return resultado
