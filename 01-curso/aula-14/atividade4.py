# Fala um program aque leia dois vetores com 10 elementos cada, gere um terceiro vetor com 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dois outros valores.

lista_1 = []
lista_2 = []
lista_3 = []

print('Elementos do Primeiro Vetor')
for i in range(10):
    elemento = int(input(f'Elemento {i+1}: '))
    lista_1.append(elemento)
print('Elementos do Segundo Vetor')
for i in range(10):
    elemento = int(input(f'Elemento {i+1}: '))
    lista_2.append(elemento)
for i in range(10):
    lista_3.append(lista_1[i])
    lista_3.append(lista_2[i])
print(f'Vetor Intercalado {lista_3}')



# lista = [['wallace', 4 , 5, 6, 7], ['duarte', 1, 2, 4, 10]]
# print(lista)
