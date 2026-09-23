age = int(input("Digite sua idade: "))

with_parent = input() == 'true'

message = 'None'

if age >= 18:
    message = "You can watch any movie"
else:
    if with_parent:  
        message = "You can watch PG-13 movies"
    else:
        message = "You can only watch G-rated movies"

print(message)

b1 = 5
b2 = 2
b3 = not((b1 + b2) > (b1 * b2))

#====================================================

# Note que x e y devem conter números inteiros positivos ou negativos.

print(f'b3 = {b3}')
print('='*45)
print(""" 
    ENQUANTO (z) NÃO FOR TRUE REPETE 
z = ((x * y) < (x + y) && (x + y) < (x - y))
""")
print('='*45)
z = ''

while z != True:
    x = int(input('x: '))
    y = int(input('y: '))

    z = ((x * y) < (x + y) and (x + y) < (x - y))

    print(f'\n> z: {z}')
