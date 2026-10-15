# Faça um programa que receba do usuario um arquivo texto e um caracter. Mostre na tela quantas vezes aquele caractere ocorre dentro do arquivo.

try:
    nome_arquivo = input("Digite o nome do arquivo: ")
    caractere = input("Digite o caractere que deseja contar: ")

    contador = 0

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()

    for letra in texto:
        if letra == caractere:
            contador += 1

    print(f"O caractere '{caractere}' aparece {contador} vezes no arquivo.")

except FileNotFoundError:
    print("Erro: arquivo não encontrado!")

except OSError:
    print("Erro ao ler o arquivo!") 

 
 