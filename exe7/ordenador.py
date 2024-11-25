def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        z = i
        for j in range(i+1, n):
            if lista[j] < lista[z]:
               z = j
        
        lista[i], lista[z] = lista[z], lista[i]
    
    return lista
