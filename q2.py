
lista = []
pares = []
for i in range(5):
    num = float(input("Digite um número: "))
    lista.append(num)


for num in lista:
    if num % 2 == 0:
        pares.append(num)

print(pares)
