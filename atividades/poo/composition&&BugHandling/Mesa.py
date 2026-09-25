from ItemPedido import ItemPedido

class Mesa:
    def __init__(self, numero):
        self.numero = numero
        self.listaPedido = []

    def adicionarPedido(self, numero, item: ItemPedido):
        try:
            self.listaPedido.append(item)
            print(f"{item.nome} foi adicionado à mesa {numero}.")
        except ValueError as erro:
            print(f"Erro: {erro}")


    def somarTotal(self, i: ItemPedido):
        try:
            soma = 0
            for i in self.listaPedido:
                soma += i.valor 
            print(f"O valor total dos pedidos é {soma}")
        except ValueError as erro:
            print(f"Erro: {erro}")
        

    def fecharConta(self):
        for i in self.listaPedido:
            print(f"{i.nome} --- {i.valor}")
            subtotal = self.somarTotal()
            taxaServiço = subtotal * 0.15
            print(f"Subtotal: {subtotal}\nTaxa de Serviço: {taxaServiço}\nTotal: {subtotal + taxaServiço}")
            self.listaPedido.remove(all)

mesa1 = Mesa(1)

mesa1.adicionarPedido(1, ItemPedido("Pizza 4Queijos", 45.00))
mesa1.adicionarPedido(1, ItemPedido("Coca-cola zero", 8.00))


print("\n--- TESTANDO ENTRADA INVÁLIDA ---")
mesa1.adicionarPedido(1, ItemPedido("Pudim", "quinze"))  # Deve exibir o ALERTA DO SISTEMA e não quebrar
mesa1.adicionarPedido(1, ItemPedido(nome = "Café", valor = "5,50"))     # Erro comum de vírgula, deve acionar o ALERTA


# 4. Adicionando mais um pedido válido após o erro
mesa1.adicionarPedido(1, ItemPedido("Suco de Laranja", 12.00))

mesa1.somarTotal(mesa1.listaPedido)



print("\n--- FECHAMENTO DA CONTA ---")
mesa1.fecharConta()

print("\n--- VERIFICANDO STATUS DA MESA APÓS FECHAMENTO ---")
mesa1.fecharConta() # A conta deve vir zerada

