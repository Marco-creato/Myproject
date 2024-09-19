#6° atividade - parte 1

# Inicializa uma lista vazia
lista = []

# Recebe 10 elementos do usuário
for i in range(10):
    numero = float(input(f"Digite o {i + 1}º elemento: "))
    lista.append(numero)

# Inicializa as variáveis maior e menor com o primeiro elemento do vetor
maior = lista[0]
menor = lista[0]

# Percorre o vetor para encontrar o maior e o menor elemento
for numero in lista:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

# Exibe os resultados
print(f"O maior é {maior:.0f} o menor é {menor:.0f}")