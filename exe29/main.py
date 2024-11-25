from operacoes18 import intervalo_entre_elementos

class ProcessadorLista:
    def __init__(self, lista):
        self.lista = lista

    def calcular_intervalo(self):
        return intervalo_entre_elementos(self.lista)

    def exibir_resultados(self):
        intervalo = self.calcular_intervalo()
        print(f"lista: {self.lista}")
        print(f"intervalo entre o maior e o menor valor: {intervalo}")


if __name__ == "__main__":
    lista = [10, 5, 15, 30, 25]  
    processador = ProcessadorLista(lista)
    processador.exibir_resultados()

    lista2 = [100, 25, 50, 75, 10]  
    processador2 = ProcessadorLista(lista2)
    processador2.exibir_resultados()
