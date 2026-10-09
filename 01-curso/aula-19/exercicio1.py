# 1. Crie um dicionário que represente informações sobre uma pessoa, como nome, idade cidade natal e profissão;

pessoa = {
    'nome': 'Wallace',
    'idade': 38,
    'cidade_n': 'Fortaleza',
    'profissao': 'Programador'
}
pessoa1 = {
    'nome': 'Duarte',
    'idade': 38,
    'cidade_n': 'Fortaleza',
    'profissao': 'Programador'
}

""" print(pessoa, '\n', pessoa1)
# 2. Acesse e imprimia valores especificos do dicionário que você cricou no exercicio anterior;
print(pessoa['nome'])
print(pessoa['idade'])

# 3. Modifique o valor de um item no dicionário que você cruiy e, em seguida, imprima dicionario atualizado;

pessoa['idade'] = 37
print('\n',pessoa)

# 4. Adcione informações adidionais a pessoa no dicionario, como seu endereço de email e numero de telefone
pessoa['email'] = 'wd.wallaceduarte@gmail.com'
pessoa['telefone'] = '85 987563268'

print(f'\nEndereço de email e telefone adicionando:\n {pessoa}')

# 5. Remova um item do dicionario, como o numero de telefone, e imprima o dicionatio

del pessoa['telefone']
print(f'\nTelefone removido:\n {pessoa}') """

# Extra: motrar o print da mesma forma que a estutura;

for chave, valor in pessoa1.items():
    print(f'{chave}: {valor},')

print()

