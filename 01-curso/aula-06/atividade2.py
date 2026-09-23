print('='*30)
print('     POSSO DIRIGIR?')
print('='*30)

carteira = input('Possui CNH?\n s - Sim\n n - Não\n >  ')
idade = int(input('Qual sua idade? '))

if idade >= 18 and carteira in 'sS':
    print('='*30)
    print('Você pode dirigir.')
    print('='*30)

    print('↓'*30, "\n")
else:
    print('='*30)
    print('Você não pode dirigir ainda.')
    print('='*30)
    print('↓'*30, "\n")

#==========================================================

print('='*30)
print('     POSSO VOTAR?')
print('='*30)

titulo = input('Possui titulo de eleitor? (s) - Sim | (n) - Não\n >   ')
idade = int(input('Qual sua idade?\n> '))

if  idade < 16:
    print('='*30)
    print('Você não pode votar.')
    print('='*30,"\n")
    print('↓'*30,"\n")
elif titulo in 'ss' and idade < 18:
    print('='*30)
    print('Voto facutativo.')
    print('='*30,"\n")
    print('↓'*30,"\n")
else:
    print('='*30)
    print('Voto obrigatorio.')
    print('='*30)
    print("\n"'↓'*30,"\n")

#==========================================================

print('='*30)
print('     DESCONTO 10%')
print('='*30)

valor = float(input('Valor da compra: '))
cliente = input('Cadastro VIP?\n 1 - Sim\n 2 - Não\n > ')

if cliente == '1':
    cliente = 'Sim'
elif cliente == '2':
    cliente = 'Não'
else:
    print('Valor invalido.')

desconto = valor * 0.10
print('='*30)
if valor >= 100 or cliente == 'Sim':
    print(f""" 
        Valor da compra: {valor:.2f}
        Cliente VIP: {cliente}
        Desconto: 10%
        Total: {valor - desconto:.2f}
    """)
else:
    print(f""" 
        Valor da compra: {valor:.2f}
        Cliente VIP: {cliente}
        Desconto: -
        Total: {valor:.2f}
    """)
