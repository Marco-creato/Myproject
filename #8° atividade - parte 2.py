#8° atividade - parte 2

def calcular(num,unidade): #criando a função principal
    def mais(n):
        return n + x
    def menos(n):
        return n - x
    def divisão(n):
        return n / x
    def multiplicação(n):
        return n * x
    if unidade == "+":
        result = "Valor da adição é {}.".format(mais(num))
    elif unidade == "-":
        result = "Valor da subtração é {}.".format(menos(num))
    elif unidade == "/":
        result = "Valor da Divisão é {}.".format(divisão(num))
    elif unidade == "*":
        result = "Valor da multiplicação é {}.".format(multiplicação(num))
    else:
        result = "Verifique a unidade de calculo."
    return result

while True:
    try:
        n = int(input("Informe um valor: "))
        x = int(input("Informe um numero: "))
        u = input("Informe o metodo de calculo (+ ou - ou / ou *): ")
    except ValueError:
        print("Verifique a entrada de dados")
    else:
        print(calcular(n,u)) #chamando a função principal
        break