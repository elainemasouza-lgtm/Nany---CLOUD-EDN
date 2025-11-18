# 1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/)

# Função para encapsular a lógica da calculadora.
def calculadora():
    # Mensagens informativas para o usuário.
    print("=== Calculadora Básica ===")
    print("Operações: +  -  *  /")
    try:
        # Lê o primeiro numero e converta para float (permite decimais).
        a = float(input("Digite o primeiro número: "))
        # Lê a operação e remove espaços extras com strip().
        op = input("Digite a operação (+, -, *, /): ").strip()
        # Lê o segundo número.
        b = float(input("Digite o segundo número: "))

        # Verificamos qual operação foi solicitada e calculamos calcula o resultado.
        if op == "+":
            resultado = a + b
        elif op == "-":
            resultado = a - b
        elif op == "*":
            resultado = a * b
        elif op == "/":
            # Tratamento especial para evitar divisão por zero.
            if b == 0:
                print("Erro: divisão por zero não é permitida.")
                return  # Encerra a função cedo.
            resultado = a / b
        else:
            # Se o operador não for reconhecido, informamos erro.
            print("Operação inválida.")
            return

        # Exibimos o resultado formatado.
        print(f"Resultado: {a} {op} {b} = {resultado}")
    except ValueError:
        # Caso a conversão para float falhe (ex.: usuário digitou letras), tratamos aqui.
        print("Entrada inválida. Certifique-se de digitar números válidos.")

# Este bloco garante que a função só roda automaticamente se o arquivo for executado diretamente.
if __name__ == "__main__":
    calculadora()