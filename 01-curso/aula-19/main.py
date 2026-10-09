pessoa = {
    
    'nome': 'Wallace', 
    'idade': 38,
    'altura': 1.71,
    'peso': 80,
    'endereco': {
        'rua': ' 41',
        'numero': 30,
        'complemento': 'Casa C',
        'bairro': 'Barra do ceara',
        'cidade': 'Fortaleza',
    }
}

for i in pessoa:
    print(i, ": ", pessoa[i])

print('-='*30)

for chave, valor in pessoa.items():
    print(chave, ': ', valor)

print('-='*30)

print(f'Rua: {pessoa["endereco"]['rua']}')
print(f'Numero: {pessoa["endereco"]['numero']}')
print(f'Complemento: {pessoa["endereco"]['complemento']}')
print(f'Bairro: {pessoa["endereco"]['bairro']}')
print(f'Cidade: {pessoa["endereco"]['cidade']}')
