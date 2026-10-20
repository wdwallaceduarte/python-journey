# Você foi contratado po rum plataforma de streaming de música para gerar um relatório automatizado sobre os habitos de escuta dos usuários. A plataforma fornece um arquivo chamado 'historico_escuta.json'
# Sua missão: Escrever um program em python que faça o seguinte:
# 1. Leia o arquivo 'historico_escuta.json'
# 2. Calcule o tempo total que a usuária "Ana"  passou ouvindo musica (em minutos)
# 3. Crie um novo dicionario contendo apenas o nome da usuaria e o tempo total em minutos.
# 4. Salve esse resultado em um novo arquivo chamado 'realatorio_ana.json'

import json


def lerArquivo():
    try:
        with open('musicas.json', 'r') as arquivo:
            conteudo = json.load(arquivo)
            print(conteudo)
    except Exception as erro:
        print(f'\n Erro ao ler o arquivo: {erro}')


def calcularTempo():
    try:
        with open('musicas.json', 'r') as arquivo:
            conteudo = json.load(arquivo)
            tempo = 0
            for registro in conteudo:
                if registro['usuario'] == 'Ana':
                    tempo_seg = registro['duracao_segundos']
                    tempo += tempo_seg
            tempo_minutos = tempo / 60
            resultado['usuario'] = registro['usuario']
            resultado['tempo_total_minutos'] = tempo_minutos
            print(f'Tempo total da Ana: {tempo_minutos} minutos')
            return tempo_minutos
    except Exception as erro:
        print(f'\n Erro ao ler o arquivo: {erro}')


def resultadoUsuario():
    try:
       with open('relatorio_ana.json', 'a', encoding='utf-8') as arquivo:
            json.dump(resultado, arquivo, ensure_ascii=False, indent=4)
            print('Relatório criado com sucesso!')
            print(resultado)        
    except FileNotFoundError:
        print('O arquivo historico_escuta.json não foi encontrado.')

# ======== Codigo Principal =========
       
resultado = {
    
}

print('\n \33[30m Ler o arquivo\33[0m ')
lerArquivo()

print('\n \33[30m Calcula o tempo em minutos\33[0m')
calcularTempo()

print('\n \33[30m Mostra o resultado do usuário\33[0m')
resultadoUsuario()
