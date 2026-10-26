import sqlite3
conexao = sqlite3.connect('exemplo.db')
cursor = conexao.cursor()

def criar_banco():
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Alunos (
                    ID INTEGER PRIMARY KEY,
                    Nome TEXT NOT NULL,
                    Idade INTEGER,
                    Curso TEXT) ''')
    # Confirmar a transação
    conexao.commit()

def inserir_dados():
    nome = input("Nome: ")
    idade = int(input("idade: "))
    disciplina = input("Curso: ")
    cursor.execute('''
        INSERT INTO Alunos (NOME, IDADE, CURSO) VALUES(?,?,?);''',
                   (nome, idade, disciplina))

    conexao.commit()

def consultar_dados():
    nome = input('Nome: ')
    cursor.execute(""" 
        SELECT * FROM alunos WHERE nome LIKE ? """, ('%'+nome+'%',))
    dados = cursor.fetchall()
    
    for alunos in dados:
        print(alunos)

def deletar_dados(id_aluno):
    # Método 1
    # cursor.execute( 
    #  """DELETE FROM alunos WHERE nome = ? """, 
    #  (id_aluno,)
    # )
    # conexao.commit()
    
    # print('Aluno deletado com sucesso!')
    
    # Método 2
    # cursor.execute(
    #     "DELETE FROM alunos WHERE id = ?",
    #     (id_aluno,)
    # )
    #   ********
    # if cursor.rowcount > 0:
    #     conexao.commit()
    #     print("Aluno deletado com sucesso!")
    # else:
    #     conexao.rollback()
    #     print("Nenhum aluno encontrado com esse ID.")
    #   ********
    # Método 3 
    tamanho = consultar_dados()
    id_del = int(input('Id que deseja deletar: '))
    if id_del < 0:
        print('Valor invalido')
    else:
        cursor.execute(""" 
            DELETE FROM alunos WHERE id ? """, (id_del,)
        )


def atualizar_dados(id_aluno, atualizar_nome, atualizar_idade, atualizar_curso):
    pass
    cursor.execute(""" 
        UPDATE alunos
        SET nome = ?, idade = ?, curso = ? 
        WEHERE id = ?""", (id_aluno, atualizar_nome, atualizar_idade, atualizar_curso)
    )

criar_banco()

while True:
    print(""" 
        1 - Add
        2 - Consultar 
        3 - Del
        4 - Atualizar 
    """)
    opcao = input("> ")

    if opcao == "1":
        inserir_dados()
    elif opcao == "2":
        consultar_dados()
    elif opcao == "3":
        deletar_dados(input('ID do Aluno: '))
    elif opcao == "4":
        id_aluno = int(input('ID do Aluno: ')
        atualizar_dados(), input('Novo nome: '), int(input('Nova idade: ')), input('Atualizar curso: '))
    else:
        print("opcao invalida")
        