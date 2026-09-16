print("Formulario de cadastro")
nome = input("Digite seu nome completo: ")
idade = int(input("Digite sua idade: "))
plano = bool(input("Você tem plano de saúde? Caso não tenha, deixe em branco. "))
aceito = idade >= 18 and plano == True
print("Seu nome é", nome, "você tem", idade, "Tem plano?", plano, "Você foi aceito?", aceito)

#debug rapido
#print(plano)
