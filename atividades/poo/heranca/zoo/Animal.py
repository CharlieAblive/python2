class Animal:
    def __init__ (self, nome, idade, nivelFome):
        self.__nome = nome
        self.__idade = idade
        self.__nivelFome = nivelFome

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def nivelFome(self):
        return self.__nivelFome

    @nome.setter
    def nome(self, nomeNovo):
        self.__nome == nomeNovo

    @idade.setter
    def idade(self, idadeNova):
        if idadeNova > 0:
            self.__idade == idadeNova
            print("Idade Atualizada.")
        else:
            print(f"Erro: Idade inválida.")

    @nivelFome.setter
    def nivelFome(self, fomeNova):
        if fomeNova < 0:
            self.__nivelFome == 0
            print("O animal está sem fome!")
        elif fomeNova > 100:
            self.__nivelFome == 100
            print("O animal está faminto!")
        else:
            self.__nivelFome == fomeNova

    def alimentar(self, porcao):
        if porcao > 0:
            self.__nivelFome -= porcao
            print("Animal alimentado.")
        else:
            print("Erro: Quantidade inválida")

    def emitirSom(self):
        pass

    def animalStatus(self):
        pass