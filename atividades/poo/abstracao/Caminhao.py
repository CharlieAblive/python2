from CalculoFrete import CalculoFrete

class Caminhao(CalculoFrete):
    def __init__(self, distancia):
        self.distancia = distancia
    
    def calcular(self):
        print("Calculando Frete de Caminhão...")
        preco = 10.0 * self.distancia
        print(f"Seu frete será de R${preco}\2.")

        