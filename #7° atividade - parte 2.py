# 7° atividade - parte 2

nomes = ["Maria", "Marco", "Victor", "Duda", "Cauã", "Raphaela", "Rodrigo", "Daniel", "Miguel", "Micaelly"]
notas = [4, 9, 5, 7, 2, 4, 7, 8, 8, 10]
acima = 0
abaixo = 0


for i in range(10):
    soma = sum(notas)
    media = soma / 10
    if notas[i] > media:
        acima += 1
    else:
        abaixo += 1

maior_nota = max(notas)
indice_maior_nota = notas.index(maior_nota)
nome_maior_nota = nomes[indice_maior_nota]

print("=======================================================")
print(f"A media é {media}.")
print("=======================================================")
print(f"Essa e a quantidade de notas acima da media {acima}.")
print("=======================================================")
print(f"Essa e a quantidade de notas abaixo da media {abaixo}.")
print("=======================================================")
print(f"A pessoa com a maior nota é {nome_maior_nota} com {maior_nota}. pontos.")
print("=======================================================")