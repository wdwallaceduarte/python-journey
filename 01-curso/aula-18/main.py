# Dicionario
# Sintaxe:
# nome_dicionario = {'chave':valor, chave:valor} 

dicionario = {

    'nome': 'Wallace', 
    'idade': 38,
    'altura': 1.71,
    'peso': 80
}

# print('\n',dicionario)

# print('\n',dicionario['nome'], end=' ')
# print(dicionario['altura'])

# dicionario['profissao'] = 'Full Stack' # adiciona chave-valor 'profissao': 'Full Stack'
# dicionario['salario'] = 11000 # adicina chave-valor 'salario': 11000
# print('\n', dicionario)

# del dicionario['peso'] # Deleta a chave-valor 'peso': 80
# print('\n',dicionario)

# if 'nome' in dicionario:
#     print('Existe nome')
print()

chaves = dicionario.keys()
valores = dicionario.values()
duplas = dicionario.items()

print(chaves)
print(valores)
print(duplas)

    
print()