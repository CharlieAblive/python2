# Instanciando os animais
from Mamifero import Mamifero
from Ave import Ave

leao = Mamifero(nome="Simba", idade=5, nivelFome=70, velocidade=80)
gaviao = Ave(nome="Sky", idade=2, nivelFome=75, envergadura=120)

# 1. Tentativa de alteração direta dos atributos privados (Proteção do Encapsulamento)
leao.__nivel_fome = -999
leao.__idade = -10

# 2. Testando ações que alteram o estado interno via Herança e Encapsulamento
leao.correr()          # Fome sobe de 70 para 90
gaviao.voar()          # Fome sobe de 75 para 90 (Sucesso)
gaviao.voar()          # Fome está em 90 -> Deve exibir: "Voo negado: Sky está faminto demais para voar!"

# 3. Testando alimentação
leao.alimentar(50)     # Fome cai de 90 para 40
leao.alimentar(-10)    # Deve exibir: "Erro: Porção inválida"
