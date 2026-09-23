""" # Faça um programa que peça a nota de um aluno e informe se ele foi aprovado (nota maior ou igual a 7) ou aprovado."""
# print('='*30)
# print('      TURNO ')
# print('='*30)
# print(""" 
#     M - Matutino
#     V - Vespertino
#     N - Noturno
#  """)
# print('='*30)
# nome = input('Qual seu nome? ')
# turno = input('Em que turno voce estuda? ').lower()


# if turno == "m" or turno == 'M': # Primeira forma de compração
#     print(f'Bom dia {nome}! 🌞')
# elif turno == "v": # Segunda forma de comparação precisa do .lower()
#     print(f'Boa tarde {nome}! 🌞')
# elif turno in "nN": # Terceira forma de comparação
#     print(f'Boa Noite {nome}! 🌛')
# else:
#     print('Valor Invalido! 🧟')
 


# Faturamento total da empresa
fat = 45000

# Custo total da empresa
custo = 23500

# Cálculo do lucro (faturamento - custo)
lucro = fat - custo

# Cálculo da margem de lucro (lucro dividido pelo faturamento)
margem = lucro / fat

# Exibe o lucro formatado em reais e a margem em porcentagem
# :,.2f : formata número com separador de milhar e 2 casas decimais
# :.0% : converte para porcentagem sem casas decimais
print(f"Lucro: R${lucro:,.2f}, Margem: {margem:.0%}")
