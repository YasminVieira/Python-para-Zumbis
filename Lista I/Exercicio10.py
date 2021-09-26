# Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
# Considere que um fumante perde 10 minutos de vida a cada cigarro,
# calcule quantos dias de vida um fumante perderá. Exiba o total de dias:

cigarros = int(input('Quantidade de cigarros fumados por dia: '))
anos = int(input('Há quantos anos fuma: '))

# sabendo que 1 ano tem 365 dias, logo:
dias_fumados = anos * 365

# sabendo que 1 dia tem 1440 minutos, logo:
dias_perdidos = ((cigarros * 10) / 1440) * dias_fumados

print('Um fumante perderá {:.0f} dias'.format(dias_perdidos))