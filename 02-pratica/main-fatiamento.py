# FATEAMENTO, ANALISE E TRANSFORMAÇÃO DE UMA STRING

nome = 'wallace'
#key =  0123456 
completo = 'Antonio Wallace Ferreira Duarte'
   # key =  0123456789....................31 
# n = int(input('Digite um numero: '))
# FATEAMENTO
print('\n\33[32m - FATEAMENTO \33[0m')
# Traz a letra referente a key 6 no caso letra 'e'
print(nome[6]) 
# Traz as letras referente a key do 8 ao 17 no caso 'wallace f'
print(completo[8:17])
# Traz as letras a partir da key 8 até o final da string
# usado quando não se sabe o tamanho final da strint
print(completo[8:])
# Traz as letras de 1 a 15 pulando de 2 em 2
print(completo[1:15:2])
#Traz de 1 ao final da string pulando de 2 em 2
print(completo[1::2])

# ANALISE DE STRING
print('\n\33[32m - ANALISE \33[0m')
# o metodo '.count('o')' conta quantas letras "o" tem na string
print(completo.count('w'))
# '.upper()' faz toda a string ficar maiuscula 
print(nome.upper())
# '.lower()' faz toda a string ficar minuscula 
print(nome.lower())
# '.en()' usado pra descobri o tamnho da string contando com os espaços
print(len(nome))
print(len(completo))
# '.strip() é um metodo que remove os espaços antes e depois da string
print(nome.strip())
# '.replace' é um metodo que localiza e troca uma parte da string, mas não define definitivamente
print(completo.replace('Ferreira', 'Duarte'))
print(completo)
# Dessa forma será definitva
# completo = completo.replace('Ferreira', 'Duarte')
# print(completo)

# forma que verfica se uma palavra ou caracter na string, no caso 'Duarte
print('Duarte' in completo)

# '.find()' localiza a posição da palavra a partir da primeira key localizada
print(completo.find('Duarte')) # nesse caso a partir da key 25
print(completo.find('duarte')) # se não encontrar irá mostrar -1

# '.split()' é o metodo que divide a string a cada espaço
dividido = completo.split()
print(dividido) # saida cria uma lista com cada nome separado
print(dividido[2]) # Saida: Ferreira
print(len(dividido))
print(dividido[1][0])



