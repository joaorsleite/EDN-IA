#Calculadora de IMC

#Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
#O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, 
#calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

# imc < 18.5: classificacao = "Abaixo do peso"
# imc < 25: classificacao = "Peso normal"
# imc < 30: classificacao = "Sobrepeso"
#Para os demais cenários: classificacao = "Obeso"

# Dados do usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Classificação com base no IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

# Exibindo o resultado da classificação
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
