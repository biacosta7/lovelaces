palavra = input("Digite uma palavra: ").split()
vogais = ["a", "e", "i", "o", "u"]

caracteres =len(palavra)
print(caracteres)

palavra.lower()

if palavra[0] == "a" or "e" or "i" or "o" or "u":
    print("vogal")
else:
    print("consoante")
