import sqlite3

conexao = sqlite3.connect('exemplo.db')  # comando para cirar o banco de dados
cursor = conexao.cursor()

# # COMANDO PARA CRIAR UMA TABELA
# cursor.execute(''' CREATE TABLE IF NOT EXISTS alunos (
#     id INTEGER PRIMARY KEY AUTOINCREMENT, 
#     nome TEXT NOT NULL,
#     idade INTEGER,
#     curso REAL 
#   ) 
#  ''')

# # COMANDO PARA INSERIR DADOS NA TABELA
cursor.execute( ''' 
    INSERT INTO alunos (nome, idade, curso) VALUES 
    ('Wallace', '38', 'Programador de sistema'),  
    ('Daniele', '36', 'Programador Web'),  
    ('Duarte', '38', 'Rust')  
''')

# # COMANDO PARA REALIZAR BUSCA NA TABELA
#  SELECT * FROM tabela_carros # retorna toda a lista
#  SELECT * FROM tabela_carros WHERE preco < 70000 # retorna somente as entidades com preço menor que 70.000

# Confirma a transação
conexao.commit()  # executa o comando SQL