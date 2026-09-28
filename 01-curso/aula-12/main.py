""" numeros = []

numeros.append(int(input('Digite um número: ')))
numeros.append('Kira')
numeros.append('Pandora')
numeros.append('Laguertha')
numeros.append('Siggy')
numeros.append('Laofei')

print(numeros)

lista = ['M','O', 'N', 'T', 'Y','','P', 'Y', 'T', 'H', 'O', 'N']
# key =   0   1   2 
print(lista[0:5])
print(lista[6:12]) # imprime o intervalo dos indeices/key
print(lista[-1])
print() """

num = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

print('Tamanho da lista: ', len(num)) # Saída: Tamanho da lista: 10
print('Soma dos elementos: ', sum(num)) # Saída: Soma dos valores dos elementos: 39
print('Menor elemento: ', min(num)) # Saída: Menor elemnto: 1
print('Maior elemento: ', min(num)) # Saída: Maior elemento: 9
print('Lista ordenada: ', sorted(num)) # Saída: Lista ordenada: [1, 1, 2, 3, 5, 6, 9]

print('=-'*30)
cores = ['black', 'magenta', 'cyan', 'green', 'red']
# key =    0         1         2        3       4
print('Lista de cores:', cores)
print('Quantidades de cores: ',len(cores)) # conta a quantidade dos valres
print('Menor: ',min(cores)) # menor valor pela ordem alfabetica
print('Maior: ',max(cores)) # maior valor pela ordem alfabetica
print('Cores em ordem alfabetica: ',sorted(cores))
print('Cores em ordem inversa: ', cores.sort(reverse=True))






