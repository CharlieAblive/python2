class Produto:
    def __init__(self, nome, preco, quant_estoque):
        self.__nome = nome
        self.__preco = preco
        self.__quant_estoque = quant_estoque


    @property
    def nome(self):
        print(self.__nome) 
    @property
    def preco(self):
        print(self.__preco)
    @property
    def quant_estoque(self):
        print(self.__quant_estoque)

    @preco.setter
    def preco(self, novoPreco):
        self.__preco = novoPreco

    @quant_estoque.setter
    def quant_estoque(self, novaQuant):
        self.__quant_estoque = novaQuant


    def adicionarEstoque(self, quant):
        if quant > 0:
            self.__quant_estoque += quant
        else:
            print("Erro: Quantidade não pode ser menor que 0.")

    def realizarVenda(self, quant):
        if quant > 0 and quant <= self.__quant_estoque:
            self.__quant_estoque -= quant
        else:
            print("Erro: Estoque insuficiente.")

    def aplicarDesconto(self, desconto):
        if desconto <= 80 and desconto > 0:
            self.__preco = (self.__preco * desconto)/100
        else:
            print("Erro: Desconto inválido.")

    def exibirStatus(self):
        return f"Produto: {self.__nome}\nPreço: {self.__preco}\nEstoque: {self.__quant_estoque}"
    


produto1 = Produto("Teste", 5.0, 12)

produto1.adicionarEstoque(int(input("Quantidade de produtos a serem adicionados: ")))
produto1.realizarVenda(int(input("Quantidade de produtos a serem vendidos: ")))
produto1.aplicarDesconto(int(input("Insira o valor de desconto: ")))
print(produto1.exibirStatus())    

    
        