# Faça agora o contrário, de Fahrenheit para Celsius:
# 5 / 9 * (F − 32)

f = int(input('Digite um valor para temperatura em °F: '))
c = 5 / 9 * (f - 32)
print('{:.2f}°F equivale a {:.2f}°C'.format(f, c))