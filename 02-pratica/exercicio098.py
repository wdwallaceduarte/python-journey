# Faça um programa que tenha uma função chamada contador(), que receba três parametros: inicio, fim e passo e realize a contagem.
# 
# Seu programa tem que realizar tres contagens através da função criada:
# 
# a) De 1 até 10, de 1 em 1;
# b) De 10 até 0, de 2 em 2;
# c) Uma contagem presonalizada.  

from time import sleep

def separar():
    print('>'*10, end=' Prepara ')
    print('<'*10)

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    separar()
    print(f'Contando de {inicio} até {fim} de {passo}')
    sleep(2.5)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True) # flush=True funciona com sleep para que mostre na tela simultaneamente
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM!')

# Porgrama principal
contador(1, 10, 1)
contador(10, 0, 2)
separar()
print('Agora é sua vez de personalizar a contagem')
inic = int(input('Inicio:  '))
fim = int(input('Fim:     '))
pas = int(input('Passo:   '))
contador(inic, fim, pas)
