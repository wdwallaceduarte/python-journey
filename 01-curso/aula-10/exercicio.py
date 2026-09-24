# Faça um programa receba dois numero sinteiros e print os npumeros inteiros que estão no intervalo compreendido por eles
# \033[m
print('='*30)
print(""" 
     EXERCICIO 10 
""")
print('='*30)

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
passo = int(input('Digite número de passo: '))

for i in range(n1, n2+1, passo):
    print(i)
# print(n2)