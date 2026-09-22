""" 
# 1. Média do aluno
print('='*30)
print('     MÉDIA DO ALUNO')
print('='*30)

nota1 = float(input(' Digite a primeira nota: '))
nota2 = float(input(' Digite a segunda nota: '))
nota3 = float(input(' Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print('='*30)
    print(f" 
        Média: {media}
        Situação: Aprovado
    ")
elif media > 5 and media < 7:
    print('='*30)
    print(f" 
        Média: {media}
        Situação: Recupreção
    ")
else:
    print('='*30)
    print(f" 
        Média: {media}
        Situação: Reprovado
    ")
    
#2. Maior entre três npumeros
print('='*30)
print('     MAIOR ENTRE TRÊS NPUMEROS')
print('='*30)

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

if n1 > n2 and n1 > n3:
    print('='*30)
    print(f'O maior número é {n1}')
elif n2 > n1 and n2 > n3:
    print('='*30)
    print(f'O maior númeor é {n2}')
elif n3 > n1 and n3 > n2:
    print('='*30)
    print(f'O maior número é {n3}')


# 3. Calculadora com operação
print('='*30)
print('     Calculadora com operação')
print('='*30)

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
operador = input('Esolha o operador: ')

if operador == '+':
    print('='*30)
    print(f' 
        Primeiro número: {n1}
        Segundo número: {n2}
        Operador: {operador}

        Resultado: {n1 + n2}
     ')
elif operador == '-':
    print('='*30)
    print(f' 
        Primeiro número: {n1}
        Segundo número: {n2}
        Operador: {operador}

        Resultado: {n1 - n2}
     ')
elif operador == '*':
    print('='*30)
    print(f' 
        Primeiro número: {n1}
        Segundo número: {n2}
        Operador: {operador}

        Resultado: {n1 * n2}
     ')
elif operador == '/':
    print('='*30)
    print(f' 
        Primeiro número: {n1}
        Segundo número: {n2}
        Operador: {operador}

        Resultado: {n1 / n2}
     ')
elif operador == '%':
    print('='*30)
    print(f' 
        Primeiro número: {n1}
        Segundo número: {n2}
        Operador: {operador}

        Resultado: {n1 % n2}
     ')
else:
    print('='*30)
    print('Opração inválida.')


# 4. Classificação de idade
print('='*30)
print('     CLASSIFICAÇÃO DE IDADE')
print('='*30)

idade = int(input('Digite sua idade: '))

if idade <= 12:
    print('> Criança')
elif idade <= 17:
    print('> Adolecente')
elif idade <= 59:
    print('> Adulto')
else:
    print('> Idoso')


# 5. Desconto da loja
print('='*30)
print('     DESCONTO NA LOJA')
print('='*30)

compra = float(input("Valor da compra: R$ "))

if compra <= 100:
    desconto = 0
    print('='*30)
    print(f' 
        Compra: R$: {compra}
        Desconto: 0%
        Valor do desconto: R$ {desconto}
        Total: R$ {compra}   
     ')
elif compra <= 500:
    desconto = compra * 0.10 
    print('='*30)
    print(f' 
        Compra: R$: {compra}
        Desconto: 10%
        Valor do desconto: R$ {desconto}
        Total: R$ {compra - desconto}   
     ')
elif compra <= 1000:
    desconto = compra * 0.15 
    print('='*30)
    print(f' 
        Compra: R$: {compra}
        Desconto: 15%
        Valor do desconto: R$ {desconto}
        Total: R$ {compra - desconto}   
     ')
else:
    desconto = compra * 0.20 
    print('='*30)
    print(f' 
        Compra: R$: {compra}
        Desconto: 20%
        Valor do desconto: R$ {desconto}
        Total: R$ {compra - desconto}   
     ')


# 6. Login 
print('='*30)
print('        LOGIN')
print('='*30)

usuario_cadastrado = 'wallace'
senha_cadastrada = 8888

login = input('Usuário: ')
senha = int(input('Digite sua senha: '))

if login == usuario_cadastrado and senha == senha_cadastrada:
    print('='*30)
    print(f'> Olá, {login}!')
else:
    print('='*30)
    print('Usuário ou senha incorretos.')


# 7. Pode participar da competilção?
print('='*30)
print('   PODE PARTICIPAR DA COMPETIÇÃO?')
print('='*30)

idade = int(input('Idade: '))
inscrito = input('Está escrito? (sim/não) ')

if idade >= 16 and inscrito == 'sim':
    print('='*30)
    print('> Você pode participar!')
else:
    print('='*30)
    print('> Você não pode participar!')

# 8. Pode viajar?
print('='*30)
print('     PODE VIAJAR?')
print('='*30)

doc = input('Documento válido? (sim/não) ')
passagem = input('Possui passagem? (sim/não) ')

if doc == 'sim' and passagem == 'sim':
    print('='*30)
    print('> Você pode viajar!')
else:
    print('='*30)
    print('> Você não pode viajar.')

# 9. Número dentro do intervalo 
print('='*30)
print('   NÚMERO DENTRO DO INTERVALO')
print('='*30)

n1 = int(input('Digite um número: '))

if n1 > 9 and n1 < 51:
    print('='*30)
    print('> O número está dentro do intervalo.')
"""

# 10. Sistema de notas
print('='*30)
print('     Sistema de notas')
print('='*30)

nome = input('Nome do aluno(a): ')
nota1 = int(input('Primeira nota: '))
nota2 = int(input('Segunda nota: '))
nota3 = int(input('Terceira nota: '))
frequencia = int(input('Fequência (%): '))

media = (nota1 + nota2 + nota3) / 3

if media < 7:
    print('='*30)
    print(f""" 
        Aluno: {nome}
        Média: {media}
        Frequência: {frequencia}%

        Resultado: Reprovado por nota.
    """)
elif frequencia < 75:
    print('='*30)
    print(f""" 
        Aluno: {nome}
        Média: {media}
        Frequência: {frequencia}%

        Resultado: Reprovado por frequência.
     """)
else:
    print('='*30)
    print('Resultado: Aprovado!')


