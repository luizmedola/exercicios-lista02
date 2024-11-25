from operacoes import diferenca_max_min

class ProcessadorListas:
    def __init__(self, lista):
        self.lista = lista

    def calcular_diferenca_max_min(self):
        return diferenca_max_min(self.lista)

    def exibir_resultados(self):
        diferenca = self.calcular_diferenca_max_min()
        print(f"lista: {self.lista}")
        print(f"diferença entre o maior e o menor elemento: {diferenca}")

if __name__ == "__main__":
    lista = [64, 25, 12, 22, 11]
    processador = ProcessadorListas(lista)
    processador.exibir_resultados()
