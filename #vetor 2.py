#vetor 2
nomes = ["João","Maria","Pedro"]
idades = [30,40,25]

posiçao = nomes.index("Maria")
print(posiçao)

del nomes[posiçao]
del idades[posiçao]

for i in range(len(idades)):
    print(nomes[i] + " " + str(idades[i]))