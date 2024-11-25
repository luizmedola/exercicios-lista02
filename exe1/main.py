from multiplicador import multiplica_escalar

class ProcessadorLista:
    def __init__(self, lista):
        self.lista = lista

    def processar_multiplicacao(self, escalar):
        lista_resultante = multiplica_escalar(self.lista, escalar)
        return lista_resultante

    def exibir_resultados(self, escalar):
        print(f"lista original: {self.lista}")
        lista_resultante = self.processar_multiplicacao(escalar)
        print(f"lista após multiplicação por {escalar}: {lista_resultante}")


if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    escalar = 3
    processador = ProcessadorLista(lista)
    processador.exibir_resultados(escalar)
