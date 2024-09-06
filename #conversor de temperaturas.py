#conversor de temperaturas
C = float(input("Digite a temperatura em Celsius: "))

F = ((C * 9) / 5) + 32
print('Valor em Fahrenheit: {0}°F'.format(F))

K = C + 273
print('Valor em Kelvin: {0}°K'.format(K))

F = float(input('Entre com a temperatura em graus Fahrenheit: '))

C = (F - 32) * (5 / 9)
print('Valor em Celsius: {0}°C'.format(C))

K = F + 459.67 * 5 / 9
print('Valor em Kelvin: {0}°K'.format(K))

K = float(input("Digite a temperatura em Kelvin: "))

C = K - 273
print('Valor em Celsius: {0}°C'.format(C))

F = 1.8 * (K - 273) + 32
print('Valor em Fahrenheit: {0}°F'.format(F))