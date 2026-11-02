# Crie um módulo chamado modeda.py que tenha as funções incorporadas `aumentar()`, `diminuir()`, `dobrar()` e `metade()`.
# 
# Faça também um programa que importe esse módulo e use algumas dessas funções. 
import moeda
# from exec109 import moeda

p = float(input('\nDigite o preço: R$ '))

print(f'\nA metade de  {moeda.moeda(p)} é  {moeda.metade(p, True)}')
print(f'O dobro de  {moeda.moeda(p)} é R$ {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos  {moeda.aumentar(p, 10, True)}')
print(f'Aumentando 13%, temos  {moeda.aumentar(p, 13, True)}')
