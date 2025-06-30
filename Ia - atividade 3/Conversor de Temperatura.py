#Conversor de Temperatura
# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

# Função para conversão de temperatura
def converter_temperatura(valor, origem, destino):
    if origem == "C":
        if destino == "F":
            return valor * 9/5 + 32
        elif destino == "K":
            return valor + 273.15
    elif origem == "F":
        if destino == "C":
            return (valor - 32) * 5/9
        elif destino == "K":
            return (valor - 32) * 5/9 + 273.15
    elif origem == "K":
        if destino == "C":
            return valor - 273.15
        elif destino == "F":
            return (valor - 273.15) * 9/5 + 32
    return None

# Solicitação dos dados do usuário
valor = float(input("Digite o valor da temperatura: "))
origem = input("Digite a unidade de origem (C, F ou K): ").upper()
destino = input("Digite a unidade de destino (C, F ou K): ").upper()

# Verificando se as unidades são válidas e diferentes
if origem in ["C", "F", "K"] and destino in ["C", "F", "K"] and origem != destino:
    resultado = converter_temperatura(valor, origem, destino)
    print(f"{valor:.2f}°{origem} equivale a {resultado:.2f}°{destino}")
else:
    print("Unidades inválidas ou iguais. Por favor, use C, F ou K e escolha unidades diferentes.")
