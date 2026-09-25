# Serié de fibonacci: Escreva um programa que utlize um loop for para os primeiros 10 números da serie fibonacci.
# 0 , 1, 1, 2, 3, 4, 5, 6...

a = 0 
b = 1
for i in range(2000000000):
    c = a + b
    print(a)
    a = b
    b = c

    