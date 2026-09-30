# Foram anotadas as idades e alturas de 30 alunos. Faça um program que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

idades = []
alturas = []

# Ler os dados dos 30 alunos
for i in range(30):
    idade = int(input(f"Digite a idade do aluno {i + 1}: "))
    altura = float(input(f"Digite a altura do aluno {i + 1}: "))

    idades.append(idade)
    alturas.append(altura)

# Calcula a média das alturas
media = sum(alturas) / 30

# Conta alunos com mais de 13 anos e altura abaixo da média
quantidade = 0

for i in range(30):
    if idades[i] > 13 and alturas[i] < media:
        quantidade += 1

print(f"Média das alturas: {media:.2f} m")
print(f"Quantidade de alunos: {quantidade}")
