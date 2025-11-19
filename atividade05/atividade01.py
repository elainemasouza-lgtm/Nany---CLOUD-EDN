# 1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
# gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
# Parâmetros:
# a - valor_conta (float): O valor total da conta
# b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
# c - retorna: float: O valor da gorjeta calculada



# Função que calcula o valor da gorjeta com base na conta e na porcentagem
def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    # Validação: o valor da conta não pode ser negativo
    if valor_conta < 0:
        raise ValueError("O valor da conta não pode ser negativo.")
    # Validação: a porcentagem não pode ser negativa
    if porcentagem_gorjeta < 0:
        raise ValueError("A porcentagem da gorjeta não pode ser negativa.")
    
    # Converto a porcentagem informada (ex: 10) para taxa decimal (0.10)
    taxa = porcentagem_gorjeta / 100
    
    # Calculo a gorjeta multiplicando o valor da conta pela taxa
    gorjeta = valor_conta * taxa
    
    # Retorno apenas o valor da gorjeta calculada
    return gorjeta


# Programa interativo que conversa com o usuário no terminal
def programa_gorjeta_interativo():
    # Uso try/except para capturar erros de conversão e validação
    try:
        # Leitura do valor da conta como texto
        # .strip() tira espaços extras; .replace(',', '.') permite usar vírgula como separador decimal
        conta_str = input("Digite o valor total da conta (ex: 120,50): ").strip().replace(',', '.')
        
        # Leitura da porcentagem da gorjeta como texto (também aceito vírgula)
        gorjeta_str = input("Digite a porcentagem da gorjeta (ex: 10 para 10%): ").strip().replace(',', '.')
        
        # Conversão das strings para float (números reais)
        valor_conta = float(conta_str)
        porcentagem = float(gorjeta_str)

        # Chamo a função para calcular o valor da gorjeta
        valor_gorjeta = calcular_gorjeta(valor_conta, porcentagem)
        
        # Calculo o total a pagar somando a conta e a gorjeta
        total_com_gorjeta = valor_conta + valor_gorjeta

        # Exibição dos resultados formatados com 2 casas decimais
        print("\n--- Resultado ---")
        print(f"Valor da conta: R$ {valor_conta:.2f}")
        print(f"Gorjeta ({porcentagem:.2f}%): R$ {valor_gorjeta:.2f}")
        print(f"Total a pagar: R$ {total_com_gorjeta:.2f}\n")

    except ValueError as e:
        # Caso o usuário digite algo inválido (ex: letras no lugar de números ou valores negativos),
        # mostro uma mensagem amigável explicando o erro
        print(f"Erro: {e}")


# Ponto de entrada opcional do script:
# Se você rodar este arquivo diretamente (python nome_do_arquivo.py), essa parte executa o programa.
if __name__ == "__main__":
    # Chamo a função interativa para iniciar o processo de perguntas e respostas no terminal
    programa_gorjeta_interativo()