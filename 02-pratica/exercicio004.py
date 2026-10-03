# Faça um program aque leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possivels sobre ele.
print('_'*50)
var = input('\nDigite algo: ')

# type() informa o tipo do caracter
print(f'O tipo primitivo desse valor é \33[36m {type(var)}\33[0m') 
# `.isspace()` verifica se a entrada é apenas espaco 
print(f'Só tem espaços? \33[36m {var.isspace()}\33[0m') 
# `.isnumeric()` verifica se a entrada é apenas número 
print(f'É um número? \33[36m {var.isnumeric()}\33[0m' )
# `.isalpha()` verifica a entrada é alfabetico
print(f'É alfabético? \33[36m{var.isalpha()}\33[0m')
# '.isalnum()' verifica se a entrada é alfanúmerico
print(f'É alfanúmerico? \33[36m{var.isalnum()}\33[0m')
# '.isupper()' verifica se a entrada é maiúscula
print(f'É maiúscula? \33[36m{var.isupper()}\33[0m', )
# '.islower()' verifica se a entrada é minúscula
print(f'É minúscula? \33[36m{var.islower()}\33[0m')
# '.istitle()' verficia se a entrada é capitalizada, maiúscula e minúscula
print(f'É capitalizado? \33[36m{var.istitle()}\33[0m')


