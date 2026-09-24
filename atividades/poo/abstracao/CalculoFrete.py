from abc import ABC, abstractmethod

class CalculoFrete(ABC):
    def iniciar(self):
        print("\n=====-Cálculo de Frete-=====\n")
   
    @abstractmethod
    def calcular(self, distancia):
        pass

    
