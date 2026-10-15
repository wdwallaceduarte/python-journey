
# abrir/cria um arquivo de texto e escrever seu conteúdo ('w' write)
arquivo = open('exemplo.txt', 'w', encoding='utf-8')
arquivo.write('Wallace\n')
arquivo.close()

# Abrir um arquivo de texto e ler seu conteúdo ('r' read)
arquivo = open('exemplo.txt', 'r', encoding='utf-8')
conteudo = arquivo.read()
print(arquivo)
arquivo.close()

# Abrir um arquivo e add mais conteúdo com o modo ('a' append)
arquivo = open('exemplo.txt', 'a', encoding='utf-8')
arquivo.write('Wallace Duarte\n')
arquivo.close()


with open('exemplo.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
# o arquivo é fechado automaticamente apos o bloco 

try:
    with open('exemplo.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print('Erro: O  arquivo não foi encontrado')
except Exception as e:
    print(f'Erro ao ler arquivo: {e}')


try:
    # Tente executar isto
    print(10 / 0)

except ZeroDivisionError:
    # Se acontecer este erro, faça isto
    print("Erro: divisão por zero!")
