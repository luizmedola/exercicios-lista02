from operacoes6 import multiplica_matrizes

class ProcessadorMatrizes:
    def __init__(self, matriz1, matriz2):
        self.matriz1 = matriz1
        self.matriz2 = matriz2

    def calcular_multiplicacao(self):
        return multiplica_matrizes(self.matriz1, self.matriz2)

    def exibir_resultados(self):
        resultado = self.calcular_multiplicacao()
        print(f"matriz 1: {self.matriz1}")
        print(f"matriz 2: {self.matriz2}")
        print(f"resultado da multiplicação: {resultado}")

if __name__ == "__main__":
    matriz1 = [[1, 2], [3, 4]]
    matriz2 = [[5, 6], [7, 8]]
    processador = ProcessadorMatrizes(matriz1, matriz2)
    processador.exibir_resultados()
