# 1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).

def calculadora():
    print("==== Calculadora Básica ====")
    print("Operações disponíveis:")
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    
    operacao = input("Escolha a operação (1/2/3/4): ")
    
    if operacao not in ['1', '2', '3', '4']:
        print("Operação inválida!")
        return
    
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Você precisa digitar números válidos.")
        return
    
    if operacao == '1':
        resultado = num1 + num2
        operador = '+'
    elif operacao == '2':
        resultado = num1 - num2
        operador = '-'
    elif operacao == '3':
        resultado = num1 * num2
        operador = '*'
    elif operacao == '4':
        if num2 == 0:
            print("Erro: Divisão por zero!")
            return
        resultado = num1 / num2
        operador = '/'
    
    print(f"\nResultado: {num1} {operador} {num2} = {resultado}")

# Executar a calculadora
calculadora()
