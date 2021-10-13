# Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides:

# O algoritmo de Euclides é um dos primeiros algoritmos para calcular o máximo divisor comum:

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
while a % b != 0:
    a, b = b, a%b
print(f'mdc = {b}')
