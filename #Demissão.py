#Demissão
MyEmpres = input("nome da empresa?: ")
MyRh = input("nome do gestor?: ")
MyRole = input("Meu cargo na empresa?: ")
MyDataDoAviso = input("Data do aviso previo?: ")
MyDdTdAP = input("Data do termino do aviso previo?: ")
MyDataLocal = input("data é Hora?: ")
Myass = input("Sua assinatura?: ")
MyName = input("Seu nome completo?: ")

#carta pronta
print("A", MyEmpres)
print("Prezado(a)", MyRh)
print("Venho por meio dessa carta comunicar formalmente meu pedido de demisão do seguinte crago:", MyRole)
print(f"Estarei a disposição da empresa para comunicação dentre esse periodo {MyDataDoAviso} a {MyDdTdAP} ")
print(f"{MyDataLocal} ")
print(f"{Myass}")
print(f"{MyName}")