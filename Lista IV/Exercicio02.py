# Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os números ímpares na lista IMPAR.
# Imprima as três listas:

import random
lista = random.sample(range(100), 20)
print(f'LISTA: {lista}')
par = []
impar = []
k = 0
while k < len(lista):
    if lista[k] % 2 == 0:
        par.append(lista[k])
    if lista[k] % 2 != 0:
        impar.append(lista[k])
    k = k + 1
print(f'PARES: {par}')
print(f'ÍMPARES: {impar}')
