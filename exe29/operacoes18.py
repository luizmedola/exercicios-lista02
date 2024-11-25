def intervalo_entre_elementos(lista):
    if len(lista) == 0:
        return 0 
    return max(lista) - min(lista)
