def cabeca(msg):
    print('\33[32m=\33[0m' * 30)
    print('\33[32m{:^30}\33[0m'.format(msg))
    print('\33[32m=\33[0m' * 30)

def cabecalho(*msg):
    texto = ' '.join(msg)
    print('\33[32m=\33[0m' * 30)
    print(f'{texto:^30}')
    print('\33[32m=\33[0m' * 30)

cabeca('Wallace')


cabecalho('Olá', 'Python')