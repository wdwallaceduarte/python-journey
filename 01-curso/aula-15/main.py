
# print('      ='*30)
print('             LISTA DE COMPRAS')
# print('='*30)

lista_compras = []
opcao = 0
# Menu de navegação (RF03)
while opcao != 3:
    print("""
    ================================
    ***********  MENU **************
    ================================ 
    1 -> Adicionar item
    2 -> Ver lista
    3 -> Sair
    """)
    print('=-'*15)
    opcao = int(input('> Digite uma opção: ')) 
    if opcao == 1:          # Adicionar Item (RF01)
        print('=-'*15)
        lista_compras.append(input('Nome Add Item: ')) 
    elif opcao == 2:        # Visualizar lista (RF02)
        print('=-'*15)
        if len(lista_compras) == 0:
            print('\33[32mSua lista está vazia!\33[0m')
        else:
            print('=-'*30)
            print(f'Sua lista contem os seguintes itens:\n \33[32m{lista_compras}\33[0m')
            print('=-'*30)
    else:                   # Encerrar programa (RF04)
        print('=-'*15)
        print('\33[32mPrograma encerrado!\n\33[32m')
