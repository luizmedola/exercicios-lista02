from operacoes14 import concatena_strings

class ProcessadorStrings:
    def __init__(self, lista_strings):
        self.lista_strings = lista_strings

    def concatenar(self):
        return concatena_strings(self.lista_strings)

    def exibir_resultados(self):
        resultado = self.concatenar()
        print(f"lista de strings: {self.lista_strings}")
        print(f"string concatenada: {resultado}")

# Exemplo de uso
if __name__ == "__main__":
    lista_strings = ["Olá", " ", "mundo", "!"]  
    processador = ProcessadorStrings(lista_strings)
    processador.exibir_resultados()
