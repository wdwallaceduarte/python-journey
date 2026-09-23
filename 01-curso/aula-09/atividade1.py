"""Escreva um programa que solicite ao usuário um número inteiro positivo e, em seguida, faça uma contagem regressiva desse número até zero."""

numero = int(input('Digite um nnúmero positivo: '))

while numero >= 0:
    print(f'Contagem refressiva: {numero}')
    numero -= 1