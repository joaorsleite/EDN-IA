"""
    Calcula o valor do desconto e o preço final com base no percentual fornecido.

    Parâmetros:
    preco (float): Preço original do produto.
    percentual_desconto (float): Percentual de desconto a ser aplicado.

    Retorna:
    tuple: (valor_desconto, preco_final), ambos arredondados para 2 casas decimais.
    """

def calcular_desconto(preco, percentual_desconto):

    valor_desconto = preco * (percentual_desconto / 100)
    preco_final = preco - valor_desconto
    return round(valor_desconto, 2), round(preco_final, 2)

# Interação com o usuário
preco_original = float(input("Digite o preço original do produto: R$ "))
desconto = float(input("Digite o percentual de desconto (%): "))

valor_desc, preco_com_desc = calcular_desconto(preco_original, desconto)

#Resultado
print(f"\nValor do desconto: R$ {valor_desc:.2f}")
print(f"Preço final com desconto: R$ {preco_com_desc:.2f}")
