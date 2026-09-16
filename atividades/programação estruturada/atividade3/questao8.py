print("Calculadora de lucro")
nomeProduto = input("Nome do produto: ")
custoFabrica = float(input("Custo de fabrica do produto: "))
custoVenda = float(input("Valor que será cobrado na loja:"))
lucro = (custoVenda - custoFabrica) >= 20
print("O produto", nomeProduto, "lucrou", (custoVenda - custoFabrica), ". O lucro foi bom? ", lucro)
