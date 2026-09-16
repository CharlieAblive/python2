def notaBimestre(nome, nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4)/4
    print(f"O aluno {nome} teve a média final de {media}")

nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a nota do 1 bimestre"))
nota2 = float(input("Digite a nota do 2 bimestre"))
nota3 = float(input("Digite a nota do 3 bimestre"))
nota4 = float(input("Digite a nota do 4 bimestre"))

notaBimestre(nome, nota1, nota2, nota3, nota4)
