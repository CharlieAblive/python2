from CalculoFrete import CalculoFrete

class Drone(CalculoFrete):
    def __init__(self, distancia, peso):
        self.distancia = distancia
        self.peso = peso
        
    def calcular(self):
        print("Calculando Frete de Drone...")
        if self.peso <= 5.0:
            preco = 5 * self.distancia
            print(f"Seu frete será de R${preco}.")
        else:
            (print(f"Erro: Sobrecarga de peso."))