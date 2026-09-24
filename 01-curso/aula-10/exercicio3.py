# Escreva um programa que solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número de 1 a 10

print('='*30)
print('     TABUADA MULTIPLICAR')
print('='*30)

num = int(input('Digite um número: '))

for i in range(11):
    print(f'{i} x {num} = {i*num}')