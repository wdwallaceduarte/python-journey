# Uma parte do poder do print()

nome = 'Wallace'
print('\33[32m=-\33[0m'*30)

# ':20' escreve a variavel dentro de {} na quantidade de esapaços desejada, no caso 20 espaços
print('\n=> Olá {:20}!'.format(nome))
# ':>20' o sinal de > faz alinhamento a diretita em 20 espacos
print('\n> Olá {:>20}!'.format(nome))
# ':<20' o sinal de < faz alinhamento a esqueda em 20 espacos
print('\n> Olá {:<20}!'.format(nome))
# ':^20' o sinal de ^ faz alinhamento ao centro em 20 espacos
print('\n> Olá {:^20}!'.format(nome))
# ':=^20' o sinal de =^ faz alinhamento ao centro em 20 espacos preenchido com =
print('\n> Olá {:=^20}!'.format(nome))
# ':*^20' o sinal de =^ faz alinhamento ao centro em 20 espacos preenchido com *
print('\n> Olá {:*^20}!'.format(nome))
# end='' no final do print, remove a quebra de linha entre dois prints
print('Olá, ', end='')
print(nome)
print('Olá, ', end='>>> ')
print(nome)