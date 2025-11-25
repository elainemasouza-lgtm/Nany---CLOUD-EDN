# Atividade Prática 07 - Questão 4
#
# Crie um script que leia e escreva dados em um arquivo JSON.
#
# -----------------------------------------------------------------

import json

# Dados que serão escritos no arquivo JSON
dados_pessoa = {
    'nome': 'João',
    'idade': 30,
    'cidade': 'Curitiba'
}

nome_arquivo = 'pessoa.json'

# --- Escrevendo no arquivo JSON ---
# Abre o arquivo no modo de escrita ('w')
with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
    # O 'indent=4' deixa o arquivo mais fácil de ler
    json.dump(dados_pessoa, arquivo_json, indent=4, ensure_ascii=False)

print("Exemplo resolvido:")
print(f"Dados escritos no arquivo '{nome_arquivo}' com sucesso!")
print("-" * 20)

# --- Lendo do arquivo JSON ---
# Abre o arquivo no modo de leitura ('r')
try:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
        dados_lidos = json.load(arquivo_json)
        
        print("Dados lidos do arquivo:")
        print(f"Nome: {dados_lidos['nome']}")
        print(f"Idade: {dados_lidos['idade']}")
        print(f"Cidade: {dados_lidos['cidade']}")
except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")