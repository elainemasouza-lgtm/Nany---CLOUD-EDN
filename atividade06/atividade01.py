# 1 - Crie um programa que gere senhas aleatórias com letras, números e símbolos e que o usuário  também escolha o tamanho da senha  para criar senhas seguras automaticamente.

import secrets
import string

try:
    import pyperclip
    TEM_PYPERCLIP = True
except Exception:
    TEM_PYPERCLIP = False

def gerar_senha(tamanho: int,
                usar_minusculas=True,
                usar_maiusculas=True,
                usar_numeros=True,
                usar_simbolos=True) -> str:
    if tamanho < 4:
        raise ValueError("Tamanho mínimo recomendado é 4.")
    
    grupos = []
    if usar_minusculas:
        grupos.append(string.ascii_lowercase)
    if usar_maiusculas:
        grupos.append(string.ascii_uppercase)
    if usar_numeros:
        grupos.append(string.digits)
    if usar_simbolos:
        grupos.append(string.punctuation)

    if not grupos:
        raise ValueError("Selecione pelo menos um tipo de caractere.")

    # Garantir ao menos um de cada grupo escolhido
    senha_chars = [secrets.choice(g) for g in grupos]

    # Conjunto total permitido
    todos = "".join(grupos)

    # Completar até o tamanho desejado
    senha_chars += [secrets.choice(todos) for _ in range(tamanho - len(senha_chars))]

    # Embaralhar
    secrets.SystemRandom().shuffle(senha_chars)

    return "".join(senha_chars)

def input_int(msg, minimo=None, maximo=None):
    while True:
        valor = input(msg).strip()
        if not valor:
            print("Por favor, digite um número.")
            continue
        if not valor.isdigit():
            print("Entrada inválida. Use apenas dígitos (0-9).")
            continue
        n = int(valor)
        if minimo is not None and n < minimo:
            print(f"Valor mínimo é {minimo}.")
            continue
        if maximo is not None and n > maximo:
            print(f"Valor máximo é {maximo}.")
            continue
        return n

def input_s_n(msg, padrao=None):
    sufixo = " [s/n]"
    if padrao is not None:
        sufixo = f" [s/n] (padrão: {padrao})"
    while True:
        resp = input(msg + sufixo + ": ").strip().lower()
        if not resp and padrao in ("s", "n"):
            return padrao == "s"
        if resp in ("s", "sim"):
            return True
        if resp in ("n", "nao", "não"):
            return False
        print("Responda com 's' para sim ou 'n' para não.")

def configurar_opcoes():
    print("\n== Configurações de caracteres ==")
    usar_minusculas = input_s_n("Incluir letras minúsculas?", "s")
    usar_maiusculas = input_s_n("Incluir letras maiúsculas?", "s")
    usar_numeros    = input_s_n("Incluir números?", "s")
    usar_simbolos   = input_s_n("Incluir símbolos?", "s")
    return usar_minusculas, usar_maiusculas, usar_numeros, usar_simbolos

def copiar_clipboard(texto):
    if not TEM_PYPERCLIP:
        print("Dica: instale 'pyperclip' para copiar para a área de transferência: pip install pyperclip")
        return
    try:
        pyperclip.copy(texto)
        print("Copiado para a área de transferência.")
    except Exception as e:
        print(f"Não foi possível copiar: {e}")

def mostrar_menu():
    print("\n===== Gerador de Senhas Interativo =====")
    print("1) Gerar senha")
    print("2) Gerar várias senhas")
    print("3) Configurar tipos de caracteres")
    print("4) Sobre dicas de segurança")
    print("0) Sair")

def dicas():
    print("\n== Dicas de segurança ==")
    print("- Use senhas longas (12+ caracteres).")
    print("- Misture maiúsculas, minúsculas, números e símbolos quando possível.")
    print("- Evite reutilizar senhas em diferentes serviços.")
    print("- Considere usar um gerenciador de senhas.")
    print("- Ative autenticação de dois fatores (2FA) sempre que disponível.")

def main():
    # Configurações padrão
    usar_minusculas = True
    usar_maiusculas = True
    usar_numeros = True
    usar_simbolos = True

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            tamanho = input_int("Tamanho da senha (mínimo 4, recomendado 12+): ", minimo=4)
            try:
                senha = gerar_senha(
                    tamanho,
                    usar_minusculas,
                    usar_maiusculas,
                    usar_numeros,
                    usar_simbolos
                )
                print(f"\nSenha gerada: {senha}")
                if input_s_n("Copiar para a área de transferência?", "n"):
                    copiar_clipboard(senha)
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            qtd = input_int("Quantas senhas gerar? ", minimo=1, maximo=1000)
            tamanho = input_int("Tamanho das senhas (mínimo 4): ", minimo=4)
            senhas = []
            try:
                for _ in range(qtd):
                    senhas.append(gerar_senha(
                        tamanho,
                        usar_minusculas,
                        usar_maiusculas,
                        usar_numeros,
                        usar_simbolos
                    ))
                print("\nSenhas geradas:")
                for i, s in enumerate(senhas, 1):
                    print(f"{i:02d}: {s}")
                if input_s_n("Salvar em arquivo 'senhas.txt'?", "n"):
                    nome = input("Nome do arquivo (Enter para 'senhas.txt'): ").strip() or "senhas.txt"
                    with open(nome, "w", encoding="utf-8") as f:
                        f.write("\n".join(senhas))
                    print(f"Arquivo salvo: {nome}")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "3":
            usar_minusculas, usar_maiusculas, usar_numeros, usar_simbolos = configurar_opcoes()
            print("Configurações atualizadas.")

        elif opcao == "4":
            dicas()

        elif opcao == "0":
            print("Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()


# secrets: gera valores aleatórios apropriados para criptografia e senhas (melhor que random).
# string: fornece conjuntos prontos de caracteres, como ascii_letters, digits, punctuation.
# pyperclip (opcional): copia texto para a área de transferência. O try/except define TEM_PYPERCLIP para sabermos se está disponível.