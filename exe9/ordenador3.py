def quick_sort(lista):
    pilha = []
    pilha.append((0, len(lista) - 1))
    
    
    while pilha:
        inicio, fim = pilha.pop()
        
        if inicio < fim:
            p = particionar(lista, inicio, fim)
            
            pilha.append((inicio, p - 1))
            pilha.append((p + 1, fim))
    
    return lista

def particionar(lista, inicio, fim):
    p = lista[fim]
    i = inicio - 1
    

    for j in range(inicio, fim):
        if lista[j] <= p:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    return i + 1
