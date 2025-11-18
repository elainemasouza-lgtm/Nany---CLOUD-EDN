# 3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
# a - deve ter pelo menos 8 caracteres.
# b - deve conter pelo menos um número.


# A função retorna uma tupla: (bool_valida, lista_de_erros).
# - bool_valida: True se passou em todos os critérios, False caso contrário.
# - lista_de_erros: mensagens explicando o que faltou.

def verificar_senha(senha: str) -> tuple[bool, list]:
    erros = []  # Lista para acumular mensagens de erro.

    # Critério 1: tamanho mínimo.
    if len(senha) < 8:
        erros.append("A senha deve ter pelo menos 8 caracteres.")

    # Critério 2: pelo menos um dígito numérico.
    # any(...) retorna True se algum caractere atender à condição isdigit().
    if not any(ch.isdigit() for ch in senha):
        erros.append("A senha deve conter pelo menos um número.")

    # Dicas opcionais (descomente se quiser exigir mais critérios):
    # if not any(ch.islower() for ch in senha):
    #     erros.append("Inclua ao menos uma letra minúscula.")
    # if not any(ch.isupper() for ch in senha):
    #     erros.append("Inclua ao menos uma letra maiúscula.")
    # if not any(ch in "!@#$%^&*()-_=+[]{};:,.?/\\|" for ch in senha):
    #     erros.append("Inclua ao menos um caractere especial.")

    # A senha é válida se a lista de erros estiver vazia.
    return (len(erros) == 0, erros)

def main():
    print("=== Verificador de Senha ===")
    # Ler a senha do usuário (observação: input exibe o que é digitado).
    senha = input("Digite a senha para verificar: ")
    ok, erros = verificar_senha(senha)

    # Se ok for True, passou; caso contrário, lista os problemas.
    if ok:
        print("Senha válida! Atende aos critérios.")
    else:
        print("Senha inválida. Problemas encontrados:")
        for e in erros:
            print(f"- {e}")

if __name__ == "__main__":
    main()