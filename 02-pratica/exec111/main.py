# Crie um `pacote` chamado `utilidadesPack` que tenha dois `módulos internos` chamados `modea` e `dado`;
# Transfira todos as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.   


# import exec111.utilidadesPack
from exec111.utilidadesPack import moeda
p = float(input('\nDigite o preço: R$ '))
a = int(input('Quantos % de aumento: '))
r = int(input('Quantos % de redução: '))

moeda.resumo(p, a, r)

# Para testar rode o comando `python -m exec111.main` a partir do diretorio 02-pratica/
""" Porque precisa rodar dessa forma?
    Isso acontece porque o Python procura o pacote a partir do diretório do script (02-pratica/exec111). Para encontrar exec111, ele precisaria procurar dentro desse diretório — como se esperasse outro exec111 ali. Mas o pacote está no próprio diretório atual, então o Python não o encontra.

    Executar como módulo resolve isso porque você informa ao Python o contexto do pacote.
"""