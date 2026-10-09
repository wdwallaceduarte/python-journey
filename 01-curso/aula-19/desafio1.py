# Crie um dicionário de tradução que mapeie palavras de um idioma para outro (por explo, ingles para espanhol). Pela ao usuaio para inserir uma placabra em ingles e, em seguida imprima a tradução correspondente. Crie uma funçaõ no qual a pessoa pode colocar uma nova tradução.

tradutor = {
    'motorcycle': 'motocicleta',
    'dog': 'perro',
    'cat': 'gato',
    'hello': 'hola',
    'house': 'casa',
    'mouse': 'ratón',
    'computer': 'computadora'
}

while True:
    print()
    def adicionar_traducao():
        palavra = input('\33[32mDigite a palavra em inglês: \33[0m').lower()
        traducao = input('Digite a tradução em espanhol: ').lower()

        tradutor[palavra] = traducao
        print('Tradução adicionada com sucesso!')

    palavra = input('Digite uma palavra em inglês para traduzir para espanhol:\n> ').lower()

    if palavra in tradutor:
        print('Tradução:', tradutor[palavra])
    else:
        print('Palavra não encontrada no dicionário.')

        opcao = input('Deseja adicionar essa palavra? (s/n): ').lower()

        if opcao == 's':
            adicionar_traducao()

    print('-='*30)
    print(f'\nDicionário atualizado:\n ')
    
    for ingles, espanhol in tradutor.items():
        print(f'{ingles}: {espanhol}')