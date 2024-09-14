#4º atividade

print("============================================")
#primeira parte
print("Digite um valor do qual você quer saber a tabuada")
NUMERO = int(input())
print("========================")
for X in range (0, 10):
    X = X + 1
    print(NUMERO * X)




print("============================================")

#segunda parte
print("Qual o melhor time de futebol?")
CONTADOR = 0; time = ""
while time != "Vasco":
    print("Qual é o time?")
    time = input()

    if time == "Vasco":
        print("time correto")
        break
    else:
        print("time incorreto!")
    CONTADOR = CONTADOR + 1
    if CONTADOR == 5:
        print("tenativa excedida")
        break

print("============================================")

#terceira parte
print("contagem regressiva")

import time

INICIO = 10

for X in range (INICIO, 0, -1):
    print(X)
    time.sleep(1)

print("Feliz Ano novo!")

print("============================================")

#quarta parte
X = 0
Y = 1

limite = 2000
while X <= limite:
    print(X)
    Z = X
    X = Y
    Y = X + Z

print("============================================")

#quinta parte
Valor = float(input("Qual o valor do produto? "))
OT = int(input("Em quantas parcelas você ira pagar? "))
taxa = float(input("Qual a taxa a ser cobrada? "))
ACUMULADO = 0
parcela = Valor / OT
for X in range (0, OT):
    print(f"deseja pagar a {X+1}º parcela?")
    pagar = input()
    if pagar == "sim":
        parcela = parcela * (1 + taxa)
        ACUMULADO = ACUMULADO + parcela
        print("O acumulado é:", ACUMULADO)
    else:
        break