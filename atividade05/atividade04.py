# 4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.

# Exercício 4 — Calculadora de Dias de Vida (interativa)
# Regra: Enter vazio encerra o programa.

from datetime import datetime, date

def calcular_dias_de_vida(data_nascimento_str: str) -> int:
    """
    Recebe a data de nascimento como string no formato DD/MM/AAAA
    e retorna a quantidade de dias vividos até hoje.
    """
    nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y").date()
    hoje = date.today()
    if nascimento > hoje:
        raise ValueError("A data de nascimento não pode ser no futuro.")
    return (hoje - nascimento).days

def programa_dias_de_vida_interativo():
    print("Calculadora de Dias de Vida — pressione Enter vazio para sair.\n")
    while True:
        data_str = input("Digite sua data de nascimento (DD/MM/AAAA): ").strip()
        if data_str == "":
            print("Encerrando...")
            break
        try:
            dias = calcular_dias_de_vida(data_str)
            print(f"Você está vivo há {dias} dias.\n")
        except ValueError:
            print("Erro: data inválida. Use o formato DD/MM/AAAA (ex: 25/12/2000) e não use data futura.\n")

if __name__ == "__main__":
    programa_dias_de_vida_interativo()