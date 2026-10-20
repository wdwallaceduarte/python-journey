# Faça um program para aprovar o emprestimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado.

casa = float(input('\nQual o valor da casa?\n > '))
salario = float((input('\nQual o salário do cliente?\n > ')))
anos = int(input('\nQuantos anos o cliente quer pagar?\n > '))
prestacao = casa / (anos * 12)
minimo = salario * 0.30
print(f'Para pagar uma casa de R$ {casa:.2f} em {anos} anos', end='')
print(f' a prestação será de R$ {prestacao:.2f}')
print(salario)

if prestacao <= minimo:
    print('\nCredito APROVADO!')
else:
    print('\nEmpresimo Negado!')