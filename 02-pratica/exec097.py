# Faça uma program que tenha uma função chamada escreva(),
# que receva um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(msg):
    tam = len(msg) +4
    print('='*tam)
    print(f'  {msg}')
    print('='*tam)

escreva('Wallace Duarte')
escreva('Estou gostando de Python')

