'''Implemente uma calculadora com suas funções básicas: soma, subtração,
multiplicação e divisão. No programa principal o usuário deve informar dois
números e escolher a operação que quer efetuar.

O programa chamará a função de acordo com a operação escolhida e
retornará o resultado (uma função para cada operação).
A cada interação pergunte se o usuário deseja escolher uma nova operação
ou encerrar a execução.

Na operação de divisão, divida o maior número pelo menor.'''

def soma(num1, num2):
    print(f'{num1} + {num2} = {num1 + num2}')

def subtracao(num1, num2):
    print(f'{num1} - {num2} = {num1 - num2}')

def multiplicacao(num1, num2):
    print(f'{num1} * {num2} = {num1 * num2}')
    
def divisao(num1, num2):
    print(f'{num1} / {num2} = {num1 / num2}')

opcao = int(input("\nEscolha: \n1-Soma\n2-Subtração\n3-Multiplicacao\n4-Divisao\n5-Sair\n"))

num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))

def calculadora(num1, num2, opcao):
    if opcao == 1:
        soma(num1, num2)
    if opcao == 2:
        subtracao(num1, num2)
    if opcao == 3:
        multiplicacao(num1, num2)
    if opcao == 4:
        divisao(num1, num2)
    else:
        print("Opção inválida.")

print(calculadora(num1, num2, opcao))


    
    

