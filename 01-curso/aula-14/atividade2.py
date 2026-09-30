# Faça um programa que leia 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes

lista = []
consoantes = 0
vogais = 'aeiou'


for i in range(1, 11):
    char = input(f'Digite o {i} caracteres: ')
    lista.append(char)
    if char not in vogais:
        consoantes +=1
print(lista)

if i in lista:
    if i not in vogais:
        print(i)

print(f'Total de consoantes: {consoantes}')

