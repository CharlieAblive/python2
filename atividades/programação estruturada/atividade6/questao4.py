escolha = int(input("Escolha: \n1 - Mostrar saudação\n2 - Sair do programa\n"))
while escolha >=0:
    if escolha ==1:
        print("Olá. seja muito bem-vindo(a)! \n1 - Mostrar saudação\n2 - Sair do programa\n")
        escolha = int(input())
    elif escolha == 2:
        print("Programa encerrado.")
        break
    else:
        escolha = int(input("Opção invalida."))

        
    