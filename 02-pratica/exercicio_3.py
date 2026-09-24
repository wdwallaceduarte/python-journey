""" 
# Exemplo de como usar a biblioteca rich para uma saida mais apresentaval no console
from rich.console import Console
from rich.table import Table

console = Console()

# Criando uma tabela profissional
table = Table(title="Relatório de Vendas - 2026")

table.add_column("Produto", justify="left", style="cyan", no_wrap=True)
table.add_column("Quantidade", justify="right", style="magenta")
table.add_column("Lucro Total", justify="right", style="green")

table.add_row("Console de Videogame", "42", "$16,800")
table.add_row("Teclado Mecânico", "120", "$9,600")
table.add_row("Mouse Gamer", "85", "$4,250")

# Renderizando na tela
console.print(table)
#=============================================================================================
# As variáveis a e b estão com valores ausentes; preencha-as para que o código dentro da instrução if seja executado! (certifique-se de que a condição do if seja verdadeira)

# Ao final do programa, o valor de c deve ser 3.

# Bônus: tente encontrar mais de uma solução!

a = 20
b = 14

c= 0
if a >= b and not b < 10:
    c = 2

c += 1
print(f'c = {c}')
# 1 Apresentação
nome = 'Wallace'
idade = 38
cidade = 'Fortaleza'

print()
print(f'> Olá, meu nome é {nome}, tenho {idade} de idade e moro em {cidade}')

# 2. Calculadora de soma
print('='*50)
print('Calculadora')
print('='*50)

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

print('='*50)
print(f' 
    Soma: {n1+n2}
    Subitração: {n1-n2}
    Multiplicação: {n1*n2}
    Divisão: {n1/n2}
' )

# 3. Antecessor e sucessor
print('='*30)
print('     ANTECESSOR E SUCESSOR')
print('='*30)

numero = int(input('>> Digite um número: '))

print(f" 
    > Número: {numero}
    > Antecessor: {numero - 1}
    > Sucessor: { numero + 1}
 ")
print('='*30)

# 4. Resto da divisão
print('='*30)
print('     RESTO DA DIVISÃO')
print('='*30)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

resto = n1 % n2

print('='*30)
print(f'Resto: {resto} ')
print('='*30)

# 5. Maior de dois números
print('='*30)
print('     MAIOR DE DOIS NÚMEROS')
print('='*30)

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print('='*30)
    print(f'{n1} é maior que {n2}')
elif n2 > n1:
    print('='*30)
    print(f'{n2} é maior que {n1}')
else:
    print('='*30)
    print('Os números são iguais.')


# 6 Positivo ou negativo
print('='*30)
print('     POSITIVO OU NEGATIVO')
print('='*30)

n1 = int(input("> Digite um número: "))

if n1 < 0:
    print('='*30)
    print('>> O número é negativo')
else:
    print('='*30)
    print('>> O número é positivo')


# 7. Pode Dirigir?
print('='*30)
print('     PODE DIRIGIR?')
print('='*30)

idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('='*30)
    print('>> Você pode dirigir.')
else:
    print('='*30)
    print('> Você ainda não pode dirigir.')


# 8. Par ou ímpar
print('='*30)
print('     NÚMERO PAR OU ÍMPAR')
print('='*30)

n = int(input('Digite um número: '))
n %= 2
if n == 0:
    print('='*30)
    print(f'> O número é PAR.')
else:
    print('='*30)
    print(f'> O número é IMPAR.')
  

# 9. Senha simples
print('='*30)
print('     SENHA SIMPLES')
print('='*30)

senha = 8888
use_senha = int(input('Insira sua senha: '))

if use_senha == 8888:
    print('='*30)
    print('> Acesso permitido!')
else:
    print('='*30)
    print('Senha incorreta!')

"""  
# 10. Temperatura
# print('='*30)
# print('     TEMPERATURA')
# print('='*30)

# temperatura = int(input('Digite a temperatura: '))

# if temperatura < 15:
#     print('='*30)
#     print('> Está frio!')
# elif temperatura >=15 and temperatura < 25:
#     print('='*30)
#     print('> Temperatura agradável.')
# else:
#     print('='*30)
#     print('> Está quente!')


