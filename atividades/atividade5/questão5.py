num1 = input("Digite um número")
num2 = input("Digite outro número")
operador = input("qual operação você quer fazer? (+, -, *, /)")

match operador:
    case "+":
        print("A soma dos numeros é", num1 + num2)
    case "-":
        print("A subtração dos numeros é", num1-num2)
    case "*":
        print("A multiplicação dos numeros é", num1*num2)
    case "/":
        print("A divisão dos numeros é", num1/num2)
    case _:
        print("Erro")

