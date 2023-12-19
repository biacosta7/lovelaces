
'''Escreva um programa em Python que solicita ao usuário que insira uma lista de números inteiros. O programa deve calcular e imprimir a soma apenas dos números pares presentes na lista.'''

soma = 0
lista = []

while True:
    num = input("Digite um número inteiro (pressione x para sair): ")

    if str(num) == "x" or str(num) == "X":
        break

    lista.append(int(num))

for n in lista:
    if n % 2 == 0:
        soma += n

print("\nSoma dos números pares presentes na lista:", soma)
