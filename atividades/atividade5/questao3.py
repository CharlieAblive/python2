turno = input("Digite o seu turno: ")

match turno:
    case 'm'|'M':
        print("Bom Dia!")
    case 'v'|'V':
        print("Boa Tarde!")
    case 'm'|'M':
        print("Boa Noite!")
    case _:
        print("Invalido")