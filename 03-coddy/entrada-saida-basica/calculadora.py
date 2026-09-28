## Calculadora de Divisão de Contas
# Calcula a porcentagem total da conta e divide pela quantidade de pessoas

print('='*40)
print('     Bill Split Calculator') 
print('='*40)

conta = float(input('Digite o valor da conta: '))
gorjeta = float(input('Digite o valor % da gorjeta: '))
n_pessoas = int(input('Quantidade de pessoas: '))
valor_gorjeta = (gorjeta / 100) * conta

valor_total = conta + valor_gorjeta

valor_por_pessoa = valor_total / n_pessoas

print('='*40)
print(f'Total (gorjeta incluso): R$ {valor_total}')
print(f'Cada pessoa paga: R$ {valor_por_pessoa}')
