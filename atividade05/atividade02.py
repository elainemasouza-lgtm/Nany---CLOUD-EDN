# 2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”

# Exercício 2 — Verificador de Palíndromos (interativo e funcional)
# Regra: Enter vazio encerra o programa.

import unicodedata
import re

def remover_acentos(s: str) -> str:
    # Remove acentos deixando apenas o caractere base
    nfkd = unicodedata.normalize('NFKD', s)
    return ''.join(c for c in nfkd if unicodedata.category(c) != 'Mn')

def normalizar_texto(texto: str) -> str:
    # 1) Minúsculas
    texto = texto.lower()
    # 2) Remove acentos
    texto = remover_acentos(texto)
    # 3) Mantém só letras e números (remove espaços e pontuação)
    texto = re.sub(r'[^a-z0-9]', '', texto)
    return texto

def eh_palindromo(texto: str) -> bool:
    t = normalizar_texto(texto)
    return t == t[::-1]

def programa_palindromo_interativo():
    print("Verificador de Palíndromos — Digite a frase ou palavra --- ou --- pressione Enter vazio para sair.")
    while True:
        frase = input("Digite uma palavra ou frase: ").strip()
        if frase == "":
            print("Encerrando...")
            break
        print("Sim" if eh_palindromo(frase) else "Não")

if __name__ == "__main__":
    programa_palindromo_interativo()