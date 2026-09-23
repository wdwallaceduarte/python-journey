""" 
# Maior de idade
print('='*30)
print('     MAIOR DE IDADE ')
print('='*30)

nome = input('Informe seu nome: ')
idade = int(input('Informe sua idade: '))
altura = float(input('Qual sua altura: '))

if idade >= 18:
    print('='*30)
    print(f'> {nome} é MAIOR de idade!\nSua altura é {altura}\n')
else:
    print('='*30)
    print(f'> {nome} é MENOR de idade!\nSua altura é {altura}\n') 



# Positivo ou negativo
print('='*30)
print('     POSITIVO OU NEGATIVO')
print('='*30)

n1 = int(input('Informe um número: '))

if n1 < 0:
    print('='*30)
    print(f'{n1} é NEGATIVO\n')
elif n1 > 0:
    print('='*30)
    print(f'{n1} é POSITIVO\n')
else:
    print('='*30)
    print(f'{n1} é Positivo :(\n')

print('↓'*30)

# Ordem crescente
print('='*30)
print('     ORDEM CRESCENTE')
print('='*30)

n1 = int(input('Informe um número: ')) 
n2 = int(input('Informe outro número: ')) 

if n1 < n2:
    print('='*30)
    print(f" 
        {n1} - {n2}
     ")
elif n1 > n2:
    print('='*30)
    print(f" 
        {n2} - {n1}
     ")
else:
    print('='*30)
    print('São iguais')

    
Sistema de aprovação escolar

Peça ao usuário:

3 notas de um aluno;
Número de faltas;
Se ele entregou o trabalho final (sim ou nao).

Calcule a média e determine a situação:

Reprovado por faltas → mais de 25 faltas.
Reprovado por média → média menor que 5.
Recuperação → média entre 5 e 6,9.
Aprovado → média ≥ 7.
Porém, se a média for ≥ 7 mas o trabalho final não foi entregue, o aluno fica em recuperação.
Se tiver mais de 25 faltas, é reprovado independentemente das notas.

Desafio extra: valide também se as notas estão entre 0 e 10 e se a quantidade de faltas não é negativa.
"""

# Sistema de aprovação escolar
print('='*33)
print('    SITEMA DE APROVAÇÃO ESCOLAR')
print('='*33)

aluno = input('Nome de aluno: ')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

falta = int(input('Quantidade de faltas do aluno: '))

trabalho = input('Trabalho final:\n 1 → Sim\n 2 → Não\n> ')

if trabalho == "1":
    trabalho = "Sim"
elif trabalho == "2":
    trabalho = "Não"
else:
    print('Valor Inválido.')

if falta >= 25:
    print('='*33)
    print(f""" 
        Aluno: {aluno}
        Média: {media}
        Trabalho final: {trabalho}
        Situação: Reprovado por falta.
    """)
else:
    if media < 5:
        print('='*30)
        print(f""" 
            Aluno: {aluno}
            Média: {media}
            Trabalho final: {trabalho}
            Situação: Reprovado por média. 
        """)
    elif media >= 5 and media <= 6.9:
        print('='*30)
        print(f""" 
            Aluno: {aluno}
            Média: {media}
            Trabalho final: {trabalho}
            Situação: Recuperação.
        """)
    elif media >= 7 or trabalho == "2":
        print('='*30)
        print(f""" 
            Aluno: {aluno}
            Média: {media}
            Trabalho final: {trabalho}
            Situação: Recuperação.
        """)
    else:
        print('='*30)
        print(f""" 
            Aluno: {aluno}
            Média: {media}
            Trabalho final: {trabalho}
            Situação: Aprovado.
        """)
    

