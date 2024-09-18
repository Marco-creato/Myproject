#vetor 3
notas = []
resp = "S"
resultado = 0
#iniciando o bloco de repeticão
while resp == "S" or resp == "s":
    #alimentando a lista
    notas.append(float(input("Informe as Notas: ")))
    resp = input("Deseja Continuar (S/N)? ")
#finalizando o bloco de repeticão
#iniciando o bloco de repeticão
for i in range(len(notas)):
    print(notas[i]) # Exibindo o conteudo da lista
    resultado = sum(notas) # somando as notas
#finalizando o bloco de repeticão
print(f"A media das suas notas é {resultado / len(notas)}")
