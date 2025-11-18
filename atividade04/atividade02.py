# 2 - Criar um código que registre as notas de alunos e calcular a média da turma.

def media_da_turma():
    print("=== Registro de Notas e Média da Turma ===")
    # Lista para guardar tuplas (nome, nota) de cada aluno.
    alunos = []
    while True:
        # Ler o nome do aluno; ENTER vazio encerra o cadastro.
        nome = input("Nome do aluno (ou tecle o ENTER para finalizar a lista dos alunos): ").strip()
        if nome == "":
            break  # Sai do loop quando o usuário não digita um nome.

        try:
            # Ler a nota e converta para float.
            nota = float(input(f"Nota de {nome}: ").strip())
            # Validação simples: nota deve estar entre 0 e 10.
            if nota < 0 or nota > 10:
                print("Atenção: insira uma nota entre 0 e 10.")
                continue  # Volta ao início do loop para pedir novamente.
            # Armazenar o par (nome, nota) na lista.
            alunos.append((nome, nota))
        except ValueError:
            # Caso a nota não seja um número válido.
            print("Entrada inválida para nota. Tente novamente.")

    # Se nenhum aluno foi cadastrado, informa e encerra.
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    # Calculamos a soma das notas usando compreensão de lista.
    soma = sum(nota for _, nota in alunos)
    # Média é a soma dividida pela quantidade de alunos.
    media = soma / len(alunos)

    # Exibimos um pequeno relatório.
    print("\n--- Relatório ---")
    for nome, nota in alunos:
        print(f"- {nome}: {nota}")
    print(f"\nQuantidade de alunos: {len(alunos)}")
    print(f"Média da turma: {media:.2f}")  # :.2f formata com 2 casas decimais.

if __name__ == "__main__":
    media_da_turma()