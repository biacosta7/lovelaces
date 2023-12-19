''''
Faça um programa que solicite ao usuário a inserção de 5 nomes e 5 idades por meio de um laço “for” e exiba na tela esses 5 nomes, às 5 idades e a soma das 5 idades.
'''

soma_idades = 0

for i in range(5):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))

    soma_idades += idade
    print('Nome:', nome)
    print('Idade:', idade)

print()
print('Total das idades:', soma_idades)