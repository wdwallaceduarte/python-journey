# Calculando Potencia: escreva um program que solicite ao usuário uma base e um expoente e, em seguida, utilize um loop for para calcular a potencia (base^expoente) sem utilizar o operador **

n1 = int(input('Base: '))
n2 = int(input('Expoente: '))

resultado = 1

for i in range(n2):
    resultado *= n1

print(resultado)