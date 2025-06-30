#Calculadora de Desconto
#Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

# Informações do produto
nome_produto = "Camiseta"
preco_original = 50.00
desconto = 20

# Cálculo do valor do desconto
valor_desconto = preco_original * (desconto / 100)

# Cálculo do preço final
preco_final = preco_original - valor_desconto

#Resultados 
print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final com desconto: R$ {preco_final:.2f}")
