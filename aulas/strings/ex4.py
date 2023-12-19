palavra = input("Digite uma palavra: ")
invertida = palavra[::-1]

if palavra == invertida:
    print("palíndromo")
else:
    print("não é um palíndromo")

print(palavra)
print(invertida)