# Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem:
# vm = d / t  =>  t = d / vm 

distancia = int(input('Qual a distância a ser percorrida em Km: '))
velocidade = int(input('Qual a velocidade média esperada em Km/h: '))
tempo = distancia / velocidade
print('O tempo de uma viagem de carro será: {:.0f} hora(s)'.format(tempo))