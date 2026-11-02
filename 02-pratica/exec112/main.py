# Dentro do pacote `utilidades` que foi criado no desafio111, temos um módulo chamado `dado`. Crie uma função chamada `leiaDinheiro()` que seja capaz de funcionar como a função `input()`, mas com uma `validação de dados` para aceitar apenas valores que sejam `monetários`.  


# import exec112.utilidadesPack
from exec112.utilidadesPack import moeda, dado

p = dado.leiaDinheiro('Digite o preço: ')
a = int(input('Quantos % de aumento: '))
r = int(input('Quantos % de redução: '))

moeda.resumo(p, a, r)

# Para testar rode o comando `python -m exec111.main` a partir do diretorio 02-pratica/
""" Porque precisa rodar dessa forma?
    Isso acontece porque o Python procura o pacote a partir do diretório do script (02-pratica/exec111). Para encontrar exec111, ele precisaria procurar dentro desse diretório — como se esperasse outro exec111 ali. Mas o pacote está no próprio diretório atual, então o Python não o encontra.

    Executar como módulo resolve isso porque você informa ao Python o contexto do pacote.
"""