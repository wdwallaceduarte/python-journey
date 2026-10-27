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
        consultar_dados()''
    elif opcao == "3":
        deletar_dados(input('ID do Aluno: '))
    elif opcao == "4":
                id_aluno = int(input('ID do Aluno: ')
        atualizar_dados(), input('Novo nome: '), int(input('Nova idade: ')), input('Atualizar curso: '))
    else:
        print("opcao invalida")
        
        
        
        
        
        
        
 
import sqlite3


# 1. Conectar ao banco de dados
def conectar_banco():
    try:
        conexao = sqlite3.connect("filmes.db")
        print("Banco de dados conectado com sucesso!")
        return conexao

    except sqlite3.Error as erro:
        print(f"Erro ao conectar ao banco: {erro}")
        return None


# 2. Criar a tabela de filmes
def criar_tabela(conexao):
    try:
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS filmes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                ano INTEGER,
                duracao INTEGER,
                nota REAL
            )
        """)

        conexao.commit()
        print("Tabela de filmes criada com sucesso!")

    except sqlite3.Error as erro:
        print(f"Erro ao criar a tabela: {erro}")


# 3. Adicionar um novo filme
def add_filme(conexao):
    try:
        titulo = input("Título:\n> ")
        ano = int(input("Ano:\n> "))
        duracao = int(input("Duração em minutos:\n> "))
        nota = 0.0

        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO filmes (titulo, ano, duracao, nota)
            VALUES (?, ?, ?, ?)
        """, (titulo, ano, duracao, nota))

        conexao.commit()
        print("Filme adicionado com sucesso!")

    except ValueError:
        print("Erro: ano e duração devem ser números inteiros.")

    except sqlite3.Error as erro:
        print(f"Erro ao adicionar filme: {erro}")


# 4. Programa principal
conexao = conectar_banco()

if conexao is not None:

    criar_tabela(conexao)

    while True:
        print("""
        ===== MENU DE FILMES =====

        0 - Criar tabela de filmes
        1 - Adicionar novo filme
        2 - Listar todos os filmes
        3 - Pesquisar filme
        4 - Atualizar filme
        5 - Deletar filme
        6 - Sair
        """)

        opcao = input("> ")

        if opcao == "0":
            criar_tabela(conexao)

        elif opcao == "1":
            print("\nVamos adicionar um novo filme.")
            add_filme(conexao)

        elif opcao == "2":
            print("Função de listar filmes ainda será criada.")

        elif opcao == "3":
            print("Função de pesquisar ainda será criada.")

        elif opcao == "4":
            print("Função de atualizar ainda será criada.")

        elif opcao == "5":
            print("Função de deletar ainda será criada.")

        elif opcao == "6":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida!")

    conexao.close()
    print("Conexão com o banco encerrada.")

else:
    print("Não foi possível iniciar o programa.")
