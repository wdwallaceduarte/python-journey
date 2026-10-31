import sqlite3


def conectar_banco():
    try:
        conexao = sqlite3.connect("filmes.db")
        print("Banco de dados conectado com sucesso!")
        return conexao

    except sqlite3.Error as erro:
        print(f"Erro ao conectar ao banco: {erro}")
        return None


def criar_tabela(conexao):
    try:
        cursor = conexao.cursor()

        cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS filmes (
                id INTEGER PRIMARY KEY,
                titulo TEXT NOT NULL,
                ano INTEGER,
                duracao INTEGER,
                nota REAL
            )
        """)
        conexao.commit()
        print('Tabela de filmes criada com sucesso!')
    except sqlite3.Error as erro:
        print(f'\33[31m Erro ao criar a tabela: {erro} \33[0m')


def add_filme(conexao):
    try:
        titulo = input('Título: \n> ')
        ano = int(input('Ano: \n> '))
        duracao = int(input('Duração: \n> '))
        nota = 0.0

        cursor = conexao.cursor()

        cursor.execute(f""" 
            INSERT INTO filmes ( titulo, ano, duracao, nota)
            VALUES('{titulo}', '{ano}', '{duracao}', '{nota}');
        """)
        conexao.commit()
        print('\33[32m Filme adicionado com sucesso! \33[0m')

    except ValueError:
        print('Erro: ano e duração devem ser números inteiros.')

    except sqlite3.Error as erro:
        print(f'Erro ao adicionar filme: {erro}')


def listar_filmes(conexao):
    try:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM filmes")

        filmes = cursor.fetchall()

        if filmes:
            for filme in filmes:
                print(f"""
                ID: {filme[0]}
                Título: {filme[1]}
                Ano: {filme[2]}
                Duração: {filme[3]} H
                Nota: {filme[4]}
                -------------------------
                """)
        else:
            print("Nenhum filme cadastrado.")

    except sqlite3.Error as erro:
        print(f"Erro ao listar filmes: {erro}")


def pesquisar_filme(conexao):
    try:
        print('Digite o nome do filme que deseja buscar.')
        nome = input('Título: \n> ')

        cursor = conexao.cursor()

        cursor.execute("""
            SELECT * FROM filmes
            WHERE titulo LIKE ?
        """, ('%' + nome + '%',))

        dados = cursor.fetchall()

        if dados:
            for filme in dados:
                print(f"""
                    ID: {filme[0]}
                    Título: {filme[1]}
                    Ano: {filme[2]}
                    Duração: {filme[3]} minutos
                    Nota: {filme[4]}
                    -------------------------
                """)
        else:
            print('Nenhum filme encontrado.')

    except sqlite3.Error as erro:
        print(f'Erro ao pesquisar filme: {erro}')


conexao = conectar_banco()

if conexao is not None:
    criar_tabela(conexao)

# Programa Principal
while True:
    print(""" 
           ====== Menu =======
        0 - Criar banco de filmes
        1 - Adicionar Novo Filme
        2 - Listar todos os filmes
        3 - Pesquisar
        4 - Atualizar filme
        5 - Deçetar filme
        6 - Sair
    """)
    opcao = input('> ')

    if opcao == '0':
        criar_tabela(conexao)
    elif opcao == '1':
        print('\nVamos adicionar um novo filme.')
        add_filme(conexao)
    elif opcao == '2':
        listar_filmes(conexao)
    elif opcao == '3':
        pesquisar_filme(conexao)
    elif opcao == '4':
        pass
    elif opcao == '5':
        pass
    else:
        print('Opção inválida!')
