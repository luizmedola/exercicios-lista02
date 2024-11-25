from operacoes3 import separa_pares_impares

class ProcessadorListas:
    def __init__(self, lista):
        self.lista = lista

    def separar_pares_impares(self):
        pares, impares = separa_pares_impares(self.lista)
        return pares, impares

    def exibir_resultados(self):
        pares, impares = self.separar_pares_impares()
        print(f"lista original: {self.lista}")
        print(f"lista de números pares: {pares}")
        print(f"lista de números ímpares: {impares}")


if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    processador = ProcessadorListas(lista)
    processador.exibir_resultados()
