produtos = []
valor = []
soma = 0

for i in range(3):
    p = str(input(f'Digite o nome do Produto:'))
    v = float(input(f'Digite o valor:'))
    produtos.append(p)
    valor.append(v)

print('''Sua conta será paga por meio de PIX ou CARTÃO DE CRÉDITO? '
       [1]PIX
       [2]CARTÃO DE CRÉDITO''')
pag = int(input('Digite o número equivalente a função escolhida: '))

for v in valor:
   soma += v



if pag == 1:
    if soma > 100:
        desc = soma * (15/100)
        soma = soma - desc

print(total)

if pag == 2:
    print(soma)