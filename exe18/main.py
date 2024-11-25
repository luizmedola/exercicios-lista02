from operacoes9 import media_ponderada

class ProcessadorMedia:
    def __init__(self, lista_valores, lista_pesos):
        self.lista_valores = lista_valores
        self.lista_pesos = lista_pesos

    def calcular_media_ponderada(self):
        return media_ponderada(self.lista_valores, self.lista_pesos)

    def exibir_resultados(self):
        media = self.calcular_media_ponderada()
        print(f"valores: {self.lista_valores}")
        print(f"pesos: {self.lista_pesos}")
        print(f"média ponderada: {media}")

if __name__ == "__main__":
    lista_valores = [10, 7, 9, 8]
    lista_pesos = [3, 2, 4, 1]
    processador = ProcessadorMedia(lista_valores, lista_pesos)
    processador.exibir_resultados()
