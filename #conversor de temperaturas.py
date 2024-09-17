#conversor de temperaturas
print("qual a temperatura você quer converter?")
print("1.Fahrenheit para ...")
print("2. Kelvin para ...")
print("3 .Celsius para ...")
TEMP = int(input())


match TEMP:
    case 1:
       F = float(input('Entre com a temperatura em graus Fahrenheit: '))
       print("Convetendo Fahrenheit para Celsius é?")
       C = (F - 32) * (5 / 9)
       print('Valor em Celsius: {0}°C'.format(C))
       print("Convetendo Fahrenheit para Kelvin é?")
       K = F + 459.67 * 5 / 9
       print('Valor em Kelvin: {0}°K'.format(K))
    case 2:
        K = float(input("Digite a temperatura em Kelvin: "))
        print("Convetendo Kelvin para Celsius é?")
        C = K - 273
        print('Valor em Celsius: {0}°C'.format(C))
        print("Convetendo Kelvin para Fahrenheit é?")
        F = 1.8 * (K - 273) + 32
        print('Valor em Fahrenheit: {0}°F'.format(F))
    case 3:
        C = float(input("Digite a temperatura em Celsius: "))
        print("Convetendo Celsius para Fahrenheit é?")
        F = ((C * 9) / 5) + 32
        print('Valor em Fahrenheit: {0}°F'.format(F))
        print("Convetendo Celsius para Kelvin é?")
        K = C + 273
        print('Valor em Kelvin: {0}°K'.format(K))