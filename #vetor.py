#vetor
nomes = ["João","Maria","Pedro"]
idades = [30,40,25]

#Exibindo o conteudo das listas

print(nomes[0])
print(idades[0])

#Exibindo todos os conteudos da listas com repeticão

for i in range(len(idades)):
    print(nomes[i])
    print(idades[i])

nomes.append("Marco")
idades.append("18")

#Exibindo todos os conteudos da listas com repeticão

for i in range(len(idades)):
    print(nomes[i])
    print(idades[i])

nomes.append(input("informe um nome: "))
idades.append(int(input("informe uma idade: ")))

#Exibindo todos os conteudos da listas com repeticão

for i in range(len(idades)):
    print(nomes[i])
    print(idades[i])
