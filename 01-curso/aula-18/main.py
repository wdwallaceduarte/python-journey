# Dicionario
# Sintaxe:
# nome_dicionario = {'chave':valor, chave:valor} 

nome_dicionario = {
    'nome':'Wallace', 
    'idade':38,
    'altura': 1.71,
    'peso': 80
}

print('\n',nome_dicionario)

print('\n',nome_dicionario['nome'], end=' ')
print(nome_dicionario['altura'])

nome_dicionario['profissao'] = 'Full Stack' # adiciona chave-valor 'profissao': 'Full Stack'
nome_dicionario['salario'] = 11000 # adicina chave-valor 'salario': 11000
print('\n', nome_dicionario)

del nome_dicionario['peso'] # Deleta a chave-valor 'peso': 80
print('\n',nome_dicionario)

if 'nome' in nome_dicionario:
    print('Existe nome')
    
print()