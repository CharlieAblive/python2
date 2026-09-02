#operadores
"""
    atribuição
    = -> variavel = 10

    ! = NÃO, NOT, CONTRARIO...
    SIM -> !SIM = NÃO

    COMPARAÇAO
    esperar uma resposta de TRUE ou FALSE (basicamente boolean)
    != ->se for diferente retorna True, se for igual retorna False
    == -> se for diferente retorna false, se for igual retorna true

    > -> se for menor retorna true, se for maior retorna false
    < -> se for maior retorna true, se for menor retorna false

    >= -> se for menor ou igual retorna true, se for maior retorna false
    <= -> se for maior ou igual retorna true, se for menor retorna false

    and -> faz duas comparações e se as duas forem verdadeiras, retorna true, se uma ou mais forem falsas, retorna false.
    or -> faz duas comparações e se as duas forem falsas, retorna false, se uma ou mais forem verdadeiras, retorna true.
    not


"""

#TESTES
idade = 18 #inteiro

print("diferente:", idade != 18) #false
print("igual:", idade == 18) #true

print("maior que:", idade > 18) #false
print("menor que:", idade < 18) #false

print("maior ou igual que:", idade >= 18) #true
print("menor ou igual que:", idade <= 18) #true

print("and:", idade == 18 and idade > 18) #false
print("or: ", idade == 18 or idade > 18) #true