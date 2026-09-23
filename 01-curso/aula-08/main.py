""" for condicao:   
    #bloco de codigo

while condicao:
    # bloco de codigo


rico = 'nao'
while not rico == 'sim':
    print('Trabalhe')
    rico = input('Estou rico? ') """

print('='*30)
print('       TELA DE LOGIN ')
print('='*30)

login = input('Usuário: ')
senha = input('Senha: ')
tentativa = 1

while  not (login == 'duarte' and senha == '8888'):
    print('> Usuário ou senha invalida! Digite novamente.')
    print(tentativa)
    login = input('Usuário: ')
    senha = input('Senha: ')
    tentativa += 1

    if tentativa == 3:
        break
    print('Tentativa excedida')
print('Bem vindo!')



