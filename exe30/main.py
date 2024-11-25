from operacoes19 import histograma

class ProcessadorLista:
    def __init__(self, lista):
        self.lista = lista

    def gerar_histograma(self):
        return histograma(self.lista)

    def exibir_resultados(self):
        histo = self.gerar_histograma()
        print(f"lista: {self.lista}")
        print("histograma das ocorrências de elementos:")
        for item, count in histo.items():
            print(f"elemento {item}: {count} ocorrências")

# Exemplo de uso
if __name__ == "__main__":
    lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4] 
    processador = ProcessadorLista(lista)
    processador.exibir_resultados()

    lista2 = ["a", "b", "a", "c", "b", "a"]  
    processador2 = ProcessadorLista(lista2)
    processador2.exibir_resultados()
