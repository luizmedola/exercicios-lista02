from operacoes10 import diagonais_matriz

class ProcessadorMatriz:
    def __init__(self, matriz):
        self.matriz = matriz

    def obter_diagonais(self):
        return diagonais_matriz(self.matriz)

    def exibir_resultados(self):
        diagonais = self.obter_diagonais()
        print(f"matriz: {self.matriz}")
        print(f"elementos das diagonais: {diagonais}")


if __name__ == "__main__":
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    processador = ProcessadorMatriz(matriz)
    processador.exibir_resultados()
