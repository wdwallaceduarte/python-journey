# Escreva um programa que encontre todos os pares de números que multiplicados dão `n` usando números de 1 a `n` (inclusivo).
# O programa deve mostrar todas as combinações possíveis, incluindo pares duplicados em ordem reversa. Por exemplo, tanto "1 6" quanto "6 1" devem ser mostrados, pois são considerados arranjos diferentes do mesmo par. Números também podem ser pareados consigo mesmos se o produto deles for igual a n.

# Importante: Considere apenas números no intervalo de 1 a n. Se n for menor que 1, não existem pares. 

n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        if i * j == n:
            print(i, j)
  