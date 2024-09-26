#9° atividade - parte 1

sexo = []
idade = []
respostas = []
resp = "S"
qtd = 0
qtd_masc = 0
qtd_femi = 0
maior = 0
menor = 0
qtd_resp_s = 0
qtd_resp_n = 0
qtd_maior_gosta = 0
qtd_menor_gosta = 0
while resp == "S" or resp == "s":
    sexo.append(input("Qual e o seu sexo(M/F): "))
    idade.append(int(input("Qual a sua idade: ")))
    respostas.append(input("Voce gostou do produto (S/N)? "))
    qtd = qtd + 1
    if sexo == "M" or sexo == "m" and idade < 18 and respostas == "S" or respostas == "s":
        qtd_masc += 1
    elif sexo == "F" or sexo == "f" and idade > 18 and respostas == "S" or respostas == "s":
        qtd_femi += 1
    elif respostas == "S" or respostas == "s":
        qtd_resp_s += 1
    elif respostas == "N" or respostas == "n":
        qtd_resp_n += 1
    elif respostas == "S" or respostas == "s" and idade > 18:
        qtd_maior_gosta += 1
    elif respostas == "S" or respostas == "s" and idade < 18:
        qtd_menor_gosta
    resp = input("Deseja continuar (S/N): ")


print(f"O total de pessoas que participam da pesquisa é {qtd}")
print(f"O numero de pessoas que responderam sim é {qtd_resp_s}")
print(f"O numero de pessoas que responderam Não é {qtd_resp_n}")
print(f"Quantas pessoas menores de 18 anos gostaram do produto é {qtd_menor_gosta}")
print(f"Quantas pessoas maiores de 18 anos gostaram do produto é {qtd_maior_gosta}")
print(f"Quantas pessoas maiores de 18 anos do sexo feminino gostaram do produto {qtd_femi}")
print(f"Quantas pessoas menores de 18 anos do sexo masculino gostaram do produto {qtd_masc} ")