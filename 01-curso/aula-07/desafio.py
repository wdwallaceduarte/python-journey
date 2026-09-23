combustivel = int(input('Quantitade do combustivel: '))
atmosfera = input('Atmosfera respiravel: 1 - Sim 2 - Não: ')
traje = input('Integridade do Traje: 100% ') #

if combustivel >= 15 and atmosfera == '1' or traje == 100:
    print('Pouso autorizado!')
else:
    print('Pouso Abortado: Risco de morte!!!')

 