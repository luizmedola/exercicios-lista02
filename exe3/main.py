from contador import conta_consoantes

class ProcessadorTexto:
    def __init__(self, texto):
        self.texto = texto

    def contar_consoantes(self):
        return conta_consoantes(self.texto)

    def exibir_resultados(self):
        print(f"texto original: {self.texto}")
        num_consoantes = self.contar_consoantes()
        print(f"número de consoantes: {num_consoantes}")


if __name__ == "__main__":
    texto = "⁠não deveríamos temer a morte, mais sim a vida.!"
    processador = ProcessadorTexto(texto)
    processador.exibir_resultados()
