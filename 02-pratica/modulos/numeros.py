# import uteis # primeira forma de importar as `def`

# num = int(input())

# fat = uteis.fatorial(num) # Utilizando a `def fatorial()`
# print(f'O fatoria de {num} é {fat}' )
# print(f'O dobro de {num} é {uteis.dobro(num)}' )

from uteis import fatorial, dobro # outra forma de importar inportando apenas as funções 

num = int(input())

fat = fatorial(num) # Não precisar usar uteis.
print(f'O fatoria de {num} é {fat}' )
print(f'O dobro de {num} é {dobro(num)}' )

