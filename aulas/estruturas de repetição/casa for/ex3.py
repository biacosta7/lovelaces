'''Crie um programa que peça ao usuário para inserir
4 números. E após inserir cada número imprima na
tela se ele é um número positivo, negativo ou igual
a zero. '''

for i in range(1, 5):
    num = int(input('Digite um número: '))
    if num > 0:
        print('Esse número é positivo. \n')
    elif num < 0:
        print('Esse número é negativo. \n')
    elif num == 0:
        print('Esse número é igual a zero. \n')
