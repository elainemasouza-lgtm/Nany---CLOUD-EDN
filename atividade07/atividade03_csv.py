# Atividade Prática 07 - Questão 3
#
# Crie um script que leia um arquivo CSV e exiba os dados na tela.
#
# -----------------------------------------------------------------

import csv

# Nome do arquivo CSV que será lido
nome_arquivo = 'dados_pessoas.csv'

# Exemplo resolvido:
print("Exemplo resolvido (lendo o arquivo 'dados_pessoas.csv'):")

# Tenta abrir e ler o arquivo
try:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        for linha in leitor:
            print(', '.join(linha))
except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado. Execute o exercício 2 primeiro.")

print("-" * 20)

# Código interativo:
print("Opção para testar lendo outro arquivo:")
nome_arquivo_novo = input("Digite o nome do arquivo CSV para ler (ex: 'dados_pessoas.csv'): ")

try:
    with open(nome_arquivo_novo, 'r', encoding='utf-8') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        print("Conteúdo do arquivo:")
        for linha in leitor:
            print(', '.join(linha))
except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo_novo}' não foi encontrado.")