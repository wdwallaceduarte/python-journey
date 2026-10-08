# Faça um program que use a funçaõ valor_pagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso epassar estes valores para a funçaõ valor_pagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O program devera então 
# 
#  

def valor_pagamento(valor_prestacao, dias_atraso):
    if dias_atraso == 0:
        return valor_prestacao

    multa = valor_prestacao * 0.03
    juros = valor_prestacao * 0.001 * dias_atraso

    valor_final = valor_prestacao + multa + juros

    return valor_final


quantidade = 0
total = 0

while True:
    prestacao = float(input("Digite o valor da prestação (0 para sair): "))

    if prestacao == 0:
        break

    dias_atraso = int(input("Digite o número de dias de atraso: "))

    valor = valor_pagamento(prestacao, dias_atraso)

    print(f"Valor a pagar: R$ {valor:.2f}")

    quantidade += 1
    total += valor

print("\nRELATÓRIO DO DIA")
print(f"Quantidade de prestações pagas: {quantidade}")
print(f"Valor total recebido: R$ {total:.2f}")