
# Ambiente para testes e codigos temporarios:
def escreva(msg):
    tam = len(msg) +4
    print('='*tam)
    print(f'  {msg}')
    print('='*tam)
    
def dobra(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *=2
        posicao += 1

valores = [6, 4, 5, 4, 10 ,140]

dobra(valores)
print(valores)

