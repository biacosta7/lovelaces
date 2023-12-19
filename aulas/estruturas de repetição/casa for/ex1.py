'''
Desenvolva um programa que solicite ao usuário que
ele insira um número. Em seguida o programa deve
calcular e imprimir na tela a tabuada do número
fornecido.
'''

num = int(input('Digite um número: '))

for i in range(1, 11):
    resultado = num * i
    print(num, 'x', i, '=', resultado)
