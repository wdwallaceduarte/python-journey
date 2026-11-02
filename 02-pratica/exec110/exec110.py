# Adicione ao módulo `moeda.py` criado nos desafios anteriores, uma função chamada `resumo()`, que mostre na tela algumas inofrmações geradas pelas funções que já temos no módulo criado até aqui.  

import moeda
# from exec109 import moeda

p = float(input('\nDigite o preço: R$ '))
a = int(input('Quantos % de aumento: '))
r = int(input('Quantos % de redução: '))

moeda.resumo(p, a, r)
