def aumentar(preco = 0, taxa = 0, formato=False):
    res = preco + (preco * taxa/100)
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

def resumo(p):
    print('-' * 30)
    print('     RESUMO DO VALOR')
    print('-' * 30)
    print(f"""
    Preço analisado: R$ {p}
    Dobro do preço: R$ {dobro(p)}
    Metade do preço: R$ {diminuir(p)}
    80% de aumento: R$ {p + (p * 0.80)}     
    35% de redução: R$ {p - (p * 0.35)}     
    """)



