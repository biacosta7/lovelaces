'''Escreva um programa em Python que solicita ao usuário que insira uma lista de números inteiros. O programa deve 
calcular e imprimir a soma apenas dos números pares presentes na lista.'''

soma = 0
lista = input("Digite uma lista de números inteiros (separados por espaço): ").split()

for i in lista:
    if int(i) % 2 == 0:
        soma += int(i)

print("Soma dos números pares da lista =", soma)

