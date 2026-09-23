# Faça um programa que peça 2 números inteiros e um número real.
#
# a. Calcule e mostre o porduto do dobro do primeiro com metade do segundo.
# b. a soma do truplo do primeiro com o terceiro 
# c. o terceiro elevado ao cubo.

print('='*30)
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

print(f"""
    Letra A -  {n1*2 * n2/2}
    Letra B -  {n1*3 + n3}
    Letra C -  {n3**3}
""")