from ordenador3 import quick_sort

class ProcessadorListas:
    def __init__(self, lista):
        self.lista = lista

    def ordenar_lista(self):
        lista_copia = self.lista.copy()
        return quick_sort(lista_copia)

    def exibir_resultados(self):
        lista_ordenada = self.ordenar_lista()
        print(f"lista original: {self.lista}")
        print(f"lista ordenada: {lista_ordenada}")

if __name__ == "__main__":
    lista = [64, 25, 12, 22, 11]
    processador = ProcessadorListas(lista)
    processador.exibir_resultados()
