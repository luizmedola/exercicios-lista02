def conta_intervalo(lista, inicio, fim):
    contador = sum(1 for numero in lista if inicio <= numero <= fim)
    return contador
