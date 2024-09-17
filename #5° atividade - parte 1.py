#5° atividade - parte 1
E = 3.70
GC = 5.39
GA = 5.75
D = 4.90
soma_litros = 0
preço = 0


for com in range(1):
    Combustivel = input("Qual dos seguintes tipos de combustivel você deseja(E/GC/GA/D)? ")
    if Combustivel == "E":
        litros = int(input("Quantos litros de Etanol você ira querer? "))
        soma_litros = soma_litros + litros
        preço = preço + soma_litros
        preço = preço * E
        print(f"O preço do Etanol é R${preço:.2f}")
        
    elif Combustivel == "GC":
        litros = int(input("Quantos litros de Gasolina comum você ira querer? "))
        soma_litros = soma_litros + litros
        preço = preço + soma_litros * GC
        print(f"O preço do Gasolina comum é R${preço:.2f}")
        
    elif Combustivel == "GA":
        litros = int(input("Quantos litros Gasolina Aditivada você ira querer? "))
        soma_litros = soma_litros + litros
        preço = preço + soma_litros * GA
        print(f"O preço do Gasolina Aditivada é R${preço:.2f}")
        
    elif Combustivel == "D":
        litros = int(input("Quantos litros de Diesel você ira querer? "))
        soma_litros = soma_litros + litros
        preço = preço + soma_litros * D
        print(f"O preço do Diesel é R${preço:.2f}")