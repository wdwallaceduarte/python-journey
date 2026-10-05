
# print('      ='*30)
print('             LISTA DE COMPRAS')
# print('='*30)

lista_compras = []
opcao = 0
# Menu de navegação (RF03)
while opcao != 5:
    print("""
    ================================
    ***********  MENU **************
    ================================ 
    1 -> Adicionar item
    2 -> Vesualizar lista
    3 -> Editar item
    4 -> Remover item
    5 -> Sair
    """)
    print('=-'*15)
    opcao = int(input('> Digite uma opção: '))
    if opcao == 1:          # Adicionar Item (RF01)
        print('=-'*15)
        item = input('Nome Add Item: ')
        lista_compras.append(item)
        print(f'Item {item} adicionando.')
    elif opcao == 2:        # Visualizar lista (RF02)
        print('=-'*15)
        if len(lista_compras) == 0:
            print('\33[32mSua lista está vazia!\33[0m')
        else:
            print('=-'*30)
            print('')
            print(f'Sua lista contém os seguintes itens:\n')
            for i in range(len(lista_compras)):
                print(f'\33[32m{i + 1}. {lista_compras[i]}\33[0m')
            print('=-'*30)
    elif opcao == 3:
        print(f'Sua lista contem os seguintes itens:\n')
        for i in range(len(lista_compras)):
            print(f'\33[32m{i + 1}. {lista_compras}\33[0m')
        indice = int(input('Digite o número do item que desa editar: ')) - 1
        if 0 <= indice < len(lista_compras):
            novo_item = input('Digite o novo valor para o item: ')
            lista_compras[indice] = novo_item
            print(f'Item {lista_compras[indice]} editado com sucesso.')
        else:
            print('Opção invalida!')
    elif opcao == 4:
        print(f'Sua lista contem os seguintes itens:\n')
        for i in range(len(lista_compras)):
            print(f'\33[32m{i + 1}. {lista_compras}\33[0m')
        indice = int(input('Digite o número do item que desa remover: ')) -1
        if 0 <= indice < len(lista_compras):
            item_removido = lista_compras.pop(indice)
            print(f'Item {item_removido} removido da lista.')
    elif opcao == 5:
        print('\33[32mSaindo...\n\33[32m')
        break
    else:                   # Encerrar programa (RF04)
        print('=-'*15)
        print('Opção inválida, escolha uma opção válida.')
else:
        print('\33[32mPrograma encerrado!\n\33[32m')

