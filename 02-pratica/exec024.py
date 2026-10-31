# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a plalabra "SANTO" 

print('\33[36m=-\33[0m'*30)
print('Digite: \33[30msair\33[0m para encerrar este programa.\n')

cidade = ''
while cidade != 'sair':
    print('Digite o nome da cidade:\n> ',end='')
    cidade = input('\33[36m \33[0m')

    if 'santo' in cidade:
        print("A cidade informada \33[32mCONTÉM\33[0m o nome \33[32mSanto\33[0m.")
    else:
        print('A cidade informada \33[31mNÃO\33[0m contém a palavra \33[32mSanto\33[0m.')
else:
    print('\n\33[31m> Programa encerrado! \33[0m\n')