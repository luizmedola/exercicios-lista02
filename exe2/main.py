from calculadora import produto_lista

class ProcessadorLista:
    def __init__(self, lista):
        self.lista = lista

    def calcular_produto(self):
        produto = produto_lista(self.lista)
        return produto

    def exibir_resultados(self):
        print(f"lista original: {self.lista}")
        produto = self.calcular_produto()
        print(f"produto de todos os elementos: {produto}")

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    processador = ProcessadorLista(lista)
    processador.exibir_resultados()
