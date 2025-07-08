#4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.

def analisar_numeros():
    print("## Analisador de Números ##")
    
    try:
        quantidade = int(input("Quantos números você deseja digitar? "))
    except ValueError:
        print("Digite um número inteiro válido.")
        return

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        return

    pares = 0
    impares = 0

    for i in range(quantidade):
        try:
            numero = int(input(f"Digite o {i + 1}º número: "))
        except ValueError:
            print("Por favor, digite apenas números inteiros.")
            return
        
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    print("\n### Resultado ###")
    print(f"Total de números pares: {pares}")
    print(f"Total de números ímpares: {impares}")

# Executar o analisador
analisar_numeros()
