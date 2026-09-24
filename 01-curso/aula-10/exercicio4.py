# Escreva um programa que solicite ao usuário um número e , em seguida, utilize um loop for para calcular o fatorial desse número







def calcular_fatorial(n):
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

# Testando a função com o número 5
numero = int(input('Digite um número: 50'))
resultado = calcular_fatorial(numero)
print(f"O fatorial de {numero} é {resultado}.")
