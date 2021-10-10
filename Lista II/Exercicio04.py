# Faça um Programa que leia três números e mostre o maior deles:

n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))
if n1 > n2 and n1 > n3:
    print('{} é o maior número'.format(n1))
elif n2 > n3:
    print('{} é o maior número'.format(n2))
else:
    print('{} é o maior número'.format(n3))