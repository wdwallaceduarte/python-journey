# Faça um programa que receba do usúario um arquivo texto e mostre na tela quantas letras são vogais.
import os
# from modulos.utilidades import cabecalho


def criarArquivo():
    try:
        if os.path.exists("arquivo_usuario.txt"):
            print("\nAviso - O arquivo já existe!")
        else:
            with open("arquivo_usuario.txt", "w", encoding="utf-8") as arquivo:
                pass
            print("\nSucesso - Arquivo criado!")

    except OSError as e:
        print(f"\nErro ao criar o arquivo: {e}")


def escrevaNoArquivo():
    frase = input("\nDigite uma frase ou palavra:\n> ")

    try:
        with open("arquivo_usuario.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(frase + "\n")

        print(f"[Sucesso] '{frase}' foi adicionada ao arquivo!")

    except OSError as e:
        print(f"Erro ao escrever no arquivo: {e}")


def contar_vogais(texto):
    vogais = "aeiou"
    contador = 0

    for letra in texto.lower():
        if letra in vogais:
            contador += 1

    return contador


def lerArquivo():
    try:
        with open("arquivo_usuario.txt", "r", encoding="utf-8") as arquivo:
            texto = arquivo.read()

        total = contar_vogais(texto)
        print(f"\nO arquivo tem {total} vogais.")

    except FileNotFoundError:
        print("\nO arquivo ainda não existe. Crie-o primeiro!")

    except OSError as e:
        print(f"\nErro ao ler o arquivo: {e}")


# cabecalho()
while True:
    print("""
    1. Criar um arquivo
    2. Escrever no arquivo
    3. Contar as vogais do arquivo
    4. Sair
    """)

    opcao = input("Escolha sua opção: ")

    if opcao == "1":
        criarArquivo()
    elif opcao == "2":
        escrevaNoArquivo()
    elif opcao == "3":
        lerArquivo()
    elif opcao == "4":
        print("Programa encerrado!")
        break
    else:
        print("Opção inválida! Tente novamente.")
