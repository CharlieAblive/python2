print("Você passou de ano?")
nota1 = float(input("Sua nota do primeiro semestre:"))
nota2 = float(input("Sua nota do segundo semestre:"))
frequencia = float(input("Sua porcentagem de frequência:"))
media = (nota1 + nota2)/2
passou = media >= 6.0 and frequencia >= 75

print("Passou de ano?", passou)