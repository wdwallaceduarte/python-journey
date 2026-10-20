num = int(input('\nDigite um número inteiro: '))

print(""" 
        Escolha a base para conversão:
    [1] - converter para BINÁRIO
    [2] - converter para OCTAL
    [3] - converter para HEXADECIMAL
""")

opcao = input('Sua opção: ')

if opcao == '1':
    print(f'\n{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opcao == '2':
    print(f'\n{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opcao == '3':
    print(f'\n{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('\nOpção inválida!')