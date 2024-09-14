#repetições4

CONTADOR = 0; SENHA = ""
while SENHA != "S3nh4":
    print("Digite a senha:")
    SENHA = input()

    if SENHA == "S3nh4":
        print("Senha correta:")
        break
    else:
        print("Senha incorreta...")
    CONTADOR = CONTADOR + 1
    if CONTADOR == 3:
        print("Tentativa excedida!")
        break