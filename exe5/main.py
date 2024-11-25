from somador import soma_naturais

class ProcessadorNumeros:
    def __init__(self, n):
        self.n = n

    def calcular_soma(self):
        return soma_naturais(self.n)

    def exibir_resultados(self):
        soma = self.calcular_soma()
        print(f"a soma dos primeiros {self.n} números naturais é: {soma}")

if __name__ == "__main__":
    n = 10  
    processador = ProcessadorNumeros(n)
    processador.exibir_resultados()
