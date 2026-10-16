# (Controle de Frequência em Academia): Crie um programa que gerencie a entrada de alunos em uma academia utilizando um dicionário, onde as chaves são os nomes dos alunos matriculados e os valores são a quantidade de dias que eles compareceram nos treinos este mês. O programa deve solicitar que a recepção digite o nome do aluno que acabou de passar pela catraca. Se o nome constar no sistema, o programa deve exibir o histórico de acessos daquela pessoa e somar mais 1 dia de presença ao valor atual; caso contrário, deve exibir uma mensagem informando que o aluno não possui matrícula ativa na unidade.

# from uteis import escreva
import uteis
from modulos import escreva # Está dando erro
escreva('testando')
uteis.escreva('Controlde de Frequência')

alunos = {
    'wallace': 15,
    'duarte': 14
}

nome = input('\nDigite o nome do aluno: ').lower()

if nome in alunos:
    print(f'Nome: {nome}')
    print(f'Historico de acesso: {alunos[nome]}')
else:
    print('Aluno não possui matricula.\n')

    novo_aluno = input('Deseja cadastrar aluno? (s/n): ')

    # if novo_aluno.lower() == 's':


alunos[nome] += 1

print('\nPresença registrada!')
print(f'Total de dias: {alunos[nome]}')
