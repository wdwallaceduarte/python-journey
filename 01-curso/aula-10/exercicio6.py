# Somando apenas numeros pares: escreva um programa que utilize um loop for para calcular a soma de todos os númoros pares de 1 a 50:

soma = 0

for i in range(1, 51):
    if i % 2 == 0:
        soma += i
        print(soma)