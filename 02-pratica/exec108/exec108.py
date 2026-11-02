# Crie um módulo chamado modeda.py que tenha as funções incorporadas `aumentar()`, `diminuir()`, `dobrar()` e `metade()`.
# 
# Faça também um programa que importe esse módulo e use algumas dessas funções. 
import moeda
# from exec108 import moeda

p = float(input('\nDigite o preço: R$ '))

print(f'\nA metade de  {moeda.moeda(p)} é  {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de  {moeda.moeda(p)} é R$ {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10% de  {moeda.moeda(p)}, temos  {moeda.moeda(moeda.aumentar(p, 10))}')
