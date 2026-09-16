saldoAtual = float(input("Digite o saldo atual: "))
sacar = float(input("Digite o quanto deseja sacar: "))
if sacar <= saldoAtual:
    print("Saque realizado. Saldo atual: R$", saldoAtual - sacar)
else :
    print("Saldo insuficiente.")