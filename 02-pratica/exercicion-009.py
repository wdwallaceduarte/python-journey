# Faça um programa que leia um número inteiro qualuer e mostre na telua a sua tabuada.

print('='*30)
print('|        TABUADA             |')
print('='*30)

num1 = int(input('Digite um número: '))
# num2 = int(input('Digite outro número: '))
op = input('Agora digite o operador: ')

print('-='*30)

for i in range(11):
    if op == '+':
        print(f'{num1} {op} {i} = {i + num1}')
    elif op == '-':
        print(f'{num1} {op} {i} = {i - num1}')
    elif op == '*':
        print(f'{num1} {op} {i} = {i * num1}')
    elif op == '/':
        print(f'{num1} {op} {i} = {i / num1}')
    
