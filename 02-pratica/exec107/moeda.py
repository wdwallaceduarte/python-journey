def aumentar(p):
    res = p + (p * 0.10)
    return res

def diminuir(p):
    res = p - (p * 0.13)
    return res

def dobro(p):
    res = p * 2
    return res

def metade(p):
    res = p / 2
    return res




def moeda(p):
    pass

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



