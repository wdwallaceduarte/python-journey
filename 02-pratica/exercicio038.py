# Escreva um program que leia dois números inteiros e compare-os, mostrando na tela a mensagem:
# - O primeiro valor é o maior
# - O segundo valor é o maior 
# - Os dois números são iguais 


num1 = int(input('\n Primeiro número: '))
num2 = int(input('\n Segundo número: '))

if num1 > num2:
    print('\nO primeiro número é o\33[32m MAIOR\33[0m')
elif num2 > num1:
    print('\nO segundo número é o\33[32m MAIOR\33[0m')
else:
    print('\nOs dois números são \33[32m IGUAIS\33[0m')