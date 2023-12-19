lista = []
for i in range(5):
    palavra = input("Digite uma palavra: ")
    lista.append(palavra)

print(f'Primeira palavra: {lista[0]}')
print(f'Última palavra: {lista[4]}')
print(f'Três primeiros elementos: {lista[0:3]}')
print(f'Três últimos elementos: {lista[2:5]}')
print(f'Lista invertida: {lista[::-1]}')
