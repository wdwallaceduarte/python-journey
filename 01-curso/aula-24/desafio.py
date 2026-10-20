import json

try:
    with open("alunos.json", "r", encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
        # print(dados)
        alunos = dados['alunos'] # comando acrescentado
        print(f"\n Turma: {dados["turma"]}\n")
except Exception as erro:
    print(f'Erro ao ler o arquivo: {erro}')

ids_encontrados = []
aprovados = 0
soma_medias = 0

for aluno in alunos:
    if aluno["id"] in ids_encontrados:
        print("\nID duplicado:", aluno["id"])
    ids_encontrados.append(aluno["id"])
    
    nome = aluno["nome"]
    notas = aluno["notas"]
    try:
        media = sum(notas) / len(notas)
    except TypeError as erro:
        print(f'Erro ao ler a nota do do aluno {nome}: {erro}')
    
    if aluno["ativo"] == True: # Erro de sintax faltando um '='
        situacao = "Ativo"
    else:
        situacao = "Inativo"
    if media >= 7:
        resultado = "Aprovado"
        aprovados += 1
    else:
        resultado = "Reprovado"
    
    soma_medias += media
    print(f"""{nome}: {media:.1f} | {situacao} | {resultado}
--------------------------------------
    """)
    
print("\nTotal de alunos:", len(alunos))
print(f"Média geral: {soma_medias / len(alunos):.1f}") # estava 'alunos', correto 'aluno'
print("Aprovados:", aprovados)
print()