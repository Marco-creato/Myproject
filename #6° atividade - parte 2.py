#6° atividade - parte 2

# Inicializa uma lista vazia
vetor = []

# Recebe 10 números inteiros do usuário
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    vetor.append(numero)

# Contador de pares e ímpares
pares = 0
impares = 0

# Conta os números pares e ímpares
for numero in vetor:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Mostra os resultados
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")

# Mostra o vetor na ordem inversa usando reverse
vetor_inverso = vetor.copy()  # Cria uma cópia
vetor_inverso.reverse()
print("Vetor na ordem inversa:", vetor_inverso)

# Mostra o vetor na ordem crescente
vetor_crescente = sorted(vetor)
print("Vetor na ordem crescente:", vetor_crescente)
