listafuncionario = []
listademissao = []
listapromocao = []
opcao = 's'
rodando = 's'
print("Controle de funcionários")
while rodando == 's':
    match input("1- Adicionar funcionário\n" \
                "2- Remover funcionário\n" \
                "3- Adicionar funcionário à lista de demissão\n" \
                "4- Adicionar funcionário à lista de promoção\n" \
                "5- Sair"):
        case '1':
                while opcao == 's':
                    listafuncionario.append(input("Adicione um funcionário: "))
                    opcao = input("Deseja adicionar mais funcionários? (s/n)")
        case '2':
                while opcao == 's':
                    funcionario = input("Remova um funcionário: ")
                    for i in listafuncionario:
                        if i == funcionario:
                            listafuncionario.remove(funcionario)
                            opcao = input("Deseja remover outro funcionário? (s/n)")
                        else:
                            opcao = input("Este funcionário não está na lista. Deseja tentar de novo? (s/n)")
        case '3':

        case '4':        

        case '5':

        case _:



