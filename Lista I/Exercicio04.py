# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário:

salario = float(input('Qual o valor do salário: '))
p_aumento = int(input('Qual a porcentagem do aumento: '))
aumento = (p_aumento / 100) * salario
print('O valor do aumento é de R$ {}'.format(aumento))
print('O valor do novo salário com aumento é de R$ {}'.format(salario + aumento))