# 4 - Crie um programa que realize consultas a  em relação ao Real (BRL) usando a API mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.


import requests
import datetime

# --- Função Principal para Consultar a Moeda ---
def consultar_cotacao():
    """
    Função principal que interage com o usuário, consulta a API 
    e exibe os resultados da cotação da moeda.
    """
    # URL base da API AwesomeAPI. Usamos a versão mais recente e confiável.
    # O formato {moedas} será substituído pelo código da moeda desejada.
    url_base = "https://economia.awesomeapi.com.br/json/last/{moedas}-BRL"
    
    print("--- Consulta de Cotação de Moedas ---")
    
    # Loop para permitir múltiplas consultas
    while True:
        # Pede ao usuário para inserir o código da moeda (ex: USD, EUR, BTC)
        codigo_moeda = input("Digite o código da moeda (ex: USD, EUR, BTC) ou 'sair' para terminar: ").upper()

        # Condição para encerrar o programa
        if codigo_moeda == 'SAIR':
            print("Obrigado por usar o programa! Até mais.")
            break
            
        # Validação simples para garantir que o usuário digitou algo
        if not codigo_moeda:
            print("Por favor, digite um código de moeda válido.")
            continue

        try:
            # Formata a URL final substituindo '{moedas}' pelo código inserido pelo usuário
            url_final = url_base.format(moedas=codigo_moeda)
            
            # Faz a requisição GET para a API com um timeout de 5 segundos
            # O timeout evita que o programa fique travado indefinidamente.
            resposta = requests.get(url_final, timeout=5)
            
            # Verifica se a requisição foi bem-sucedida (código de status 200)
            resposta.raise_for_status() 
            
            # Converte a resposta JSON em um dicionário Python
            dados = resposta.json()
            
            # A API retorna os dados dentro de uma chave que é a combinação das moedas (ex: 'USDBRL')
            chave_api = f"{codigo_moeda}BRL"
            
            # Verifica se a chave esperada realmente existe nos dados retornados
            if chave_api in dados:
                cotacao_info = dados[chave_api]
                
                # Converte o timestamp (em segundos) para um objeto datetime
                timestamp = int(cotacao_info['timestamp'])
                data_hora_atualizacao = datetime.datetime.fromtimestamp(timestamp)
                
                # Exibe as informações formatadas para o usuário
                print("\n--- Resultado da Consulta ---")
                print(f"Moeda: {cotacao_info['name']}")
                print(f"Valor Atual (Bid): R$ {float(cotacao_info['bid']):.4f}")
                print(f"Máxima do Dia (High): R$ {float(cotacao_info['high']):.4f}")
                print(f"Mínima do Dia (Low): R$ {float(cotacao_info['low']):.4f}")
                print(f"Última Atualização: {data_hora_atualizacao.strftime('%d/%m/%Y às %H:%M:%S')}")
                print("-----------------------------\n")
                
            else:
                # Se a chave não for encontrada, significa que a moeda não existe na API
                print(f"\nERRO: A moeda '{codigo_moeda}' não foi encontrada. Verifique o código e tente novamente.\n")

        # Tratamento de erros de requisição (ex: falha de conexão, timeout)
        except requests.exceptions.RequestException as e:
            print(f"\nERRO: Falha na conexão com a API. Verifique sua internet. Detalhes: {e}\n")
            
        # Tratamento de erros de status HTTP (ex: erro 404 - Not Found)
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f"\nERRO: A moeda '{codigo_moeda}' não foi encontrada ou a combinação não é válida. Tente outra.\n")
            else:
                print(f"\nERRO: Ocorreu um problema com a requisição. Código: {e.response.status_code}\n")


# --- Início do Programa ---
if __name__ == "__main__":
    consultar_cotacao()