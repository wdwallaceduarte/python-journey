# Criar um dicionario de pessoas
import os
import json


def criarArquivoPessoa():
    try:
        if os.path.exists('arquivo_pessoas.json'):
            print('\n Arquivo já existe!')
        else:
            with open('arquivo_pessoas.json', 'w') as arquivo:
                json.dump(pessoas, arquivo, indent=4)
            print('\n Arquivo criado com sucesso!')
    except Exception as e:
        print(f'\n Erro ao contrar o arquivo: {e}')


def lerArquivoPessoa():
    try:
        with open('arquivo_pessoas.json', 'r') as arquivo:
            conteudo = json.load(arquivo)
            for pessoas, idade in conteudo.items():
                print(f'\n Pessoa: {pessoas}, Idade: {idade}')
    except Exception as e:
        print(f'\n Erro ao ler o arquivo: {e}')

def adicionarPessoa():
    pessoa = input('\n Digite o nome da pessoa a ser adcionada: ')
    idade = int(input(' Informe a idade: '))
    pessoas[pessoa] = idade
    arquivo = open('arquivo_pessoas.json', 'w', encoding='utf-8')
    json.dump(pessoas, arquivo)
    arquivo.close()
    print(f'{pessoa} foi adicionado.')
                
    

# Codigo Principal
pessoas = {}

if os.path.exists("arquivo_pessoas.json"):
    with open("arquivo_pessoas.json", "r") as arquivo:
        dicionario_pessoas = json.load(arquivo)

opcao = ""
while opcao != "0":
    print("""
              ======= MENU DO ARQUIVO =======
              1. Criar arquivo inicial
              2. Ler conteúdo do arquivo
              3. Adicionar pessoa
              0. Sair do programa
    """)
   
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        criarArquivoPessoa()
    elif opcao == "2":
        lerArquivoPessoa()
    elif opcao == "3":
        adicionarPessoa()
    elif opcao == "0":
        print("\nSaindo do sistema...")
    else:
        print("\nOpção Inválida - Escolha um número do menu.")
        