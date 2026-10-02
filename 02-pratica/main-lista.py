# Listas guardam varios valores, mas diferente das tuplas representadas por (), as listas representadas por [], podem ser alteradas, as tuplas não. Tuplas são imultaveis e as listas podem ser modificadas.

lanche = ['🍔', '🧃', '🍕', '🍦']
# key =     0     1      2     3

## MANIPULAÇÃO DE LISTA
# Comando/método que adciona item/valores a lisata
lanche.append('cooke') # Adciona um valor/item ao fim da lista, nesse exemplo adiona 'cooke'
lanche.insert(0,'impada') # Adciona um valor/item indicando a sua key, nesse caso adciona impada a key '0'

# Comandos que deletam item/valores da lista
del lanche[3] # Remove o valor/item da lista usando a key, nesse caso a key '3' será deletado.
lanche.pop(3) # Método pop removo o último valor/item da lista, mas pode pode usar o parâmetro key, nesse caso o '3'
lanche.remove('🍕') # wMetedo remove pelo valor/item da lista, logo o valor deve ser informado.
lanche.clear() # Remove tudo da lista

# print(lanche)
# Para verificar se o valor/item existe na lista
if '🍕' in lanche:
    lanche.remove('🍕')

# Criando lista usando uma função list() e passar um  range como parâmetro:
valores = list(range(4,11))
# Criando lista fora de ordem:
valores = [8, 2, 5, 4, 9, 3, 0]
#   key =  0  1  2  3  4  5  6
valores.sort() # Método que ordena todos os valores/item de forma cressente 
valores.sort(reverse=True) # Ao passar o parâmetro `verese=True` a lista fica decressente
len(valores) # Método para informar quantos valores/item tem na lista passando a variavel como parâmetro

print(valores)
