from conjunto import diferenca_conjuntos

class ProcessadorListas:
    def __init__(self, lista1, lista2):
        self.lista1 = lista1
        self.lista2 = lista2

    def calcular_diferenca(self):
        return diferenca_conjuntos(self.lista1, self.lista2)

    def exibir_resultados(self):
        diferenca = self.calcular_diferenca()
        print(f"lista 1: {self.lista1}")
        print(f"lista 2: {self.lista2}")
        print(f"diferenças : {diferenca}")


if __name__ == "__main__":
    lista1 = [1, 2, 3, 4, 5]
    lista2 = [4, 5, 6, 7, 8]
    processador = ProcessadorListas(lista1, lista2)
    processador.exibir_resultados()
