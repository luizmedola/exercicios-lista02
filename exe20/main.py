from operacoes11 import conta_intervalo

class ProcessadorLista:
    def __init__(self, lista):
        self.lista = lista

    def contar_intervalo(self, inicio, fim):
        return conta_intervalo(self.lista, inicio, fim)

    def exibir_resultados(self, inicio, fim):
        contador = self.contar_intervalo(inicio, fim)
        print(f"lista: {self.lista}")
        print(f"números no intervalo [{inicio}, {fim}]: {contador}")

if __name__ == "__main__":
    lista = [1, 5, 8, 12, 20, 25, 30, 40]
    inicio = 10
    fim = 30
    processador = ProcessadorLista(lista)
    processador.exibir_resultados(inicio, fim)
