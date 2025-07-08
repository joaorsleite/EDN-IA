#3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
#a - deve ter pelo menos 8 caracteres.
#b - deve conter pelo menos um número.

def verificar_senha():
    print("### Verificador de Senha ###")
    senha = input("Digite a senha: ")

    # Critério 1: Pelo menos 8 caracteres
    if len(senha) < 8:
        print("Senha muito curta! Deve ter pelo menos 8 caracteres.")
        return

    # Critério 2: Pelo menos um número
    contem_numero = any(caractere.isdigit() for caractere in senha)

    if not contem_numero:
        print("A senha deve conter pelo menos um número.")
        return

    print("Senha válida! Atende aos critérios básicos de segurança.")

# Executar o verificador
verificar_senha()
