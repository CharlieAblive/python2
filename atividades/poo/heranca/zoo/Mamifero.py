from Animal import Animal

class Mamifero(Animal):
    def __init__(self, nome, idade, nivelFome, velocidade):
        self.__velocidade = velocidade
        super().__init__(nome, idade, nivelFome)
        
    def correr(self):
        self.nivelFome(self.nivelFome - 20)
        print(f"{self.nome} correu a {self.__velocidade}Km/h!")

    def emitirSom(self):
        print(f"{self.nome} ruge alto!")

    def exibirResumo(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\n Fome: {self.nivelFome}%\nVelocidade: {self.__velocidade}Km/h")

if __name__ == "__main__":
    leao = Mamifero("simba", 3, 54, 70)
    leao.exibirResumo()