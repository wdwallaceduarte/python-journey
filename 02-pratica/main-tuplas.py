# Tupla é identificado por ter uma lista de '()', e imultável, não pode ser alterada.
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
#  key =      0            1        2        3

print(""" 
    lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
    #  key =      0            1        2        3
    
 """)

# imprime a 'pizza'
print(lanche[0]) 
print(lanche[2]) #imprime 'pizza'

# imprime 'hambruguer', 'suco'
print(lanche[0:2]) 

# imprime do 'haburger' até o ultimo item
print(lanche[1:])  

# imprime a partir do final, nesse caso o 'pudim'
print(lanche[-1])

# metodo len() mostra quantos elementos tem na variavel 
len(lanche) # mostrara 4 

# Exemplos: 

print()
print('Itens da minha tupla: ', end='')
print(lanche)

print()
for i in range(len(lanche)):
    print(f' O {i} da tupla de lanche é: {lanche[i]}')

print()
for comida in lanche:
    print(f' Eu vou comer {comida}')

print()
for posicao, comida in enumerate(lanche):
    print(f'Na posição {posicao} da tupla está -> {comida}')

print(lanche[0])
print(lanche[1])
print(lanche[2])
print(lanche[3])

# O metodo 'sorted()' Mostra a ordem alfabetica ou numerica se for o caso
print(sorted(lanche)) 
print(lanche) # apenas para comparação

# o metodo count(), conta quantas vezes um elemento aparece na tupla
print(lanche.count('suco'))