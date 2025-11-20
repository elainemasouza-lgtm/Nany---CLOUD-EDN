# 3 - Crie um programa que consulte informações de um  na API , retorne logradouro, bairro, cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.

import re
import requests

VIACEP_URL = "https://viacep.com.br/ws/{cep}/json/"

def normalizar_cep(cep_str: str) -> str:
    """
    Remove caracteres não numéricos e valida o tamanho (8 dígitos).
    Retorna o CEP limpo (8 dígitos) ou lança ValueError se inválido.
    """
    apenas_digitos = re.sub(r"\D", "", cep_str)
    if len(apenas_digitos) != 8:
        raise ValueError("CEP deve conter 8 dígitos (ex.: 01001000).")
    return apenas_digitos

def consultar_cep(cep: str, timeout: int = 10):
    """
    Consulta a API ViaCEP. Retorna (dados, erro).
    dados é um dicionário com logradouro, bairro, cidade, estado.
    erro é uma string com a mensagem de erro, ou None se não houve erro.
    """
    try:
        url = VIACEP_URL.format(cep=cep)
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
        dados = resp.json()

        # A API ViaCEP retorna {"erro": true} quando o CEP não existe
        if isinstance(dados, dict) and dados.get("erro"):
            return None, "CEP não encontrado."

        # Extrair campos de interesse
        logradouro = dados.get("logradouro") or ""
        bairro = dados.get("bairro") or ""
        cidade = dados.get("localidade") or ""
        estado = dados.get("uf") or ""

        # Checagem mínima de conteúdo
        if not any([logradouro, bairro, cidade, estado]):
            return None, "Resposta da API não contém dados suficientes."

        return {
            "logradouro": logradouro,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado
        }, None

    except requests.exceptions.RequestException:
        return None, "Falha ao conectar à API. Verifique sua conexão e tente novamente."
    except ValueError:
        return None, "Falha ao processar a resposta da API."

def mostrar_menu():
    print("\n===== Consulta de CEP (ViaCEP) =====")
    print("1) Consultar CEP")
    print("0) Sair")

def main():
    while True:
        mostrar_menu()
        opc = input("Escolha uma opção: ").strip()

        if opc == "1":
            cep_input = input("Digite o CEP (com ou sem hífen, ex.: 01001-000): ").strip()
            try:
                cep = normalizar_cep(cep_input)
            except ValueError as e:
                print(f"Entrada inválida: {e}")
                continue

            print("Consultando API ViaCEP...")
            resultado, erro = consultar_cep(cep)
            if erro:
                print(f"Falha: {erro}")
            else:
                print("\nResultado:")
                print(f"- Logradouro: {resultado['logradouro']}")
                print(f"- Bairro:     {resultado['bairro']}")
                print(f"- Cidade:     {resultado['cidade']}")
                print(f"- Estado:     {resultado['estado']}")

        elif opc == "0":
            print("Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()


# Programa: Consulta interativa de CEP usando a API ViaCEP

# Descrição:
# - Este programa consulta a API pública ViaCEP (https://viacep.com.br/) a partir de um CEP digitado.
# - Retorna e exibe logradouro, bairro, cidade e estado.
# - É interativo em console, com menu simples (consultar CEP ou sair).
# - Faz validação do CEP (aceita com ou sem hífen; exige 8 dígitos).
# - Trata erros de conexão/HTTP e casos em que o CEP não existe, mostrando mensagens de falha.

# Requisitos:
# - Python 3.8+ e a biblioteca 'requests' instalada:
#   - python -m pip install requests

# Como usar:
# 1) Execute: python nome_do_arquivo.py
# 2) Escolha a opção 1 para consultar.
# 3) Digite o CEP (ex.: 01001-000 ou 01001000).
# 4) Veja o logradouro, bairro, cidade e estado. Em caso de CEP inexistente ou erro de rede, será exibida uma mensagem de falha.