# 4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.

def classificar_numeros():
    print("=== Classificador de Números: Par ou Ímpar ===")
    print("Digite números (um por linha). Pressione ENTER em branco para finalizar.")

    # Contadores para pares e ímpares.
    pares = 0
    impares = 0
    # Lista para guardar todos os números digitados (opcional, apenas para exibir ao final).
    numeros = []

    while True:
        # Ler a entrada do usuário e removemos espaços nas extremidades.
        entrada = input("Número: ").strip()

        # ENTER vazio sinaliza o fim da entrada.
        if entrada == "":
            break

        try:
            # Convertendo a entrada para inteiro.
            n = int(entrada)
            # Guarda na lista para exibir depois.
            numeros.append(n)

            # Regra: números divisíveis por 2 são pares; caso contrário, ímpares.
            if n % 2 == 0:
                pares += 1
            else:
                impares += 1
        except ValueError:
            # Se não for possível converter para int, avisamos e seguimos.
            print("Entrada inválida. Digite um número inteiro ou ENTER para sair.")

    # Caso nenhum número tenha sido informado.
    if not numeros:
        print("Nenhum número informado.")
        return

    # Exibir o resultado consolidado.
    print("\n--- Resultado ---")
    print(f"Números inseridos: {numeros}")
    print(f"Quantidade de pares: {pares}")
    print(f"Quantidade de ímpares: {impares}")

if __name__ == "__main__":
    classificar_numeros()