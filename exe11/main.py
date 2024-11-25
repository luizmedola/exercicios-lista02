from operacoes2 import produto_escalar

class ProcessadorVetores:
    def __init__(self, vetor1, vetor2):
        self.vetor1 = vetor1
        self.vetor2 = vetor2

    def calcular_produto_escalar(self):
        return produto_escalar(self.vetor1, self.vetor2)

    def exibir_resultados(self):
        produto = self.calcular_produto_escalar()
        print(f"vetor 1: {self.vetor1}")
        print(f"vetor 2: {self.vetor2}")
        print(f"produto escalar: {produto}")

if __name__ == "__main__":
    vetor1 = [1, 2, 3]
    vetor2 = [4, 5, 6]
    processador = ProcessadorVetores(vetor1, vetor2)
    processador.exibir_resultados()
