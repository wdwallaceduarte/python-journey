""" 
# Calculo IMC

print('='*30)
print('     CALCULO IMC ')
print('='*30)
peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))

print(f" 
    Peso: {peso}
    Algura: {altura}

    IMC: {peso / altura ** 2:.2f}
")

# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salario no referido mes, sabendo se que são descontados 11% para imposto de Renda, 8% para IN7SS e 5% para o sindicato, faça um programa que nos de salario bruto.
# a. quanto pagou ao IR
# b. quando pagou ao INSS
# c. quanto pagou ao sindicato
# d. o slário lpiquido.
print('='*30)
print('|       SALARIO              |')
print('='*30)
valor_hora = float(input('Qual valor por hora? R$'))
hora_rabalhada = float(input('Quantas horas trabalhada? '))

salario = hora_rabalhada * valor_hora

inss = salario * 0.08
sindicato = salario * 0.05
ir = salario * 0.11

print('='*30)
print(f" 
    Salário bruto: {salario:.2f}
    INSS: {inss:.2f}
    Sindicato: {sindicato:.2f}
    IR: {ir:.2f}

    Liquido: {salario - inss - sindicato - ir:.2f}
")
"""

#Pizzaria

print('='*30)
print('|       PIZZARIA             |')
print('='*30)

pizza = float(input('Qual valor da pizza? R$'))
venda = float(input('Quantidade de pizzas vendida? '))

valor = pizza * venda

custos_fixo = valor * 0.30
custos_variado = valor * 0.20

print('='*30)
print(f""" 
    Valor bruto: {valor:.2f}
    Custos fixos: {custos_fixo:.2f}
    Custos variados: {custos_variado:.2f}

    Liquido: {valor - custos_fixo - custos_variado:.2f}
""")





