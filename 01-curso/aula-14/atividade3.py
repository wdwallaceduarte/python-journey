# Faça um program que peça as quatro notas de 10 alunos, calcule e armazene em um vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0


medias = []

while len(medias) < 10:
    aluno = input('\nNome do aluno: ')
    print(f'\nAluno {aluno} {len(medias)+1}')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    n3 = float(input('Nota 3: '))
    n4 = float(input('Nota 4: '))
    medias.append((n1 + n2 + n3 + n4) / 4)
aprovados = 0
for m in medias:
    if m >= 7.0:
        aprovados += 1
print(f'Alunos com media maior ou igual a 7: {aprovados}')
