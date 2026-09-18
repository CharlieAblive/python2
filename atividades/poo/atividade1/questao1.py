class Pessoa:
    def __init__(self, nome, cpf, idade, qualidade, defeito):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.qualidade = qualidade
        self.defeito = defeito

    def __str__(self):
        return f"{self.nome}{self.cpf}{self.idade}{self.qualidade}{self.defeito}"

    def mostrarInfo(self):
        print(f"Nome: {self.nome}\nCPF: {self.cpf}\nIdade: {self.idade}")

    def elogio(self):
        print(f"{self.nome} é bom(boa) sendo {self.qualidade}.")

    def critica(self):
        print(f"{self.nome} {self.defeito}.")


#todas as pessoas mencionadas são meus amigos e todos consentiram a estar no meu código (para fins legais)    
pessoa1 = Pessoa("Charlie",
                 12345678900,
                 20,
                 "gamedev",
                 "tem rinite")

pessoa2 = Pessoa("JP",
                 12345678900,
                 24,
                 "filósofo",
                 "é dislexo")

pessoa3 = Pessoa("Amanda",
                 12345678900,
                 28,
                 "maquiadora",
                 "é dramática (demais)")

pessoa4 = Pessoa("Brino",
                 12345678900,
                 25,
                 "artista",
                 "é tchola")

pessoa5 = Pessoa("Sophia",
                 12345678900,
                 14,
                 "fã de Queen",
                 "é chatinha ela")


pessoas = [pessoa1, pessoa2, pessoa3, pessoa4, pessoa5]

for pessoa in pessoas:
    pessoa.mostrarInfo()
    pessoa.elogio()
    pessoa.critica()
    print()

