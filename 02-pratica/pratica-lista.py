# Variávle `num` que recebe uma lista
num = [2, 5, 9 , 1]
num[2] = 3 # mofica o valor de `9` para `3`
num.append(7) # acdiciona o valor `7` a linsta `num`
num.sort(reverse=True) # Ordena os valores de `num` de forma reversa(decressente)
num.insert(2, 2) # Adiciona `0` a segunda posição
# num.pop(2) # Remove o valor da segunda posição

if 4 in num:
    num.remove(4)
else:
    print(f'Este valor não existe na lista "num"!')

print(num)
print(f'Essa lista tem {len(num)} elementos.')