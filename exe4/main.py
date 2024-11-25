from concatenador import concatena_listas

class ProcessadorListas:
    def __init__(self, lista1, lista2):
        self.lista1 = lista1
        self.lista2 = lista2

    def concatenar(self):
        return concatena_listas(self.lista1, self.lista2)

    def exibir_resultados(self):
        print(f"lista 1: {self.lista1}")
        print(f"lista 2: {self.lista2}")
        lista_concatenada = self.concatenar()
        print(f"lista concatenada: {lista_concatenada}")


if __name__ == "__main__":
    lista1 = [1, 2, 3]
    lista2 = [4, 5, 6]
    processador = ProcessadorListas(lista1, lista2)
    processador.exibir_resultados()
