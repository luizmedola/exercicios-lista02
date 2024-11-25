from operacoes12 import multiplica_pares

class ProcessadorLista:
    def __init__(self, lista):
        self.lista = lista

    def multiplicar_pares(self):
        return multiplica_pares(self.lista)

    def exibir_resultados(self):
        resultado = self.multiplicar_pares()
        print(f"lista: {self.lista}")
        print(f"multiplicação dos números pares: {resultado}")

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, 7, 8]  
    processador = ProcessadorLista(lista)
    processador.exibir_resultados()
