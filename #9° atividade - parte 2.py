#9° atividade - parte 2

nome = []
idade = []
sexo = []
altura = []
peso = []
IMC = []
resp = "S"
qtd_masc = 0
qtd_femi = 0
abaixo_peso = 0
peso_normal = 0
sobrepeso = 0
grau1 = 0
grau2 = 0
grau3 = 0
mulher_peso_ideal = 0
homem_peso_ideal = 0
while resp =="S" or resp == "s":
    nome.append(input("Qual e o seu nome: "))
    idade.append(int(input("Qual a sua idade: ")))
    sexo.append(input("Qual o seu sexo: "))
    altura.append(int(input("Qual a sua altura: ")))
    peso.append(int(input("Qual o seu peso: ")))
    resp = input("Deseja continuar (S/N): ")
for i in range(len(sexo)):
    if sexo[i] == "M" or sexo[i] == "m":
        qtd_masc += 1
    elif sexo[i] == "F" or sexo[i] == "f":
        qtd_femi += 1
for i in range(len(peso)):
    IMC.append(peso[i] / (altura[i] * altura[i]))
    if IMC[i] < 18.5:
        abaixo_peso += 1
    elif IMC[i] >= 18.5 and IMC[i] < 24.9:
        peso_normal += 1
        if IMC[i] >= 18.5 and IMC[i] < 24.9 and sexo[i] == "F" or sexo[i] == "f":
            mulher_peso_ideal += 1
        elif IMC[i] >= 18.5 and IMC[i] < 24.9 and sexo[i] == "M" or sexo[i] == "m":
            homem_peso_ideal += 1
    elif IMC [i] >= 25 and IMC[i] < 29.9:
        sobrepeso += 1
    elif IMC [i] >= 30  and IMC[i] < 34.9:
        grau1 += 1
    elif IMC [i] >= 35 and IMC[i] < 39.9:
        grau2 += 1
    elif IMC [i] > 40:
        grau3 += 1
total = grau1 + grau2 + grau3


print(f"Quantidade de pessoas do sexo feminino é {qtd_femi}")
print(f"Quantidade de pessoas do sexo masculino é {qtd_masc}")
print(f"Quantidade de pessoas com obessidade grau I, grau II, grau III é {total}")
print(f"Quantidade de pessoas abaixo do peso é {abaixo_peso}")
print(f"Percentual de pessoas do sexo feminino com peso ideal é {mulher_peso_ideal}")
print(f"Percentual de pessoas do sexo masculino com peso ideal é {homem_peso_ideal}")