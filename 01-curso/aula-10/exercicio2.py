# Somando números de 1 a N escreva um programa que solicite ao usuário um número N e, em seguida, utilize um loop for para calcular a soma de todos os números de 1 a N

print('='*30)
print('     1 a10 N')
print('='*30)

n = int(input('Digite um número: '))
passo = int(input('Digite o passo da contagem: '))
soma = 0

for i in range(1, n+1, passo):
    print(i)
    soma += i
print(f'Soma: {soma}')