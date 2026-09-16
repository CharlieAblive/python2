senha = "123456"
senhaDigitada = input("Digite a senha:")

if senhaDigitada == senha:
        print("Acesso permitido")
else:
    while senhaDigitada != senha:
        senhaDigitada = input("Senha errada! Tente de novo: ")
        if senhaDigitada == senha:
            print("Acesso permitido")
            