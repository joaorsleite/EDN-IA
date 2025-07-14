"""
    Calcula a quantidade de dias que um indivíduo está vivo.

    Parâmetro:
    data_nascimento (str): Data de nascimento no formato 'dd/mm/aaaa'.

    Retorna:
    int: Quantidade de dias vividos até a data atual.
    """

from datetime import datetime

def calcular_dias_vivo(data_nascimento):
    
    nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    hoje = datetime.now()
    dias_vividos = (hoje - nascimento).days
    return dias_vividos

# Interação com o usuário
data = input("Digite sua data de nascimento (dd/mm/aaaa): ")
dias = calcular_dias_vivo(data)
print(f"Você está vivo há {dias} dias.")
