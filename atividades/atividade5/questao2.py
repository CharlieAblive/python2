print("Detector de vogal")

letra = chr(input("Digite sua letra:"))

match letra:
    case 'a'|'e'|'i'|'o'|'u':
        print("Vogal detectada!")
    case _:
        print( letra, "não é uma vogal.")
