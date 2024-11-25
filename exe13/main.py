from operacoes4 import diferenca_elementos_lista

class ProcessadorListas:
    def __init__(self, lista):
        self.lista = lista

    def calcular_diferenca_elementos(self):
        return diferenca_elementos_lista(self.lista)

    def exibir_resultados(self):
        diferencas = self.calcular_diferenca_elementos()
        print(f"lista original: {self.lista}")
        print(f"diferença entre elementos consecutivos: {diferencas}")


if __name__ == "__main__":
    lista = [10, 5, 3, 8, 15]
    processador = ProcessadorListas(lista)
    processador.exibir_resultados()
