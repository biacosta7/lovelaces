''''
Desenvolva um programa em Python que permita ao usuário inserir uma lista de itens
de mercado, separados por espaço. O programa deverá organizar alfabeticamente
essas palavras e exibir cada palavra em uma linha separada.
Implemente um código que, após receber a entrada do usuário, converta-a em uma
lista de palavras. Em seguida, ordene alfabeticamente essa lista e imprima cada
palavra resultante em uma linha separada.'''

lista = input("Digite lista de itens de mercado, (separados por espaço): " ).split()
lista.sort()

for n in lista:
    print(n)