# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos:

d = int(input('Quantidade de dia(s): '))
h = int(input('Quantidade de hora(s): '))
m = int(input('Quantidade de minuto(s): '))
s = int(input('Quantidade de segundo(s): '))

conversor = s + (m*60) + (h*60*60) + (d*24*60*60)

print('Convertendo tudo dá {} segundos'.format(conversor))