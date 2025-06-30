#Conversor de moedas 
#Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

# Valores fixados
valor_em_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

#Calculadora de conversão 
valor_dolar = valor_em_reais / taxa_dolar
valor_euro = valor_em_reais / taxa_euro


#Valores 
print(f"Valor em reais: R$ {valor_em_reais:.2f}")
print(f"Convertido para dólares: US$ {valor_dolar:.2f}")
print(f"Convertido para euros: € {valor_euro:.2f}")