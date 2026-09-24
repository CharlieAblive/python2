from Caminhao import Caminhao
from Drone import Drone
from CalculoFrete import CalculoFrete

def iniciar():
    print(f"\n=====-Cálculo de Frete-=====\n")

def processarLote(listaDeFretes):
    print("\nProcessando a lista de Fretes")
    for i in listaDeFretes:
        iniciar()
        i.calcular()
        

frete1 = Caminhao(40)
frete2 = Drone(30, 4)
frete3 = Drone(20, 10)

listaDeFretes = [frete1, frete2, frete3]

processarLote(listaDeFretes)