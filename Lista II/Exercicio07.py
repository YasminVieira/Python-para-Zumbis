# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
# Obs. : somente são vendidos um número inteiro de latas:

metros = int(input('Tamanho da área a ser pintada (m²): '))
# 1 lata de 18 litros pintam 54 m²

if metros % 54 == 0:
    latas = metros / 54
else:
    latas = int(metros / 54) + 1

preço = latas * 80
print('Comprar {:.0f} latas de tinta'.format(latas))
print('Pagamento total de R$ {:.2f}'.format(preço))