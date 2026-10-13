# Uma parte do poder do print()

print('='*30)
print('\t Print()')
print('='*30)

nome = input('\nQual seu nome?\n\n> ') 
print('\33[32m=-\33[0m'*30)

# ':20' escreve a variavel dentro de {} na quantidade de esapaços desejada, no caso 20 espaços
print('\n 1 - Olá {:20}!'.format(nome))

# ':>20' o sinal de > faz alinhamento a diretita em 20 espacos
print('\n 2 - Olá {:>20}!'.format(nome))

# ':<20' o sinal de < faz alinhamento a esqueda em 20 espacos
print('\n 3 - Olá {:<20}!'.format(nome))

# ':^20' o sinal de ^ faz alinhamento ao centro em 20 espacos
print('\n 4 - Olá {:^20}!'.format(nome))

# ':=^20' o sinal de =^ faz alinhamento ao centro em 20 espacos preenchido com =
print('\n 5 - Olá {:=^20}!'.format(nome))

# ':*^20' o sinal de =^ faz alinhamento ao centro em 20 espacos preenchido com *
print(f'\n 6 - Olá {nome:*^20}!')

# '\t' é o mesmo que usar to Tab do teclado para dar espaço 
print(f'\n 7 - Olá,\t {nome}!')

# end='' no final do print, remove a quebra de linha entre dois prints
print('\n 8 - Olá, ', end='')
print(nome)
print('\n 9 - Olá, ', end='>>> ')
print(nome)

