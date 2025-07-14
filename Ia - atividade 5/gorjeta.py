#1 - Crie uma função que calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
#Parâmetros:
#a - valor_conta (float): O valor total da conta
#b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
#c - retorna: float: O valor da gorjeta calculada

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
   
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

# Exemplo de uso:
valor = float(input("Digite o valor da conta: "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))

print(f"Gorjeta: R$ {calcular_gorjeta(valor, porcentagem):.2f}")
