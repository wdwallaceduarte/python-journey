# Contagem de caracteres: escreva um programa que solicite ao usuáriouma frase e, em seguida, utilize um lop for para contar e imprimir o número de caracteres na frase

nome = input('Digite seu none completo: ')
contador = 0

for i in nome:
    if i != '':
        contador +=1
    print(f'A quantidade de caracteres é: {contador}')