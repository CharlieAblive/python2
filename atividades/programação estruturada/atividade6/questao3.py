numeroDigitado = int(input("Digite um numero: "))
soma = 0
while numeroDigitado != 0:
    soma += numeroDigitado
    numeroDigitado = int(input("Digite um numero:"))
    if numeroDigitado == 0:
        print("A soma de todos os seus números dá", soma)