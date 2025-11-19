# 3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
# a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
# b - Preço final: Determina o novo preço após o desconto.
# c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
# d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.

#  Calculadora de Desconto (interativa)
# Regra: Enter vazio em qualquer pergunta encerra o programa.

def calcular_desconto(preco: float, porcentagem: float) -> float:
    """
    Calcula o valor do desconto dado um preço e uma porcentagem.
    Ex.: preco=200, porcentagem=10 -> retorna 20.0
    """
    return preco * (porcentagem / 100)

def preco_final(preco: float, porcentagem: float) -> float:
    """
    Retorna o preço final após aplicar o desconto, arredondado para 2 casas.
    """
    return round(preco - calcular_desconto(preco, porcentagem), 2)

def programa_desconto_interativo():
    print("Calculadora de Descontos — pressione Enter vazio para sair.\n")
    while True:
        # Lê o preço do produto
        preco_str = input("Preço do produto (ex: 199,90): ").strip()
        if preco_str == "":
            print("Encerrando...")
            break

        # Lê a porcentagem de desconto
        porc_str = input("Porcentagem de desconto (ex: 15 para 15%): ").strip()
        if porc_str == "":
            print("Encerrando...")
            break

        try:
            # Converte vírgula para ponto e transforma em float
            preco = float(preco_str.replace(',', '.'))
            porcentagem = float(porc_str.replace(',', '.'))

            # Validações básicas
            if preco < 0:
                print("Erro: o preço não pode ser negativo.\n")
                continue
            if not (0 <= porcentagem <= 100):
                print("Erro: a porcentagem deve estar entre 0 e 100.\n")
                continue

            # Cálculos
            valor_desc = calcular_desconto(preco, porcentagem)
            novo_preco = preco_final(preco, porcentagem)

            # Exibição formatada
            print(f"\nPreço original: R$ {preco:.2f}")
            print(f"Desconto: {porcentagem:.2f}% (R$ {valor_desc:.2f})")
            print(f"Preço final: R$ {novo_preco:.2f}\n")

        except ValueError:
            print("Erro: digite números válidos (ex: 199.90 ou 199,90; 10 ou 10,5).\n")

if __name__ == "__main__":
    programa_desconto_interativo()