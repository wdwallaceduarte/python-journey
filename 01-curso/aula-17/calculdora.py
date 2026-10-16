from modulos.interface import cabecalho

cabecalho('CALCULADORA')
# print('='*30)
# print('\33[1;30;42m         CALCULADORA          \33[0m')
# print('='*30)
print()

def calcular(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        # if num2 == 0:
        #     print('Impos. dividir por 0')
        return num1 / num2
    
num1 = int(input())
op = input()
num2 = int(input())

resultado = calcular(num1, num2, op)

print(f'{num1} {op} {num2} = {resultado}')