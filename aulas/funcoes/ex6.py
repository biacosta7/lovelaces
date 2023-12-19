'''Crie um programa em python que utilize função onde ele recebe 5
números inteiros do usuário e retorna:
O menor número

O maior número

Média entre eles'''

lista = []

def calculos(lista):
    for i in range(5):
        num = float(input("Digite um número: "))
        lista.append(num)
    
    maior = menor = lista[0]

    for n in lista:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
    
    media = (menor + maior)/2

    print(f'Menor: {menor}')
    print(f'Maior: {maior}')
    print(f'Média: {media}')

calculos(lista)


'''
def calculoMedia(menor, maior):
    media = (menor + maior)/2
    return media

def min_max(lista):
    maior = menor = lista[0]

    for n in lista:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
    
    print(f'Menor: {menor}')
    print(f'Maior: {maior}')
'''

