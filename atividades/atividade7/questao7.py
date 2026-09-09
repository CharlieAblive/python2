saldo = 500.00
gasto = int(input("Quanto você gastou hoje? "))

while gasto < saldo:
    gasto = int(input("Okay, e o próximo gasto? "))
    if gasto >= saldo:
        print("Eita! Você zerou sua conta, ou estourou seu orçamento!")
        break