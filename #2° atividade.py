#2° atividade
print("-----------------------------------------------")
#primeira parte
print("Qual o seu dia da semana favotiro?")
print("1. Segunda")
print("2. Terça")
print("3. Quarta")
print("4. Quinta")
print("5. Sexta")
print("6. Sabado")
print("7. Domingo")
SEMANA = int(input())

match SEMANA:
    case 1:
        print("Um otimo dia pra relaxar.")
    case 2:
        print("Um otimo dia pra uma corrida")
    case 3:
        print("Um belo dia pra treinar peito é costas")
    case 4:
        print("Um belo dia para treinar pernas")
    case 5:
        print("Um belo dia para descansar depois dos exercicios")
    case 6:
        print("Um otimo dia para se diverti com os seus amigos")
    case 7:
        print("Um perfeito dia para relaxar com a amada assistindo netflix na cama com uma pizza")

print("-----------------------------------------------")

#segunda parte
print("Qual é o seu peso?")
PESO = int(input())
print("Qual a sua altura?")
ALTURA = int(input())

IMC = PESO / (ALTURA * ALTURA)

if IMC > 25:
    print("Acima do peso")
elif IMC < 25:
    print("Abaixo do peso")
elif IMC == 25:
    print("O seu peso esta OK")

print("-----------------------------------------------")

#terceira parte
print("Quaias foram suas notas desse trimestre?")
nota1 = int(input("Primeira nota? "))
nota2 = int(input("qual foi a segunda nota? "))
nota3 = int(input("sua terceira nota? "))
nota4 = int(input("sua quarta nota do trimestre? "))

nota5 = nota1 + nota2 + nota3 + nota4
nota6 = nota5 / 4

if nota6 >= 6:
    print("aprovado!!")
elif nota6 < 6:
    print("Você foi reprovado!!")
print("-----------------------------------------------")