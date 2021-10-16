# Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min:

import random
lista = random.sample(range(100), 10)
print(f'Lista: {lista}')
menor = lista[0]
maior = lista[0]
k = 1
while k < len(lista):
    if lista[k] < menor:
        menor = lista[k]
    if lista[k] > maior:
        maior = lista[k]
    k = k + 1
print(f'Menor: {menor}')
print(f'Maior: {maior}')
