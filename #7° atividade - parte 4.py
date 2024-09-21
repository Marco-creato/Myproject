#7° atividade - parte 4

resp = "S"

sexo = []
idade = []
olhos = []
cabelos = []
pessoas = []
sexo_f = 0
olhos_cabelos = 0


while resp == "S" or resp == "s":
    sexo.append(input("Qual e o seu sexo?(M/F): "))
    olhos.append(input("Qual a cor dos seu solhos?((A)Azul/(V)Verde/(C)Castanhos): "))
    cabelos.append(input("Qua a cor dos seus cabelos?((L)louros/(C)castanhos/(P)pretos): "))
    idade.append(input("Qual a sua idade?: "))
    resp = input("Deseja continuar(S/N): ")

maior_idade = max(idade)
for i in range(len(idade)):
    if (sexo == "F" or  sexo == "f") and (idade >= 18 and idade <= 35):
        sexo_f += 1
    if (olhos == "V" or olhos == "v") and (cabelos == "L" or cabelos == "l"):
        olhos_cabelos += 1

print(f"A maior idade é {maior_idade}.")
print(f"Número de mulheres entre 18 e 35 anos é {sexo_f}.")
print(f"A quantidades de individuos com olhos verdes e cabelos louros é {olhos_cabelos}.")