#oque você ira fazer...
print("Oque você ira fazer amanhã de manhã?")
print("dormir / estudar / planejar")
MANHÃ = input()
print("OQue você ira fazer amanhã a tarde?")
print("jogar / treinar / trabalhar")
TARDE = input()

if not MANHÃ or not TARDE:
    print("Você precisa dizer o que vai fazer!")
else:
    if MANHÃ == "dormir" or TARDE == "jogar":
        print("Você esta desperdiçando o seu dia")
    elif MANHÃ == "estudar" or TARDE == "treinar":
        print("Que bom! você ira se aperfeiçoar!")
    elif MANHÃ == "planejar" or TARDE == "trabalhar":
        print("Para trabalhar melhor devo planejar")
    else:
        print("Não combinamos estas ações...")

print("Tenha um bom dia!!")