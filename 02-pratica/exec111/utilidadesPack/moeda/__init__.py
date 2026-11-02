def topo(msg):
    print('-' * 35)
    print(msg.center(35))
    print('-' * 35)

def aumentar(preco = 0, taxa = 0, formato=False):
    """ -> Calcula o aumento de um determinado preço,
     retornando o resultado com ou sem formatação.
      :param preço: o preço que se quer reajustar
      :param taxa: qual é a porcentagem do aumento.
      :param formato: saída formatada (True) ou não (False)
      :return: o valor reajustado, com ou sem fortação.
    """
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)

def diminuir(preco = 0, taxa = 0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)

def dobro(preco = 0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)

def metade(preco = 0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda} {preco:.2f}'.replace('.', ',')

def resumo(preco=0, taxaA=10, taxaR=5):
    topo('RESUMO DO VALOR')

    print(f"""
    Preço analisado: \t{moeda(preco)}
    Dobro do preço: \t{dobro(preco, True)}
    Metade do preço: \t{metade(preco, True)}
    {taxaA}% de aumento: \t{aumentar(preco, taxaA, True)}
    {taxaR}% de redução: \t{diminuir(preco, taxaR, True)}
    """)
    print('-'*35)

