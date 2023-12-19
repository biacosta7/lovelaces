frase = input("Digite um frase: ").lower().split()
soma = 0

for i in frase:
    for letra in i:
        print(letra)
        if letra != "a" or "e" or "i" or "o" or "u":
            soma += 1
print(soma)