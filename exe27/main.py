from operacoes16 import esta_ordenada

class ProcessadorLista:
    def __init__(self, lista):
        self.lista = lista

    def verificar_ordem(self):
        return esta_ordenada(self.lista)

    def exibir_resultados(self):
        resultado = self.verificar_ordem()
        if resultado:
            print(f"a lista {self.lista} está ordenada em ordem crescente.")
        else:
            print(f"a lista {self.lista} não está ordenada em ordem crescente.")

# Exemplo de uso
if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]  
    processador = ProcessadorLista(lista)
    processador.exibir_resultados()

    lista2 = [5, 3, 4, 1, 2]  
    processador2 = ProcessadorLista(lista2)
    processador2.exibir_resultados()
