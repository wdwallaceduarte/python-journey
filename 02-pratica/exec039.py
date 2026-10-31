# Faça um programa que leia o ano de nascimento de um jovem e informe
# de acorido com sua idade: 
#   1. se ele 'ainda vai se alisatar' ao serviço militar, 
#   2. se é a 'hora de se alistar'
#   3. ou se já 'passou do tempo' do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_atual = date.today().year
ano_nas = int(input('\n Ano de nascimento? '))
sexo = input('\n Qual o sexo (M/F): ')

if sexo == 'f':
    print('\nMulheres não são obrigadorio ao alistamento.')
elif sexo == 'm':
    idade = ano_atual - ano_nas
    print(f'\nQuem nasceu em {ano_nas} tem {idade} anos em {ano_atual}.')

    if idade == 18:
        print('Você tem que se alistar imediatamente!')
    elif idade < 18:
        saldo = 18 - idade
        print(f'Ainda faltam {saldo} anos para o alistamento.')
        ano = ano_atual + saldo
        print(f'Seu alistamento será em {ano}')
    elif idade > 18:
        atraso = idade - 18
        print(f'Você já deveria ter se alistado há {atraso} anos.')
        ano = ano_atual - atraso
        print(f'Seu alistamento foi em {ano}.')