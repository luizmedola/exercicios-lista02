import math

def desvio_padrao(lista):
    if len(lista) == 0:
        raise ValueError("A lista não pode estar vazia.")
    
    media = sum(lista) / len(lista)
    
    soma_quadrados_diferencas = sum((x - media) ** 2 for x in lista)
    
    variancia = soma_quadrados_diferencas / len(lista)
    
    return math.sqrt(variancia)
