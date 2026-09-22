""" 
fruit = 'Casimiroa'
color = 'green'

print(f'The {fruit} is {color}.') 

# Apresentação
nome = input('Qual seu nome? ')
idade = input('Qual sua idade? ')
cidade = input('Qual sua cidade? ')

print('')
print(f'> Olá meu nome é {nome}, tenho {idade} e moro em {cidade}') 

# Calculadora de Idade
ano_nascimento = int(input('Qual seu ano de nascimento? '))
ano_atual = int(input('Qual ano atual? '))

idade = ano_atual - ano_nascimento

print('')
print(f'> Voçê tem {idade} anos.') 

# 3. Área do Retângulo
largura = int(input('Digite a largura do retângulo: ')) 
altura = int(input('Digite a altura do retângulo: '))

area = largura * altura 

print('')
print(f'A area do retângulo é {area}')

"""
# 4. Conversor de Minutos
entrada = int(input('Quantos minutos? '))
min = 60

hora = entrada // min
minuto = entrada % min

print('')
print(f'> {hora}h e {minuto}m')


