# faça um program no qual a pessoa deve escrever o nome de tres produtos e preencher uma lista

lista_de_compra = []

for i in range(1,5):
    lista_de_compra.append(input(f'Informe o item {i} da lista: '))

print('=-'*30)
print('> Você adcionou a lista os items: ',lista_de_compra)

for i in range(len(lista_de_compra)):
    print(lista_de_compra[i])