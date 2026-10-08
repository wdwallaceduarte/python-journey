# Escreva uma função chamada contar_vogais que receba uma string e retone o número de vogais (a, e, i, o, u) na string.

def contar_vogais(texto):
    vogais = "aeiou"
    contador = 0

    for letra in texto.lower():
        if letra in vogais:
            contador += 1

    return contador

frase = input('Digite uma frase ou plavra:\n> ')

print(f"Sua frase tem {contar_vogais(frase)} vogais")
