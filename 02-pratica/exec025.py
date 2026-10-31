# Crie um program que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

print('\33[36m=-\33[0m'*30)
print('Digite: \33[30msair\33[0m para encerrar este programa.\n')

nome = ''
while nome != 'sair':
    print('Digite seu nome:\n> ',end='')
    nome = input('\33[36m \33[0m')

    if 'santo' in nome:
        print("Seu nome contém a palavra \33[32mSilva\33[0m.")
    else:
        print('Seu nome \33[31mNÃO\33[0m contém a palavra \33[32mSilva\33[0m.')
else:
    print('\n\33[31m> Programa encerrado! \33[0m\n')