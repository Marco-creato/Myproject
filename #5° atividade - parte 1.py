#5° atividade - parte 1
E = 3.70
GC = 5.39
GA = 5.75
D = 4.90
soma_litros = 0
preço = 0
resp = "S"

while resp == "S" or resp == "s":
    Combustivel = input("Qual dos seguintes tipos de combustivel você deseja(E/GC/GA/D)? ")
    if Combustivel == "E" or Combustivel == "e":
        litros = int(input("Quantos litros de Etanol você ira querer? "))
        soma_litros = soma_litros + litros
        preço = preço + soma_litros
        preço = preço * E
        print(f"O preço do Etanol é R${preço:.2f}")
        
    elif Combustivel == "GC" or Combustivel == "gc":
        litros = int(input("Quantos litros de Gasolina comum você ira querer? "))
        soma_litros = soma_litros + litros
        preço = preço + soma_litros * GC
        print(f"O preço do Gasolina comum é R${preço:.2f}")
        
    elif Combustivel == "GA" or Combustivel == "ga":
        litros = int(input("Quantos litros Gasolina Aditivada você ira querer? "))
        soma_litros = soma_litros + litros
        preço = preço + soma_litros * GA
        print(f"O preço do Gasolina Aditivada é R${preço:.2f}")
        
    elif Combustivel == "D" or Combustivel == "d":
        litros = int(input("Quantos litros de Diesel você ira querer? "))
        soma_litros = soma_litros + litros
        preço = preço + soma_litros * D
        print(f"O preço do Diesel é R${preço:.2f}")
    else:
        print("Esse tipo de combustivel não existe!!")
    resp = input("Deseja continuar (S/N)? ")