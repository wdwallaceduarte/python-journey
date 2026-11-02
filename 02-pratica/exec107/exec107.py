# Crie um módulo chamado modeda.py que tenha as funções incorporadas `aumentar()`, `diminuir()`, `dobrar()` e `metade()`.
# 
# Faça também um programa que importe esse módulo e use algumas dessas funções. 
import moeda
# from moeda import metade

p = float(input('\nDigite o preço: R$ '))

print(f'\nA metade de R$ {p:g} é R$ {moeda.metade(p)}')
print(f'O dobro de R$ {p:g} é R$ {moeda.dobro(p)}')
print(f'Aumentando 10% de R$ {p:g}, temos R$ {moeda.aumentar(p)}')
print(f'Reduzindo 13% de R$ {p:g} teremos R$ {moeda.diminuir(p)}')
