'''Escreva um programa em Python que solicita ao usuário inserir um número inteiro,
representando o número de interações desejadas. Em seguida, o programa deve pedir ao
usuário para inserir um número real em cada interação. Após cada inserção, o programa
deve mostrar a soma acumulada dos números inseridos até o momento. O processo deve
se repetir de acordo com o número de interações especificado pelo usuário. Mostre o
resultado da soma final na tela.'''
soma = 0
numInteracoes = int(input("Digite um número inteiro: ")) 

for i in range(numInteracoes):
    numReal = float(input("Digite um número: "))
    soma += numReal
    print('Soma:', soma)

print('\nSoma final:', soma)
