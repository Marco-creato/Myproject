#futebol
print("Qual desses você é?")
print("1. carioca")
print("2. paulista")
print("3. mineiro")
ESTADO = int(input())

match ESTADO:
    case 1:
        print("Qual o seu time do coração?")
        print("1. Flamengo")
        print("2. Vasco")
        print("3. Bota fogo")
        CARI = int(input())
        if CARI == 1:
            print("Venha jogar com o mengão")
        elif CARI == 2:
            print("Vamos fazer o nosso time voltar ao triunfo")
        elif CARI == 3:
            print("Vamos tacar fogo nos inimigos com agente")
    case 2:
        print("Qual o seu time do coração?")
        print("1. São paulo")
        print("2. Corinthias")
        print("3. Palmeiras")
        LISTA = int(input())
        if LISTA == 1:
            print("Venha junto nessa nossa jornada para o mundial")
        elif LISTA == 2:
            print("Vamos esmagar os nossos inimigos")
        elif LISTA == 3:
            print("Vamos fazer todos conhecer o Palmeiras")
    case 3:
        print("Qual o seu time do coração?")
        print("1.Atlético")
        print("2.Cruzeiro")
        print("3.América")
        MINE = int(input())
        if MINE == 1:
            print("Venha com agente fazer o Atlético creser")
        elif MINE == 2:
            print("Vamos fazer o mundo conhecer o nome cruzeiro")
        elif MINE == 3:
            print("Vamos mostra pra eles a nossa América")
