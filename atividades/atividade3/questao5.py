print("Cupom Frete Gratis")
valorCompra = float(input("Digite o valor da sua compra: "))
temVIP = input("Você é VIP? (1 para sim, 0 para não) ")
freteGratis = valorCompra >= 250.00 or temVIP == 1
print("Você tem frete gratis? ", freteGratis)