# Escreva uma função chamada calcular_media que receba uma lista de números e retorne a média desses números

def calcular_media(num1, num2, num3):
    notas = [num1, num2, num3]
    return (num1 + num2 + num3) / 3
    print(notas)

calcular_media(8,8,8)
# primeira forma de mostrar a media na tela 
print(f'Media: {calcular_media(5,7,8)}')
# segunda forma demostrar media na tela 
media = calcular_media(10,6,9)
print(f'Media: {media}')