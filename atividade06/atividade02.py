
# 2 -   Crie um programa que  acesse a API  para buscar um usuário fictício aleatório. exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha.


import requests

API_URL = "https://randomuser.me/api/"

def buscar_usuario(nationality=None, timeout=10):
    """
    Busca um usuário aleatório.
    nationality: código(s) de nacionalidade (ex.: 'br', 'us', 'gb' ou 'br,us').
    """
    params = {}
    if nationality:
        params["nat"] = nationality  # ver docs: https://randomuser.me/documentation#nationalities

    try:
        resp = requests.get(API_URL, params=params, timeout=timeout)
        resp.raise_for_status()
        dados = resp.json()
        resultados = dados.get("results", [])
        if not resultados:
            return None, "Resposta da API não contém usuários."

        u = resultados[0]
        nome = u.get("name", {})
        primeiro = nome.get("first", "")
        ultimo = nome.get("last", "")
        nome_completo = f"{primeiro} {ultimo}".strip()

        email = u.get("email", "desconhecido")
        local = u.get("location", {})
        pais = local.get("country", "desconhecido")

        return {"nome": nome_completo, "email": email, "pais": pais}, None

    except requests.exceptions.RequestException:
        return None, "Falha ao conectar à API. Verifique sua conexão e tente novamente."
    except ValueError:
        return None, "Falha ao processar a resposta da API."

def mostrar_menu():
    print("\n===== Usuário Aleatório (Random User) =====")
    print("1) Buscar usuário")
    print("2) Definir nacionalidade preferida")
    print("3) Salvar último resultado em arquivo")
    print("0) Sair")

def input_s_n(msg, padrao=None):
    sufixo = " [s/n]"
    if padrao in ("s", "n"):
        sufixo += f" (padrão: {padrao})"
    while True:
        r = input(msg + sufixo + ": ").strip().lower()
        if not r and padrao in ("s", "n"):
            return padrao == "s"
        if r in ("s", "sim"):
            return True
        if r in ("n", "nao", "não"):
            return False
        print("Responda com 's' ou 'n'.")

def main():
    ultimo_resultado = None
    nacionalidade = None  # exemplos válidos: 'br', 'us', 'gb', 'fr', ou múltiplas: 'br,us'

    while True:
        mostrar_menu()
        opc = input("Escolha uma opção: ").strip()

        if opc == "1":
            print("\nBuscando usuário..." + (f" (nat={nacionalidade})" if nacionalidade else ""))
            resultado, erro = buscar_usuario(nationality=nacionalidade)
            if erro:
                print(f"Falha: {erro}")
            else:
                ultimo_resultado = resultado
                print("Usuário encontrado:")
                print(f"- Nome:  {resultado['nome']}")
                print(f"- E-mail:{resultado['email']}")
                print(f"- País:  {resultado['pais']}")

                if input_s_n("Buscar outro agora?", "n"):
                    continue

        elif opc == "2":
            print("\nDefina a nacionalidade preferida.")
            print("Exemplos: 'br', 'us', 'gb', 'fr'. Para múltiplas: 'br,us'. Vazio para qualquer país.")
            nat = input("Nacionalidade(s): ").strip().lower()
            nacionalidade = nat if nat else None
            print(f"Nacionalidade preferida: {nacionalidade or 'qualquer'}")

        elif opc == "3":
            if not ultimo_resultado:
                print("Nenhum resultado para salvar. Busque um usuário primeiro.")
                continue
            nome_arq = input("Nome do arquivo (Enter para 'usuario.txt'): ").strip() or "usuario.txt"
            try:
                with open(nome_arq, "w", encoding="utf-8") as f:
                    f.write(f"Nome: {ultimo_resultado['nome']}\n")
                    f.write(f"E-mail: {ultimo_resultado['email']}\n")
                    f.write(f"País: {ultimo_resultado['pais']}\n")
                print(f"Dados salvos em: {nome_arq}")
            except Exception as e:
                print(f"Falha ao salvar arquivo: {e}")

        elif opc == "0":
            print("Até mais!")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()



#     Descrição:

# Consulta a API pública Random User (https://randomuser.me/api/) para obter um usuário fictício aleatório.
# Exibe nome, e-mail e país do usuário.
# Permite definir uma nacionalidade preferida (ex.: br, us, gb ou múltiplas: br,us).
# Permite salvar o último resultado em um arquivo .txt.
# Trata erros de conexão, HTTP e JSON, exibindo mensagens amigáveis.