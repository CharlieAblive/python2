numeroSecreto = 78
chute = int(input("Dê um palpite de um numero: "))
while chute != numeroSecreto:
    chute = int(input("Errado! Tente de novo: "))
    if chute == numeroSecreto:
        print("você acertou!")
        break