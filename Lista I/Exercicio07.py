# Converta uma temperatura digitada em Celsius para Fahrenheit
# F = (9 * C / 5) + 32

c = int(input('Digite um valor para temperatura em °C: '))
f = (9 * c / 5) + 32
print('{:.2f}°C equivale a {:.2f}°F'.format(c, f))