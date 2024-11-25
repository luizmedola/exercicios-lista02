from operacoes17 import remove_multiplos

class ProcessadorLista:
    def __init__(self, lista):
        self.lista = lista

    def remover_multiplos(self, n):
        return remove_multiplos(self.lista, n)

    def exibir_resultados(self, n):
        lista_filtrada = self.remover_multiplos(n)
        print(f"lista original: {self.lista}")
        print(f"lista sem múltiplos de {n}: {lista_filtrada}")

# Exemplo de uso
if __name__ == "__main__":
    lista = [10, 15, 20, 25, 30, 35, 40]  
    processador = ProcessadorLista(lista)
    processador.exibir_resultados(5) 

    lista2 = [3, 7, 12, 14, 18, 22] 
    processador2 = ProcessadorLista(lista2)
    processador2.exibir_resultados(3)  
