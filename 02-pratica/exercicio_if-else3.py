
# 1. Caixa eletrônico
# Crie um programa que receba o valor que o usuário deseja sacar.
# O caixa possui notas de:

# R$ 100
# R$ 50
# R$ 20
# R$ 10

# O programa deve informar quantas notas de cada valor serão necessárias.

# Exemplo:
# Valor do saque: 380

# Notas de R$100: 3
# Notas de R$50: 1
# Notas de R$20: 1
# Notas de R$10: 1

# Regra: o valor deve ser divisível por 10.
# Caso contrário:
# Valor inválido.

""" print('='*30)
print('     Caixa Eletônico')
print('='*30)


print(" Somente notas de:\n R$ 100\n R$ 50\n R$ 20\n R$ 10")
print('='*30)

saque =  int(input('Digite o valor do Saque: R$ '))
if saque % 10 != 0:
    print('Valor inválido.')
else:
    n_100 = saque // 100
    saque -= (n_100 * 100)
    n_50 = saque // 50
    saque -= (n_50 * 50) 
    n_20 = saque // 20
    saque -= (n_20 * 20) 
    n_10 = saque // 10

    print('='*30)
    print(f"Notas de R$100: {n_100}")
    print(f"Notas de R$50: {n_50}")
    print(f"Notas de R$20: {n_20}")
    print(f"Notas de R$10: {n_10}")


# 2. Triângulo
print('='*30)
print('     TRIÂNGULO')
lado1 = int(input('Lado 1: '))
lado2 = int(input('Lado 2: '))
lado3 = int(input('Lado 3: '))

if lado1 == lado2 and lado1 == lado3:
    print('='*30)
    print('Triângulo válido.\nTipo Equilátero.')
elif lado1 == lado2 and lado1 != lado3:
    print('='*30)
    print('Triângulo válido.\nTipo Isóceles.')
elif lado1 != lado2 and lado1 != lado3:
    print('='*30)
    print('Triângulo válido.\nTipo Escaleno.')

# 3. Ano bissexto
print('='*30)
print('     ANO BISSEXTO')
print('='*30)
    
ano = int(input('Digite um ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('='*30)
    print(f'{ano} é bissexto')
else:
    print('='*30)
    print(f'{ano} não é bissexto.')


# 4. IMC completo
print('='*30)
print(' IMC COMPLETO')
print('='*30)

peso = int(input('Digite o peso: '))
altura = float(input('Digite o altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('='*30)
    print(f' 
        Peso: {peso}
        Altura: {altura}

        IMC: {imc}
     > Classificação: Abaixo do peso 
    ')
elif imc < 24.9:
    print('='*30)
    print(f' 
        Peso: {peso}
        Altura: {altura}

        IMC: {imc}
     > Classificação: Peso normal 
    ')
elif imc < 29.9:
    print('='*30)
    print(f' 
        Peso: {peso}
        Altura: {altura}

        IMC: {imc}
     > Classificação: Sobrepeso
    ')
elif imc < 34.9:
    print('='*30)
    print(f' 
        Peso: {peso}
        Altura: {altura}

        IMC: {imc}
     > Classificação: Obesidade grau I
    ')
elif imc < 39.9:
    print('='*30)
    print(f' 
        Peso: {peso}
        Altura: {altura}

        IMC: {imc}
     > Classificação: Obesidade grau II
    ')
else:
    print('='*30)
    print(f' 
        Peso: {peso}
        Altura: {altura}

        IMC: {imc}
     > Classificação: Obesidade grau III
    ')


# Sistema de ingresso
print('='*30)
print('|     SISTEMA DE INGRESSO    |')
print('='*30)

print(' 
    1 - Pista → R$ 50,00
    2 - VIP → R$ 120,00
    3 - Camarote → R$ 250,00

    Digite o número da operação acima.
 ')
print('='*30)
# pista = 50
# vip = 120
# camarote = 250
tipo = int(input('Tipo do ingresso: '))
idade = int(input('Informe sua idade: '))
print('='*30)

if tipo == 1:
    tipo = "Pista"
    valor = 50
elif tipo == 2:
    tipo = "VIP"
    valor = 120
elif tipo == 3:
    tipo = "Camarote"
    valor = 250
else:
    print("Opção inválida")


if idade < 18:
    print('='*30)
    print('Menores de 18 anos não podem comprar.')
elif idade >= 60:
    print('='*30)
    print(f' 
        Tipo: {tipo}
        Idade: {idade}

        Preço original: R$ {valor:.2f}
        Desconto: 20%
        Preço final: R$ {valor * 0.20:.2f}
    ')
else:
    print(f' 
        Tipo: {tipo}
        Idade: {idade}

        Preço original: R$ {valor:.2f}
        Desconto: 0%
        Preço final: R$ {valor:.2f}
    ')


# 6. Jogo de advinhação
print('='*30)
print('     JOGO DE ADIVINHAÇÃO')
print('='*30)

secreto = 88
palpite = int(input('Palpite: '))

if palpite == secreto:
    print('='*30)
    print(f'Acertou!! O número secreto é {palpite}!')
elif palpite > secreto:
    print('='*30)
    print('Seu palpite é maior!')
elif palpite < secreto:
    print('='*30)
    print('Seu palpite é menor!')


# Calculadora de salário
print('='*30)
print('     CALCULADORA DE SALÁRIO')
print('='*30)


horas = int(input('Horas trabalhadas: '))
valor_hora = float(input('Valor da hora: '))

if horas >= 40:
    valor =  40 * valor_hora
    hora_extra = horas - 40
    valor_extra = (hora_extra * valor_hora)
    valor_extra += valor_extra * 0.50
    print(f" 
        Horas: {horas}
        Valor/hora: {valor_hora}
        
        40 horas normais = R$ {valor}
        {hora_extra} horas extras = R$ {valor_extra}
        
        Salário total = R$ {valor + valor_extra}
    ")

# 8. Sistema de classificação de funcionário
print('='*42)
print(' SISTEMA DE CLASSIFICAÇÃO DE FUNCIONÁRIO')
print('='*42)

nome = input(' Nome: ')
salario = float(input(' Salário: '))
tempo = int(input(' Tempo: '))
avaliacao = int(input(' Avaliação: '))
print('='*42)
if tempo >= 5 and avaliacao >= 4:
    bonus = salario * 0.20
    print(f' 
        Nome: {nome}
        Salário: R$ {salario:.2f}
        Tempo de empresa: {tempo}
        Avaliação: {avaliacao}

        Bônus: 20%
        Valor do bônus: R$ {bonus:.2f}
        Salário final: R$ {salario + bonus:.2f}
    ')
elif tempo >= 2 and avaliacao >= 3:
    bonus = salario * 0.10
    print(f' 
        Nome: {nome}
        Salário: R$ {salario:.2f}
        Tempo de empresa: {tempo}
        Avaliação: {avaliacao}

        Bônus: 10%
        Valor do bônus: R$ {bonus:.2f}
        Salário final: R$ {salario + bonus:.2f}
    ')
else:
    bonus = salario * 0.05
    print(f' 
        Nome: {nome}
        Salário: R$ {salario:.2f}
        Tempo de empresa: {tempo}
        Avaliação: {avaliacao}

        Bônus: 5%
        Valor do bônus: R$ {bonus:.2f}
        Salário final: R$ {salario + bonus:.2f}
    ')


# 9. Sistema de frete
print('='*30)
print(' SISTEMA DE FRETE')
print('='*30)
peso = float(input('Peso da encomenda: '))
valor = float(input('Valor da encomenda: '))

if valor >= 200:
    frete = "GRÁTIS"
    print(f" 
        Compra: {valor:.2f}
        Peso: {peso}Kg
        Frete: {frete}
        Total: {valor:.2f}
    ")
else:
    if peso <= 1:
        frete = 10
        print('='*30)
        print(f" 
            Compra: {valor:.2}
            Peso: {peso}Kg
            Frete: {frete:.2f}
            Total: {valor:.2f}
        ")
    elif peso <= 5:
        frete = 20
        print('='*30)
        print(f" 
            Compra: {valor:.2}
            Peso: {peso}Kg
            Frete: {frete:.2f}
            Total: {valor:.2f}
        ")
    else:
        frete = 40
        print('='*30)
        print(f" 
            Compra: {valor:.2}
            Peso: {peso}Kg
            Frete: {frete:.2f}
            Total: {valor:.2f}
        ") 
"""

# Sistema de aprovação
print('='*30)
print('     SISTEMA DE APROVAÇÃO')
print('='*30)

nome = input('Nome do estudante: ')
nota_1 = float(input('Nota 1: '))
nota_2 = float(input('Nota 2: '))
nota_3 = float(input('Nota 3: '))

frequencia = int(input('Frequência: '))

trabalho = input('Trabalho final:\n 1 - Sim\n 2 - Não\n >  ')

if trabalho == '1':
    trabalho = 'Sim'
elif trabalho == '2':
    trabalho = 'Não'
else:
    print('Opção inválida.')

media = (nota_1 + nota_2 + nota_3) / 3

if trabalho == "2" or media >= 5 and media < 7 and frequencia >= 75:
    print('='*30)
    print('     RESULTADO DO ALUNO')
    print('='*30)
    print(f""" 
        Nome: {nome}
        Nota 1: {nota_1}
        Nota 2: {nota_2}
        Nota 3: {nota_3}
        Média: {media}

        Frequência: {frequencia}%
        Trabalho Final: {trabalho}

        Situação: RECUPERAÇÃO
    """)
else:
    if media < 6  or frequencia < 75:
        print('='*30)
        print('     RESULTADO DO ALUNO')
        print('='*30)
        print(f""" 
          Nome: {nome}
          Nota 1: {nota_1}
          Nota 2: {nota_2}
          Nota 3: {nota_3}
          
          Média: {media}

          Frequência: {frequencia}%
          Trabalho Final: {trabalho}

            Situação: REPROVADO 
        """)
    else:
        print('='*30)
        print('     RESULTADO DO ALUNO')
        print('='*30)
        print(f""" 
            Nome: {nome}
            Nota 1: {nota_1}
            Nota 2: {nota_2}
            Nota 3: {nota_3}
            Média: {media}

            Frequência: {frequencia}%
            Trabalho Final: {trabalho}

            Situação: APROVADO 🎉
        """)
