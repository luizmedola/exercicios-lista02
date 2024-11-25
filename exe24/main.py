from operacoes13 import numeros_primos

class ProcessadorNumeros:
    def __init__(self, n):
        self.n = n

    def obter_numeros_primos(self):
    
        return numeros_primos(self.n)

    def exibir_resultados(self):
        primos = self.obter_numeros_primos()
        print(f"números primos até {self.n}: {primos}")

if __name__ == "__main__":
    n = 30  
    processador = ProcessadorNumeros(n)
    processador.exibir_resultados()
