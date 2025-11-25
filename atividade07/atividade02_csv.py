# Atividade Prática 07 - Questão 2
#
# Crie um script que escreva dados pessoais em um arquivo CSV.
#
# -----------------------------------------------------------------

import csv

# Dados que serão escritos no arquivo CSV
dados = [
    ['Nome', 'Idade', 'Cidade'],
    ['Ana', 28, 'São Paulo'],
    ['Bruno', 35, 'Rio de Janeiro'],
    ['Carla', 42, 'Belo Horizonte']
]

# Nome do arquivo CSV
nome_arquivo = 'dados_pessoas.csv'

# Abre o arquivo no modo de escrita ('w')
# O 'newline=' evita linhas em branco extras no arquivo
with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    # Cria um objeto para escrever no arquivo
    escritor = csv.writer(arquivo_csv)
    
    # Escreve todas as linhas de uma vez
    escritor.writerows(dados)

print("Exemplo resolvido:")
print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
print("-" * 20)

# Código interativo:
print("Opção para testar outros valores:")
nome_novo = input("Digite seu nome: ")
idade_nova = int(input("Digite sua idade: "))
cidade_nova = input("Digite sua cidade: ")

# Adiciona os novos dados à lista
dados.append([nome_novo, idade_nova, cidade_nova])

# Escreve a lista completa novamente no arquivo
with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerows(dados)

print(f"Dados de '{nome_novo}' adicionados ao arquivo '{nome_arquivo}'.")