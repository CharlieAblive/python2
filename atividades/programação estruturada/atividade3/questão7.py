print("Cadastro de doação de sangue")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
idadePode = idade >= 16 and idade <= 69
podeDoar = idadePode == True and peso >= 50.0
print("Você pode doar sangue? ", podeDoar)