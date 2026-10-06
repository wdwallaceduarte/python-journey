""" def saudacao(name):
    print(f'Olá {name}')
name = (input('Qual seu nome? '))
saudacao(name)

# --------------------------------------------------

def combustivel(nome):
    print(f'Estou usando {nome}')

nome = input('Alcool ou Gasolina? ')
combustivel(nome) 

# --------------------------------------------------

def soma(num1, num2):
    print(num1 + num2)

def subitrair(num1, num2):
    print(num1 - num2)

def multiplicar(num1, num2):
    print(num1 * num2)

def dividir(num1, num2):
    print(num1 / num2)

def dividirInt(num1, num2):
    print(num1 // num2)

# Chamada das funções
soma(10,20)
subitrair(10,20)
multiplicar(10,20)
dividir(10,20)
dividirInt(10,20)


var_externa = 'Variavel externa'
def funcao_escopo():
    print('Externa dentro da Função: ', var_externa)
    var_interna = 'Variavel interna'
    print('Externa dentro da Função: ', var_interna)

funcao_escopo() # chamada da função

print('Externa fora da função: ', var_externa)
# print('Externa fora da função ', var_interna) # Apresenta erro ao imprimir

def funcao_escopo_retorno():
    var_interna = 'Variavel interna'
    return var_interna

var_retorna = funcao_escopo_retorno()
print('Retorno dora da função: ', var_retorna)"""

# def soma(num1, num2):
#    return num1 + num2

# def subitrair(num1, num2):
#     return num1 - num2

# def multiplicar(num1, num2):
#     return num1 * num2

# def dividir(num1, num2):
#     return num1 / num2

# print(soma(10, 5))
# print(subitrair(10, 5))
# print(multiplicar(10, 5))
# print(dividir(10, 5))












