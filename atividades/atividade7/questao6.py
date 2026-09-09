numeroSecreto = 78
chute = int(input("Dê um palpite de um numero: "))
quantTent = 0
while chute != numeroSecreto:
    chute = int(input("Errado! Tente de novo: "))
    quantTent += 1

print(f"Você acertou em {quantTent} tentativas.")
