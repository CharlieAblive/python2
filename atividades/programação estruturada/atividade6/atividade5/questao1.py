print("Bem vindo a lanchonete.")
lanche = ("Qual lanche você vai querer?\n1- Cachorro quente --- R$ 10,00\n2- Hambúrguer --- R$ 15,00\n3- Batata Frita --- R$ 8,00\n4- Refrigerante --- R$ 5,00\n")
match lanche:
    case '1':
        print("Aproveite seu cachorro quente!")
    case '2':
            print("Aproveite seu hamburguer!")
    case '3':
            print("Aproveite sua batata frita!")
    case '4':
            print("Aproveite seu refrigerante!")
    case _:
            print("Código inválido.")


    