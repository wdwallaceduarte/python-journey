""" # Sintaxe da função
    
    def nome_da_função(parametro):
        # Bloco de código 
"""
    
# Função que cria uma linha 
def linha():
    print('-'*30)

def mensagem(msg):
    print('='*30)
    print(msg)
    print('='*30)

# O * faz a função de desempacotamento dos números, usado quando não se sabe a quantidade de parametros a ser passado 
def numeros(*num): 
    print(num)

def soma(* valores):
    soma = 0 
    for num in valores:
        soma += num
    print(f'Somando so valores {valores} temos {soma}')


# PROGRAM PRINCIPAL

# Usando a funão linha() criada acima
print('\33[3;30m # Usando a funão \33[32m linha()\33[0m criada acima\33[0m')
linha() # chamada da função que cria a linha
print(' Nome: Antonio Wallace ')
linha()
print(' Complemento: Ferreira Duarte ')
linha()

print('\n')

# Usando a função mensagem() criada acima
print('# Usando a função \33[32m mensagem()\33[0m criada acima')
mensagem('Python é muito bom?')

# Chamada da função numero()
print('\33[3;30m # Chamada da função numero() \33[0m')
numeros(1, 5, 4, 7, 50, 18)
numeros(8, 15, 14)
numeros(28, 25)

# Outro exemplo da chamada função usando desempacotamento
print('\33[3;30m # Outro exemplo da chamada função usando desempacotamento\33[0m')
soma(1, 5, 4, 7, 50, 18)
soma(8, 15, 14)



