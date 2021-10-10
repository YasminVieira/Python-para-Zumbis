# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto,
# quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido.
# Calcule os descontos e o salário líquido, conforme a tabela abaixo:

# +Salário Bruto : R$
# -IR (11%) : R$
# -INSS (8%) : R$
# -Sindicato ( 5%) : R$
# =Salário Liquido : R$

hora = float(input('Ganhos por hora: '))
horas_trabalhadas = int(input('Horas trabalhadas no mês: '))
bruto = hora * horas_trabalhadas
ir = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05
descontos = ir + inss + sindicato
liquido = bruto - descontos

print('+Salário Bruto:\t\t R$ {:.2f}'.format(bruto))
print('-IR (11%):\t\t R$ {:.2f}'.format(ir))
print('-INSS (8%):\t\t R$ {:.2f}'.format(inss))
print('-Sindicato (5%):\t R$ {:.2f}'.format(sindicato))
print('=Salário Liquido:\t R$ {:.2f}'.format(liquido))