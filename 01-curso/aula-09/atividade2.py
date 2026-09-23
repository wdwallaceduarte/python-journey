import random

print('=' * 30)
print('       JOGO DE ADIVINHAÇÃO')
print('=' * 30)

numero = random.randint(1, 10)
tentativa = 1
limite = 3

while tentativa <= limite:
    palpite = int(input('Digite seu palpite: '))

    if palpite == numero:
        print(f"""
        Você acertou! 🎆🎉🎊
        O número é {numero}
        Você acertou em {tentativa} tentativa(s)!
        """)
        break

    elif palpite < numero:
        print('Seu palpite foi MENOR, tente novamente.')

    else:
        print('Seu palpite foi MAIOR, tente novamente.')

    tentativa += 1

if palpite != numero:
    print(f'\nVocê excedeu o limite de {limite} tentativas!')
    print(f'O número era {numero}.')
