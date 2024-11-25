from convercao2 import fahrenheit_para_celsius

class ProcessadorTemperatura:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit

    def converter_para_celsius(self):
        return fahrenheit_para_celsius(self.fahrenheit)

    def exibir_resultados(self):
        celsius = self.converter_para_celsius()
        print(f"temperatura em fahrenheit: {self.fahrenheit}°F")
        print(f"temperatura em celsius: {celsius}°C")


if __name__ == "__main__":
    fahrenheit = 77  
    processador = ProcessadorTemperatura(fahrenheit)
    processador.exibir_resultados()
