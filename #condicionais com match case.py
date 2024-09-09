#condicionais com match case

print("qual é o seu estado: ")
print("1. Esta solteiro")
print("2. Esta casado")
print("3. tem filhos")
print("4. tem irmãos")
print("5. mora com os seus pais")
ESTADO = int(input())

match ESTADO:
    case 1:
        print("Eu te desejo boa sorte irmão")
    case 2:
        print("Que bom, eu te desejo felicidades, parceiro")
    case 3:
        print("Perfeito, que eles sejam bem ciudados")
    case 4:
        print("Sabia que eles são os nossos melhores amigos pra vida toda")
    case 5:
        print("Eu recomendo você ir atras dos seus objetivos é sair da asas deles")    
 