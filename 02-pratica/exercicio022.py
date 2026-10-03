# Crie um programa que leia o nome completo de uma pessoa e mostre:
# [RF1]. O nome com todas as letras maiusculas;
# [RF2]. O nome com todas as letras minusculas;
# [RF3]. Quantas letras ao todo (sem considerar espaços);
# [RF4]. Quantas letras tem o primeiro nome.

print('\33[36m-=\33[0m'*30)

nome = input('\nDigite seu nome completo:\n > ')

# [RF1]
print(f"""
Seu nome com todas as letas maiúsculas:
    \33[32m{nome.upper()}\33[0m
""")

# [RF2]
print(f""" 
Seu nome com todas as letras minúsculas:
    \33[32m{nome.lower()}\33[0m 
""")

# [RF3]
remove_espacos = nome.replace(' ', '')
print(f'Seu nome tem um total de \33[32m{remove_espacos.count('')}\33[0m letras.\n')
# [RF4]
dividido = nome.split()
dividido = dividido[0]
# print(dividido)
print(f'Seu primeiro nome tem \33[32m{dividido.count('')}\33[0m letras.')

print('\33[36m-=\33[0m'*30)

