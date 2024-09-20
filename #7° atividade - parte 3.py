# 7° atividade - parte 3

nomes = []

for i in range(10):
    nome = input(f"Digite o {i + 1}° nome: ")
    nomes.append(nome)

print("=======================================================")
nome_busca = input("Digite um nome para verificar: ")
print("=======================================================")

if nome_busca in nomes:
    print("Usuário encontrado!")
else:
    print("Usuário não encontrado!")
