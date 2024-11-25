from operacoes7 import busca_binaria

class ProcessadorBusca:
    def __init__(self, lista):
        self.lista = lista

    def realizar_busca_binaria(self, elemento):
        return busca_binaria(self.lista, elemento)

    def exibir_resultados(self, elemento):
        indice = self.realizar_busca_binaria(elemento)
        if indice != -1:
            print(f"elemento {elemento} encontrado no índice {indice}.")
        else:
            print(f"elemento {elemento} não encontrado na lista.")

if __name__ == "__main__":
    lista = [1, 3, 5, 7, 9, 11, 13, 15]
    processador = ProcessadorBusca(lista)
    
    processador.exibir_resultados(5)
    
    processador.exibir_resultados(4)
