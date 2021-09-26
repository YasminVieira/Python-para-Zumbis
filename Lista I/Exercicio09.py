# Escreva um programa que pergunte a quantidade de km percorridos
# por um carro alugado pelo usuário
# assim como a quantidade de dias pelos quais o carro foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado

km = int(input('Qual a quantidade de Km percorridos: '))
dias = int(input('Qual a quantidade de dias que o carro foi alugado: '))
pagar = float((dias * 60) + (km * 0.15))
print('O preço a pagar pelo usuário é de R$ {:.2f}'.format(pagar))