# Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um terceiro vetor de 20 elementos,
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. Imprima os três vetores:

import random
vetor1 = random.sample(range(100), 10)
vetor2 = random.sample(range(100), 10)
print(f'Vetor 1: {vetor1}')
print(f'Vetor 2: {vetor2}')
vetor3 = []
for x in range(len(vetor1)):
    vetor3.append(vetor1[x])
    vetor3.append(vetor2[x])
print(f'Vetor 3 Intercalado: {vetor3}')
