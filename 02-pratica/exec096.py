# Falça um program que tenha a função chamara area(), que receba os dimenções de um terrmo retangular (largura e comprimento) e mostre a area do terreno.

def topo(msg):
    print('='*30)
    print(f'{msg:^30}')
    print('='*30)

def area(largura, comprimento):
    terreno = largura * comprimento
    print(f'A área do terreno {largura} x {comprimento} é de {terreno}m²')

# Programa pricipal
topo('Controle de Terrenos')

larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))

area(larg, comp)