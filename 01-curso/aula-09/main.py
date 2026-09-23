# contatdor = 100

# while contatdor >= 0:
#     print(contatdor)
#     contatdor -= 1
# print('Fim da contagem!')

print('='*30)
print('       CALCULADORA')
print('='*30)

opcao = 0

while opcao != 'sair':
    opcao = input(""" 
        Digite uma opção:
            1 - Soma
            2 - Subtração
            3 - Divisão
            4 - Multiplicação 
            5 - Sair\n
        > Opção: """)

    if opcao == '1':
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        result = n1 + n2
        print('='*30)
        print(f'>> Resultado = {result}')
    elif opcao == '2':
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        result = n1 - n2
        print('='*30)
        print(f'>> Resultado = {result}')
    elif opcao == '3':
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        result = n1 * n2
        print('='*30)
        print(f'>> Resultado = {result}')
    elif opcao == '4':
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        result = n1 / n2
        print('='*30)
        print(f'>> Resultado = {result}')
    elif opcao == '5':
        print('='*30)
        print('>>> Programa finalizado.')
        break
    else:
        print('='*30)
        print('>>> Opção Inválida!')
