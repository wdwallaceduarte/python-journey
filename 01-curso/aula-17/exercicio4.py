# Escreva uma funçaõ chamada eh_primo que receba um número interio e retorne True se o numero for primo e false caso contrário.

def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


num = int(input('Digite um número: '))
print(f'O número {num} é prino? \33[32m{eh_primo(num)}\33[0m')
