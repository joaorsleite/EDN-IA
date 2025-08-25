#Calculadora de Preço Total
#esenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

# Informações do produto
nome_produto = "Cadeira Infantil"
preco_unitario = 15.0
quantidade = int(input("Quantas unidades você deseja?: "))

# Cálculo do preço total
preco_total = preco_unitario * quantidade

# Exibição das informações
print("Produto:", nome_produto)
print("Preço unitário: R$", preco_unitario)
print("Quantidade:", quantidade)
print("Preço total: R$", preco_total)

