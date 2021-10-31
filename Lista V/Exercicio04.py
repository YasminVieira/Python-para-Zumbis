# Questão D: Daniela é uma pessoa muito supersticiosa. Para ela, um número é sortudo se ele contém o dígito 2 mas não o digíto 7.
# Então na opinião dela, quantos números sortudos existem entre 18644 e 33087, incluindo os extremos?

# Dica: em geral, fica mais fácil trabalhar com textos

cont = 0
for i in range(18644, 33088):
    lista = str(i)
    if '2' in lista and '7' not in lista:
        cont = cont + 1

print('Existem {} números sortudos entre 18644 e 33087'.format(cont))
