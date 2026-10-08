# Faça uma função chamada somar_imposto> A função possui dois parâmetros formais:
# taxa_imposto, que é a quantia de imposto sobre vndas expressas em porcentagem, e custo que é o cuso de item antes do imposto. A função "altera" o valor de cusot para incluir o imposto sobre vendas. 

def somar_imposto(taxa_imposto, custo):
    imposto = custo * taxa_imposto / 100
    custo = custo + imposto
    return custo

taxa = float(input("Taxa de imposto: "))
custo = float(input("Custo: "))

print(somar_imposto(taxa, custo))
# resultado = somar_imposto(10, 100)

# 110.0