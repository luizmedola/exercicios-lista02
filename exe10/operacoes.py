def diferenca_max_min(lista):
    if not lista:
        return 0  
    maior = max(lista) 
    menor = min(lista)  
    return maior - menor 
