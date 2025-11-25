# Atividade Prática 07 - Questão 1
#
# Leia um arquivo de log, calcule a média e o desvio padrão do tempo de execução.
#
# -----------------------------------------------------------------

import statistics
import io # Módulo para tratar uma string como um arquivo

# Exemplo resolvido:
# Simulando o conteúdo de um arquivo de log em uma string
log_data = """
Início do treinamento - Tempo de execução: 125.34s
Etapa 1 concluída - Tempo de execução: 130.56s
Etapa 2 concluída - Tempo de execução: 128.91s
Finalizando... - Tempo de execução: 132.11s
"""

# Usa 'io.StringIO' para ler a string como se fosse um arquivo
log_file = io.StringIO(log_data)
tempos = []

for linha in log_file:
    # Verifica se a linha contém "Tempo de execução"
    if "Tempo de execução" in linha:
        # Pega a parte da linha após "Tempo de execução: "
        parte = linha.split("Tempo de execução: ")[1]
        # Remove o "s" e converte para número
        tempo = float(parte.strip().replace('s', ''))
        tempos.append(tempo)

if tempos:
    media = statistics.mean(tempos)
    desvio_padrao = statistics.stdev(tempos)
    
    print("Exemplo resolvido:")
    print(f"Tempos de execução encontrados: {tempos}")
    print(f"Média: {media:.2f} segundos")
    print(f"Desvio Padrão: {desvio_padrao:.2f} segundos")
else:
    print("Nenhum tempo de execução encontrado no log.")