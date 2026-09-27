# Crie um program onde o usuário possa digitar vários valores numéricos e castre-os em uma lista. Caso o número já exita lá dentro, ele não será adicionado . No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []

for v in valores:
    valores.append(int(input('Digite um valor: ')))
    if valores == valores:
        print('Valor duplicado!')
    else:
        print('Valor adcionado com sucesso.')