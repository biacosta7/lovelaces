lista = []


def calculos(lista):
    soma = 0
    
    for i in range(5):
        num = float(input("Digite um número: "))
        lista.append(num)
        soma = soma + num

    
    maior = menor = lista[0]

    for n in lista:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
    
    media = soma/5

    print(f'Menor: {menor}')
    print(f'Maior: {maior}')
    print(f'Média: {media}')

calculos(lista)