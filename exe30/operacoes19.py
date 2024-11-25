def histograma(lista):
    ocorrencias = {}
    
    for item in lista:
        if item in ocorrencias:
            ocorrencias[item] += 1  
        else:
            ocorrencias[item] = 1  
    
    return ocorrencias
