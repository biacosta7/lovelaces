'''Escreva um código que peça para o usuário inserir um número e faça
uma função que receba esse numero e retorne o reverso dele e
imprima esse número na tela

Ex:.
Entrada: 583
Saída: 385'''

num = input("Digite um número: ")

def inverter(num):
    numInvertido = num[::-1]
    return numInvertido

print(f'Número invertido: {inverter(num)}')