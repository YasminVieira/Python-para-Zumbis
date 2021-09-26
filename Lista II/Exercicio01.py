# Faça um Programa que peça os três lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno:

a = int(input('Qual o valor do lado a do triângulo: '))
b = int(input('Qual o valor do lado b do triângulo: '))
c = int(input('Qual o valor do lado c do triângulo: '))
if a > b + c or b > a + c or c > a + b:
    print('Não pode ser um Triângulo')
    print('Um dos seus lados é maior do que a soma dos outros dois')
elif a == b == c:
    print('É um Triângulo Equilátero')
elif a == b or a == c or b == c:
    print('É um Triângulo Isósceles')
else:
    print('É um Triângulo Escaleno')