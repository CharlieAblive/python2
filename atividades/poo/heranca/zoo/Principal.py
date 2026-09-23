from Mamifero import Mamifero
from Ave import Ave

leao = Mamifero(nome="Simba", idade=5, nivelFome=70, velocidade=80)
gaviao = Ave(nome="Sky", idade=2, nivelFome=75, envergadura=120)

leao.__nivel_fome = -999
leao.__idade = -10


leao.correr()        
gaviao.voar()        
gaviao.voar()        

leao.alimentar(50)  
leao.alimentar(-10)  
