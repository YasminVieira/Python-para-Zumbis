# Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar:

mercadoria = float(input('Qual é o preço da mercadoria: '))
p_desconto = int(input('Qual o percentual de desconto: '))
desconto = (p_desconto / 100) * mercadoria
print('O valor do desconto é de R$ {:.2f}'.format(desconto))
print('O novo preço a pagar pela mercadoria é de R$ {:.2f}'.format(mercadoria - desconto))