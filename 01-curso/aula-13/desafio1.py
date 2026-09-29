# Crie uma lista de números inteiros e implemente um codigo que substitua todos os numeros pares por 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        numeros[i] = "0"
print(numeros)