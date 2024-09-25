#8° atividade

def calcular(num,unidade): #criando a função principal
    def m(n): #criando a fução metro
        return n/100
    def cm(n): # criando a função centimetro
        return n*100
    if unidade == "m":
        result = "{} centimetros.".format(cm(num))
    elif unidade == "cm":
        result = "{} metros.".format(m(num))
    else:
        result = "Verifique a unidade de medida."
    return result
#coletando os dados
while True:
    try:
        n = int(input("Informe o valor da medida: "))
        u = input("Informe a unidade de medida (cm ou m): ")
    except ValueError:
        print("Verifique a entrada de dados")
    else:
        print(calcular(n,u)) #chamando a função principal
        break