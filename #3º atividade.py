#3º atividade
#primeira parte
CLUBE = input("Digite o seu time: ")
POSIÇAO = int(input("Digite o lugar na posição: "))

if POSIÇAO == 1:
    print(f"O {CLUBE} é campeão")
elif POSIÇAO >= 1 and POSIÇAO <= 6:
    print(f"O {CLUBE} esta na libertadores")
elif POSIÇAO >= 7 and POSIÇAO <= 12:
    print(f"O {CLUBE} esta na Sul-americana")
elif POSIÇAO >= 13 and POSIÇAO <= 16:
    print(f"O {CLUBE} esta rebaixado")

#segunda parte
LOCAL = input("Digite o estado (RJ/SP/MG/ES): ")
print("Esteve no horario exato do eclipse?")
HORA = int(input("se sim, Digite 0; se não, digite os minutos: "))
DIA = input("O dia esta claro(S/N): ")

if DIA == "S":
    if LOCAL == "RJ" and HORA == 0:
        print(" ecliose total")
    elif (LOCAL == "RJ" or LOCAL == "SP" or LOCAL == "MG" or LOCAL == "ES" and HORA > 0):
        print("eclipse parcial")


#terceira parte
X = int(input("Me informe um numero: "))
Z = int(input("Me informe outro numero: "))
Y = int(input("Me informe outro numero: "))

if X > Z and Z > Y:
    print("esta em ordem decrescente")
elif X < Z and Z < Y:
    print("esta em ordem crescente")
elif X > Z and Z < Y or X < Z and Z > Y:
    print("esta misturado")

#quarta parte
print("Qual posição você gosta de jogar no futebol?")
print("1. Goleiro")
print("2. Zagueiro")
print("3. Lateral")
print("4. ALa")
print("5. volante")
print("6. meio")
print("7. atacante")
print("8. controavante")
print("9. ponta")
FUNÇAO = int(input())

if FUNÇAO >= 1 and FUNÇAO <= 3:
    print("Defesa")
elif FUNÇAO >= 4 and FUNÇAO <= 6:
    print("Meio-Campo")
elif FUNÇAO >= 7 and FUNÇAO <= 9:
    print("Atacante")

#quinta parte
SERVIÇO = input("O serviço foi prestado(S/N): ")
print("Qual a nota você daria pro serviço prestado?")
print("1. Pessimo")
print("2. Ruim")
print("3. Razoavel")
print("4. Bom")
print("5. Otimo")
NOTA = int(input())

if SERVIÇO == "N":
    RECLAMAÇAO = input("Qual a sua reclamação sobre o serviço: ")
else:
    print("Obrigado pela sua opinião!!")

#sexta parte
print("Cada jogador escolha um")
print("papel")
print("pedra")
print("tesoura")
JOGADOR1 = input("jogador 1: ")
JOGADOR2 = input("Jogador 2: ")


if JOGADOR1 == "papel" and JOGADOR2 == "pedra":
    print("Jogador 1 ganhou")
elif JOGADOR1 == "pedra" and JOGADOR2 == "papel" or JOGADOR1 == "papel" and JOGADOR2 == "tesoura" or JOGADOR1 == "tesoura" and JOGADOR2 == "pedra":
    print("Jogador 2 ganhou")
elif JOGADOR1 == "tesoura" and JOGADOR2 == "tesoura" or JOGADOR1 == "pedra" and JOGADOR2 == "pedra" or JOGADOR1 == "papel" and JOGADOR2 == "papel":
    print("Empate")