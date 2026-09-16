"""
O código retorna False por que o terminal não lê o input como int, sim como str, 
e não consegue comparar os dois valores por serem de tipos diferentes.

"""

senha_cadastrada = 1234
senha_digitada = int(input("Digite sua senha: "))
acesso_liberado = senha_cadastrada == senha_digitada
print("Acesso liberado?", acesso_liberado)