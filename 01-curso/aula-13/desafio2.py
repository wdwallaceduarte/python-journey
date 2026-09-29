lista_numeros = []
lista_pares = []
lista_impares = []

for i in range(20):
    numeros = int(input('Digite um numero: '))
    lista_numeros.append(numeros)

for i in range(20):
    if lista_numeros[i] % 2 == 0:
        lista_pares.append(lista_numeros[i])
    else:
        lista_impares.append(lista_numeros[i])

print(f""" 
    Todos os numeros: {lista_numeros}
    Numeros pares: {lista_pares}
    Mumeros impares: {lista_impares}
 """)