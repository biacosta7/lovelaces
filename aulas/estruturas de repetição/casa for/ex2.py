'''Desenvolva um programa que inclui um jogo de adivinhação. O
computador irá gerar um número aleatório entre 1 e 10, e o usuário
terá 5 tentativas para tentar adivinhar qual número foi gerado. O
programa fornecerá dicas de se o número digitado pelo usuário é
menor ou se é maior que o número gerado pelo computador após
cada tentativa para ajudar o usuário a adivinhar o número
corretamente.'''

'''
x = generate randon(1,11)

user input up to 5 times

output : if the input > or < than x 
or is it the exact value of x = break loop, well done

'''

import random

x = random.randint(1, 10)
print('Bem vindo(a) ao Jogo de Adivinhação... \n')

for tentativas in range(1, 6):

    user = int(input('Digite um número >>> '))

    if user > x:
        print('- Chute um número menor - \n')

    elif user < x:
        print('- Chute um número maior - \n')

    elif user == x:
        print()
        print('Parabéns, você acertou!')
        break

if tentativas == 5:
    print()
    print('Limite de tentativas esgotado.')

print(' ' * 4, 'RESPOSTA:', x)
print()
print('=' * 5,'GAME OVER', '=' * 5 )

