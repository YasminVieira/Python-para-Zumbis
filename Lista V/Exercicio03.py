# Questão C: Entre 1067 e 3627 (inclusive), quantos números são pares  e também divisíveis  por 7?

cont = 0
for i in range(1067, 3628):
    if i % 2 == 0 and i % 7 == 0:
        cont = cont + 1

print('Entre 1067 e 3627, existe {} números que são pares e divisíveis por 7'.format(cont))
