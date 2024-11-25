from convercao import celsius_para_fahrenheit

class ProcessadorTemperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    def converter_para_fahrenheit(self):
        return celsius_para_fahrenheit(self.celsius)

    def exibir_resultados(self):
        fahrenheit = self.converter_para_fahrenheit()
        print(f"temperatura em celsius: {self.celsius}°C")
        print(f"temperatura em fahrenheit: {fahrenheit}°F")

if __name__ == "__main__":
    celsius = 25  
    processador = ProcessadorTemperatura(celsius)
    processador.exibir_resultados()
