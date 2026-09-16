print("Qual estação do ano é esta?")
mes = input("Digite o mês atual: ")
match mes:
    case 12|1|2:
        print("A estação é verão.") 
    case 3|4|5:
        print("A estação é outono.") 
    case 6|7|8:
        print("A estação é inverno")
    case 9|10|11:
        print("A estação é primavera.")
    case _:
        print("Mês invalido.")