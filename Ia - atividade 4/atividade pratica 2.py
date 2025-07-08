#2 - Criar um código que registre as notas de alunos e calcular a média da turma.

def registrar_notas():
    print("### Registro de Notas ###")
    
    try:
        quantidade_alunos = int(input("Digite o número de alunos na turma: "))
    except ValueError:
        print("Você precisa digitar um número inteiro válido.")
        return

    if quantidade_alunos <= 0:
        print("O número de alunos deve ser maior que zero.")
        return

    notas = []
    for i in range(quantidade_alunos):
        try:
            nota = float(input(f"Digite a nota do aluno {i + 1}: "))
            if nota < 0 or nota > 10:
                print("Nota inválida! Digite uma nota entre 0 e 10.")
                return
            notas.append(nota)
        except ValueError:
            print("Digite uma nota válida.")
            return

    media_turma = sum(notas) / quantidade_alunos
    print(f"\nA média da turma é: {media_turma:.2f}")

# Executar o programa
registrar_notas()
