def tamanho(frase):
    tam = len(frase)
    return tam

frase = input("Digite a frase: ").split()
print('Número de palavras da frase:', tamanho(frase))