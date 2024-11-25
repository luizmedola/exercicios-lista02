from operacoes8 import intercala_listas_ordenadas

class ProcessadorListas:
    def __init__(self, lista1, lista2):
        self.lista1 = lista1
        self.lista2 = lista2

    def intercalar_listas(self):
        return intercala_listas_ordenadas(self.lista1, self.lista2)

    def exibir_resultados(self):
        resultado = self.intercalar_listas()
        print(f"lista 1: {self.lista1}")
        print(f"lista 2: {self.lista2}")
        print(f"lista intercalada e ordenada: {resultado}")


if __name__ == "__main__":
    lista1 = [1, 3, 5, 7, 9]
    lista2 = [2, 4, 6, 8, 10]
    processador = ProcessadorListas(lista1, lista2)
    processador.exibir_resultados()
