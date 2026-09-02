print("Vamo rachar a conta?")

valorTotal = float(input("Digite o valor total da compra:"))
quantPessoas = float(input("Quantas pessoas vão dividir a conta?"))

print("O valor total da compra foi de R$", valorTotal, ", e cada pessoa deve pagar R$", (valorTotal/quantPessoas))