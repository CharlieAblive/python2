from Animal import Animal

class Ave(Animal):
    def __init__(self, nome, idade, nivelFome, envergadura):
        self.__envergadura = envergadura
        super().__init__(nome, idade, nivelFome)
        
    def voar(self):
        if self.nivelFome <= 80:
            print(f"{self.nome} voa com suas asas de {self.__envergadura}cm.")
        else:
            print(f"{self.nome} está faminto demais para voar.")

    def emitirSom(self):
        print(f"{self.nome} canta melodicamente!")

    def exibirResumo(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nFome: {self.nivelFome}%\nEnvergadura: {self.__envergadura}cm.")

if __name__ == "__main__":
    pombo = Ave("pruu", 3, 54, 70)
    pombo.exibirResumo()