def multiplica_pares(lista):
    resultado = 1  
    encontrou_par = False  
    
    for numero in lista:
        if numero % 2 == 0:  
            resultado *= numero  
            encontrou_par = True
    
    if not encontrou_par:
        return 0 
    return resultado
