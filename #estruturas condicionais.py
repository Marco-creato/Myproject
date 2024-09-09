#estruturas condicionais
print("Qual a sua idade?")
IDADE = int(input())

if IDADE < 18:
    print("Você não é maior de idade!!")
    print("Vcê não tem permissão de usar nossos trabalhos.")
elif IDADE >= 65:
    print("Você já esta pronto pra aposentar?")
    print("Poderemos oferecer nosso suporte tecnico...")
else:
    print("Você é maior de idade!")
    print("Você tem permisão para usar os nossos trabalhos.")

print("Obrigado por optar pelos nossos serviços!")    