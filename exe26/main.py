from operacoes15 import merge_sort

class ProcessadorLista:
    def __init__(self, lista):
        self.lista = lista

    def ordenar_lista(self):
        return merge_sort(self.lista)

    def exibir_resultados(self):
        lista_ordenada = self.ordenar_lista()
        print(f"lista original: {self.lista}")
        print(f"lista ordenada: {lista_ordenada}")

# Exemplo de uso
if __name__ == "__main__":
    lista = [38, 27, 43, 3, 9, 82, 10]  
    processador = ProcessadorLista(lista)
    processador.exibir_resultados()
