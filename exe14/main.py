from operacoes5 import desvio_padrao

class ProcessadorListas:
    def __init__(self, lista):
        self.lista = lista

    def calcular_desvio_padrao(self):
        return desvio_padrao(self.lista)

    def exibir_resultados(self):
        desvio = self.calcular_desvio_padrao()
        print(f"lista: {self.lista}")
        print(f"desvio padrão: {desvio:.2f}")

if __name__ == "__main__":
    lista = [10, 20, 30, 40, 50]
    processador = ProcessadorListas(lista)
    processador.exibir_resultados()
