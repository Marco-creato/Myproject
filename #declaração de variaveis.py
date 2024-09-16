#declaração de variaveis
soma_qtd_filhos = 0
soma_renda = 0
maior_renda = 0
qtd_renda = 0
# inicio do codigo
for cont in range(3):
    #coletando dados
    renda = float(input("Informe a renda familliar: "))
    qtd_filhos = int(input("Informe a quantidade de filhos: "))
    #Acumulando dados
    soma_renda = soma_renda + renda
    soma_qtd_filhos = soma_qtd_filhos + qtd_filhos
    #coletando a maior renda
    if renda > maior_renda:
        maior_renda = renda
    #coletando a quantidade de pessoas com renda menor que 1500
    if renda < 1500:
        qtd_renda += 1
#final do codigo
print(f"A Media da renda familiar é {soma_renda/cont}")
print(f"A Media da quantidade de filhos é {soma_qtd_filhos/cont}")
print(f"A maior das rendas é R${maior_renda:.2f}")
print(f"O percentual de pessoas com renda abaixo de R$1500 é {(qtd_renda/cont)*100}")